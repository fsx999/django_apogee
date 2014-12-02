# coding=utf-8
from django.db import models
from django.db.models import Count
from django.conf import settings

__author__ = 'paul'
liste_diplome = ["LINPSYC", "LININFO", "LINEDUC", "LINDROI", "MANPSYC", 'MANEFIS', 'DSNATAV', 'DSNPCAV']
ANNEE = 2014


class EtapeNonCondiValideManagerOracle(models.Manager):
    def get_query_set(self):
        # from inscription.models import AnneeEnCour
        # annee = AnneeEnCour.objects.get(annee_en_cours=True)

        return super(EtapeNonCondiValideManagerOracle, self).get_query_set().using('oracle').filter(cod_anu=ANNEE,
                                                                                                    eta_iae='E',
                                                                                                    cod_pru__in=['NO',
                                                                                                                 'FP'],
                                                                                                    cod_dip__in=liste_diplome) | super(
            EtapeNonCondiValideManagerOracle, self).get_query_set().filter(cod_anu=ANNEE, eta_iae='E', tem_iae_prm='O',
                                                                           cod_dip__in=liste_diplome)

    def impayes(self):
        return self.filter(ETA_PMT_IAE='A')


class EtapeCondiValideManagerOracle(models.Manager):
    def get_query_set(self):
        return super(EtapeCondiValideManagerOracle, self).get_query_set().using('oracle').filter(cod_anu=ANNEE,
                                                                                                 eta_iae='E',
                                                                                                 cod_dip__in=liste_diplome)


class EtapeCondiValideManager(models.Manager):
    def get_query_set(self):
        return super(EtapeCondiValideManager, self).get_query_set().filter(cod_anu=ANNEE, eta_iae='E',
                                                                           cod_dip__in=liste_diplome)


class EtapeNonCondiValideManager(models.Manager):
    def get_query_set(self):
        return super(EtapeNonCondiValideManager, self).get_query_set().filter(cod_anu=ANNEE, eta_iae='E',
                                                                              cod_pru__in=['NO', 'FP'],
                                                                              cod_dip__in=liste_diplome) | super(
            EtapeNonCondiValideManager, self).get_query_set().filter(cod_anu=ANNEE, eta_iae='E', tem_iae_prm='O',
                                                                     cod_dip__in=liste_diplome)

    def impayes(self):
        return self.filter(ETA_PMT_IAE='A')

        # def nb_paiement(self):
        # result = self.annotate(num_paiement=Count('paiements'))
        # t = {
        #         'nb_paiement1': result.filter(num_paiement=1).count(),
        #         'nb_paiement2': result.filter(num_paiement=2).count(),
        #         'nb_paiement3': result.filter(num_paiement=3).count(),
        #     }
        #     return t


class DiplomeManager(models.Manager):
    def diplome_composante_active(self):
        cmp = settings.CODE_COMPOSANTE
        return
