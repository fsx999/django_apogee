# coding=utf-8
from __future__ import unicode_literals
import autocomplete_light
from django_apogee.models import ComBdi


autocomplete_light.register(
    ComBdi,
    limit_choices=40,
    search_fields=['cod_bdi'],
    attrs={
        "placeholder": u'Veuillez saissir un code postal',
        'data-autocomplete-minimum-characters': 5,
        'class': 'form-control'
    })
