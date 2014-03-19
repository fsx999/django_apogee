# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core import serializers
from django.core.files.temp import NamedTemporaryFile
from django.core.mail import send_mail
from django.core.management import call_command
from django.db import DatabaseError
from django.db.models.loading import get_models, get_app
import django_apogee
from django_apogee.models import AnneeUni


__author__ = 'paul'
from django.core.management.base import BaseCommand
from optparse import make_option
import warnings


class Command(BaseCommand):
    def handle(self, *args, **options):
        #on récupére les personnes du jour (soit la date de création, de modif plus grand que la veille
        print "Verification de connection a oracle"
        error = []
        app = get_app('django_apogee')
        for model in get_models(app):
            if model._meta.db_table not in ['INS_ADM_ETP_COPY', 'COM_BDI_COPY']:
                self.test_connection_model(model, error)
        if error:
            print "Les tables suivantes sont en anomalies " + ' '.join(error)

    def test_connection_model(self, model, error):
        try:
            model.objects.using('oracle').count()
            print "Connection {} réussi".format(model._meta.db_table.encode('utf-8'))
        except DatabaseError as e:
            error.append(model._meta.db_table)
            r = "La connection pour {} a échoué pour la raison suivante {}".encode('utf-8').format(model._meta.db_table, e)
            print r.decode('utf-8')

