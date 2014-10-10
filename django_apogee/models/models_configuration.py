# coding=utf-8
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django_apogee.models import AnneeUni


@python_2_unicode_compatible
class ConfAnneeUni(AnneeUni):
    inscription = models.BooleanField(default=False)
    synchro = models.BooleanField(default=False)

    class Meta:
        app_label = 'django_apogee'
        verbose_name = 'Setting année universitaire'
        verbose_name_plural = u'Settings année universitaire'

    def __str__(self):
        if self.inscription:
            inscription = 'inscription ouverte'
        else:
            inscription = 'inscription fermée'
        return '{} {}'.format(self.cod_anu, inscription)
