# -*- coding: utf-8 -*-
from jeton.models import Ec, EcMaquette

__author__ = 'paul'
from django.core.management.base import BaseCommand
from apogee.models.models_apogee import *


class Command(BaseCommand):

    def handle(self, *args, **options):

        EcMaquette.objects.all().delete()
        Ec.objects.all().delete()
        for etape in EtpGererCge.objects.using('oracle').filter(cod_cge='IED'):
            etape.save_all_ec()
        # EcMaquette.objects.save_ec_apogee('L1NPSY')
        # EcMaquette.objects.save_ec_apogee('L2NPSY')
        # EcMaquette.objects.save_ec_apogee('L3NPSY')
