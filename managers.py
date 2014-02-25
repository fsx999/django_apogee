# coding=utf-8
from django.db import models
from django.db.models import Count


__author__ = 'paul'
liste_diplome = ["LINPSYC", "LININFO", "LINEDUC", "LINDROI", "MANPSYC", 'MANEFIS', 'DSNATAV']


class EtapeNonCondiValideManagerOracle(models.Manager):
    def get_query_set(self):
        from inscription.models import AnneeEnCour
        annee = AnneeEnCour.objects.get(annee_en_cours=True)
        return super(EtapeNonCondiValideManagerOracle, self).get_query_set().using('oracle'). \
            filter(COD_ANU=annee.annee,
                   ETA_IAE='E',
                   COD_PRU__in=['NO', 'FP'],
                   COD_DIP__in=liste_diplome) \
               | \
            super(EtapeNonCondiValideManagerOracle, self).get_query_set().filter(COD_ANU=annee.annee,
                                                                              ETA_IAE='E',
                                                                              TEM_IAE_PRM='O',
                                                                              COD_DIP__in=liste_diplome)

    def impayes(self):
        return self.filter(ETA_PMT_IAE='A')


class EtapeCondiValideManagerOracle(models.Manager):
    def get_query_set(self):
        from inscription.models import AnneeEnCour
        annee = AnneeEnCour.objects.get(annee_en_cours=True)
        return super(EtapeCondiValideManagerOracle, self).get_query_set().using('oracle').filter(
            COD_ANU=annee.annee,
            ETA_IAE='E',
            COD_DIP__in=liste_diplome)


class EtapeCondiValideManager(models.Manager):

    def get_query_set(self):
        from inscription.models import AnneeEnCour
        annee = AnneeEnCour.objects.get(annee_en_cours=True)
        return super(EtapeCondiValideManager, self).get_query_set().filter(COD_ANU=annee.annee, ETA_IAE='E',
                                                                           COD_DIP__in=liste_diplome)


class EtapeNonCondiValideManager(models.Manager):
    def get_query_set(self):
        from inscription.models import AnneeEnCour
        annee = AnneeEnCour.objects.get(annee_en_cours=True)
        return super(EtapeNonCondiValideManager, self).get_query_set().filter(COD_ANU=annee.annee,
                                                                              ETA_IAE='E',
                                                                              COD_PRU__in=['NO', 'FP'],
                                                                              COD_DIP__in=liste_diplome) \
               | \
            super(EtapeNonCondiValideManager, self).get_query_set().filter(COD_ANU=annee.annee,
                                                                              ETA_IAE='E',
                                                                              TEM_IAE_PRM='O',
                                                                              COD_DIP__in=liste_diplome)

    def impayes(self):
        return self.filter(ETA_PMT_IAE='A')

    def nb_paiement(self):
        result = self.annotate(num_paiement=Count('paiements'))
        t = {
            'nb_paiement1': result.filter(num_paiement=1).count(),
            'nb_paiement2': result.filter(num_paiement=2).count(),
            'nb_paiement3': result.filter(num_paiement=3).count(),
        }
        return t



