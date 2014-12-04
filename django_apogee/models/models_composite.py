# coding=utf-8
from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.db.models import get_app, get_model

APOGEE_CONNECTION = getattr(settings, 'APOGEE_CONNECTION', 'oracle')


class classproperty(property):
    def __get__(self, cls, owner):
        return classmethod(self.fget).__get__(None, owner)()


class CompositeInitial(models.Model):
    """
    :attribut: _composite_model_implementation : c'est la classe qui implemente l'id
    :attribut: _composite_field : liste qui indique les clé composites
    """
    _composite_field = []
    _separator = '|'

    @classproperty
    def composite_field(cls):
        return cls._composite_field

    @property
    def composite_key_to_id(self):
        result = []
        for key in self.composite_field:
            value = getattr(self, key)

            if issubclass(value.__class__, models.Model):
                value = value.pk
            if issubclass(value.__class__, int):
                value = str(value)
            result.append(value)
        separator = getattr(self, '_separator', '|')
        return separator.join(result)

    @property
    def kwargs(self):
        result = {}
        for key in self.composite_field:
            value = getattr(self, key)
            if issubclass(value.__class__, models.Model):
                result[key] = value
            else:
                result[key] = str(value)
        return result

    def copy(self, using='default'):
        class_name = getattr(self, '_composite_model_implementation', self.__class__.__name__[:-7])
        class_composite_id = get_model(self._meta.app_label, class_name)
        copy = class_composite_id.objects.using(using).get_or_create(id=self.composite_key_to_id, **self.kwargs)[0]
        result = {field.name: getattr(self, field.name) for field in self._meta.fields}
        for key in self._meta.get_all_field_names():
            value = getattr(self, key)
            if issubclass(value.__class__, models.Model):
                setattr(copy, str(key)+'_id', value.pk)
            else:
                setattr(copy, key, value)
        copy.save(using=using)

    class Meta:
        abstract = True
        app_label = 'django_apogee'


class CompositeImplementation(models.Model):

    @property
    def class_composite_initial(self):
        class_name = getattr(self, '_composite_model_initial', self.__class__.__name__+'Initial')
        return get_model(self._meta.app_label, class_name)

    class Meta:
        abstract = True
        app_label = 'django_apogee'

    @property
    def kwargs(self):
        result = {}
        for key in self.class_composite_initial.composite_field:
            value = getattr(self, key)
            if issubclass(models.Model, value):
                value = value.pk
            result[key] = value
        return result

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.id:
            self.id = self.class_composite_initial.objects.using(APOGEE_CONNECTION).get(**self.kwargs).composite_key_to_id
        super(CompositeImplementation, self).save(force_insert, force_update, using, update_fields)

    @property
    def id_to_composite_key(self):
        cle = self.id.split(getattr(self.class_composite_initial, '_separator', '|'))
        result = {}
        for i, key in enumerate(self.class_composite_initial.composite_field):
            result[key] = cle[i]
        return result
