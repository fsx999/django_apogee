from __future__ import unicode_literals
from rest_framework import serializers
from django_apogee.models import AnneeUni

__author__ = 'juggernut'


class AnneeUniSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnneeUni
        fields = ('cod_anu', 'eta_anu_iae')

