# -*- coding: utf-8 -*-
from django.core import serializers
from django.core.files.temp import NamedTemporaryFile
from django.core.mail import send_mail
from django.core.management import call_command
from django_apogee.models import Individu, Adresse, InsAdmEtpInitial
from django_apogee.models.models_apogee import *
from django.conf import settings
from django.core.paginator import Paginator

__author__ = 'paul'
from django.core.management.base import BaseCommand
APOGEE_CONNECTION = getattr(settings, 'APOGEE_CONNECTION', 'oracle')
COD_CGE = getattr(settings, 'COD_CMP', 'IED')
NB_COPY_INITIALISATION = getattr(settings, 'NB_COPY_INITIALISATION', 5000)

TABLES = [
    AnneeUni,
    Pays,
    Departement,
    SitFam,
    TypHandicap,
    SitMil,
    TypHebergement,
    # SituationSise,
    BacOuxEqu,
    MentionBac,
    # TypEtb,
    # Etablissement,
    # CatSocPfl,
    # QuotiteTra,
    # DomaineActPfl,
    # SituationSise,
    # TypeDiplomeExt,
    # RegimeParent,
    # MtfNonAflSso,
    # SitSociale,
    # Bourse,
    Composante,
    CentreGestion,
    Etape,
    EtpGererCge,
    # Elp,
    # Diplome,
    # SpecialiteVdi,

]

BIG_TABLE = [
    Individu,
    Adresse
]

TABLES_COMPOSITES = [
    ComBdiInitial,
    # CmpHabiliterVdiInitial,
    # VersionDiplomeInitial,
    # VersionEtapeInitial,
    # VdiFractionnerVetInitial,
    # ElpLibelleInitial,
    # InsAdmEtpInitial
]


class Command(BaseCommand):
    def handle(self, *args, **options):
        """
        ligne 88 changer par le code de gestion du centre concerne
        """
        #on récupére les personnes du jour (soit la date de création, de modif plus grand que la veille
        print u"debut de copie"
        for model in TABLES:
            self.copy_oracle_base(model.objects.using(APOGEE_CONNECTION).all())
            print u"La table {} est copiee".format(model._meta.db_table)
        print u"fin de copie des tables normales"
        print u"debut des grosses tables"
        for model in BIG_TABLE:
            p = Paginator(model.objects.using(APOGEE_CONNECTION).all(), NB_COPY_INITIALISATION)
            for page in p.page_range:
                for x in p.page(page).object_list:
                    try:
                        x.save(using='default')
                    except Exception:
                        pass
            print u"La table {} est copiee".format(model._meta.db_table)
        print u"fin de copie des grosses tables"
        print u"debut de copie des tables composites, attention, operation longue"
        for model in TABLES_COMPOSITES:
            p = Paginator(model.objects.using(APOGEE_CONNECTION).all(), NB_COPY_INITIALISATION)
            for page in p.page_range:
                for x in p.page(page).object_list:
                    x.copy()
            print u"La table {} est copiee".format(model._meta.db_table)
        query = InsAdmEtpInitial.objects.using(APOGEE_CONNECTION).filter(cod_cge=COD_CGE, cod_anu__gt=2012)
        p = Paginator(query, NB_COPY_INITIALISATION)
        for page in p.page_range:
            for x in p.page(page).object_list:
                x.copy()
        print u"La table {} est copiee".format(InsAdmEtpInitial._meta.db_table)
        print u"fin de copie"

    def copy_oracle_base(self, queryset):
        fichier = NamedTemporaryFile(suffix='.json')
        data = serializers.serialize("json", queryset)
        fichier.writelines(data)
        fichier.flush()

        call_command('loaddata', fichier.name.__str__())
        fichier.close()
