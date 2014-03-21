# -*- coding: utf-8 -*-
from django.core import serializers
from django.core.files.temp import NamedTemporaryFile
from django.core.mail import send_mail
from django.core.management import call_command
from django_apogee.models.models_apogee import *
from django.conf import settings


__author__ = 'paul'
from django.core.management.base import BaseCommand
APOGEE_CONNECTION = getattr(settings, 'APOGEE_CONNECTION', 'oracle')

TABLES = [
    AnneeUni,
    Pays,
    Departement,
    SitFam,
    TypHandicap,
    SitMil,
    TypHebergement,
    SituationSise,
    BacOuxEqu,
    MentionBac,
    TypEtb,
    Etablissement,
    CatSocPfl,
    QuotiteTra,
    DomaineActPfl,
    SituationSise,
    TypeDiplomeExt,
    RegimeParent,
    MtfNonAflSso,
    SitSociale,
    Bourse,
    Composante,
    CentreGestion,
    Etape,
    EtpGererCge,
    Elp,
    Diplome,



]
TABLES_COMPOSITES = [
    ComBdiInitial,
    CmpHabiliterVdiInitial,
    VersionDiplomeInitial,
    VersionEtapeInitial,
    VdiFractionnerVetInitial,
    ElpLibelleInitial
]


class Command(BaseCommand):
    def handle(self, *args, **options):
        #on récupére les personnes du jour (soit la date de création, de modif plus grand que la veille
        print u"debut de copie"
        for model in TABLES:
            self.copy_oracle_base(model.objects.using(APOGEE_CONNECTION).all())
            print u"La table {} est copiee".format(model._meta.db_table)
        print u"fin de copie des tables normales"
        print u"debut de copie des tables composites, attention, operation longue"
        for model in TABLES_COMPOSITES:
            for x in model.objects.using(APOGEE_CONNECTION).all():
                x.copy()
            print u"La table {} est copiee".format(model._meta.db_table)
        print u"fin de copie"


    def copy_oracle_base(self, queryset):
        fichier = NamedTemporaryFile(suffix='.json')
        data = serializers.serialize("json", queryset)
        fichier.writelines(data)
        fichier.flush()

        call_command('loaddata', fichier.name.__str__())
        fichier.close()
