# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
from django.db import DatabaseError
from django.db.models.loading import get_models, get_app
from django.conf import settings

__author__ = 'paul'
from django.core.management.base import BaseCommand

APOGEE_CONNECTION = getattr(settings, 'APOGEE_CONNECTION', 'oracle')


class Command(BaseCommand):
    def handle(self, *args, **options):
        #on récupére les personnes du jour (soit la date de création, de modif plus grand que la veill
        print "Verification de connection a oracle"
        error = []
        app = get_app('django_apogee')
        for model in get_models(app):
            if not re.match(r'.*_COPY$', model._meta.db_table) and not model._meta.db_table in ['django_apogee_confanneeuni']:
                self.test_connection_model(model, error)
        if error:
            print "Les tables suivantes sont en anomalies : \n" + '\n'.join(error)
        else:
            print "Il n'y a pas d'erreurs de connection"

    def test_connection_model(self, model, error):
        try:
            model.objects.using(APOGEE_CONNECTION).count()
            print "Connection {} réussi".format(model._meta.db_table.encode('utf-8'))
        except DatabaseError as e:
            error.append(model._meta.db_table)
            r = "La connection pour {} a échoué pour la raison suivante {}".encode('utf-8').format(model._meta.db_table, e)
            print r.decode('utf-8')
