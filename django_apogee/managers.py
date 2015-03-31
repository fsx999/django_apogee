# coding=utf-8
from django.db import models
from django.conf import settings

__author__ = 'paul'
liste_diplome = ["LINPSYC", "LININFO", "LINEDUC", "LINDROI", "MANPSYC", 'MANEFIS', 'DSNATAV', 'DSNPCAV']
ANNEE = 2014


class EtapeManager(models.Manager):

    def by_composante(self, code_composante):
        return self.filter(etpgerercge__cod_cmp=code_composante)

    def by_centre_gestion(self, code_centre_gestion):
        return self.filter(etpgerercge__cod_cge=code_centre_gestion)


class EtapeNonCondiValideManagerOracle(models.Manager):
    def get_queryset(self):
        return super(EtapeNonCondiValideManagerOracle, self).get_query_et().using('oracle').filter(cod_anu=ANNEE,
                                                                                                    eta_iae='E',
                                                                                                    cod_pru__in=['NO',
                                                                                                                 'FP', 'DD'],
                                                                                                    cod_dip__in=liste_diplome) | super(
            EtapeNonCondiValideManagerOracle, self).get_queryset().filter(cod_anu=ANNEE, eta_iae='E', tem_iae_prm='O',
                                                                           cod_dip__in=liste_diplome)

    def impayes(self):
        return self.filter(ETA_PMT_IAE='A')


class EtapeCondiValideManagerOracle(models.Manager):
    def get_queryset(self):
        return super(EtapeCondiValideManagerOracle, self).get_queryset().using('oracle').filter(cod_anu=ANNEE,
                                                                                                 eta_iae='E',
                                                                                                 cod_dip__in=liste_diplome)


class EtapeCondiValideManager(models.Manager):
    def get_queryset(self):
        return super(EtapeCondiValideManager, self).get_queryset().filter(cod_anu=ANNEE, eta_iae='E',
                                                                           cod_dip__in=liste_diplome)


class EtapeNonCondiValideManager(models.Manager):
    def get_queryset(self):
        return super(EtapeNonCondiValideManager, self).get_queryset().filter(cod_anu=ANNEE, eta_iae='E',
                                                                              cod_pru__in=['NO', 'FP', 'DD'],
                                                                              cod_dip__in=liste_diplome) | super(
            EtapeNonCondiValideManager, self).get_queryset().filter(cod_anu=ANNEE, eta_iae='E', tem_iae_prm='O',
                                                                     cod_dip__in=liste_diplome)

    def impayes(self):
        return self.filter(ETA_PMT_IAE='A')


class DiplomeManager(models.Manager):
    def diplome_composante_active(self):
        cmp = settings.CODE_COMPOSANTE
        return
