# -*- coding: utf-8 -*-
from django.core import serializers
from django.core.files.temp import NamedTemporaryFile
from django.core.mail import send_mail
from django.core.management import call_command
from django_apogee.models import InsAdmEtp, Individu, Adresse, AnneeUni

__author__ = 'paul'
from django.core.management.base import BaseCommand
from optparse import make_option


class Command(BaseCommand):

    option_list = BaseCommand.option_list + (
        make_option('--annee',
                    action='store',
                    type="int",
                    dest='annee',
                    default=None,
                    help='annee de remontee'),
    )

    def handle(self, *args, **options):
        liste_diplome = ["LINPSYC", "LININFO", "LINEDUC", "LINDROI", "MANPSYC", 'MANEFIS', 'DSNATAV']
        if options['annee']:
            annee = options['annee']
        else:
            annee = AnneeEnCour.objects.get(annee_en_cours=True).annee
        try:
        #on récupére les personnes du jour (soit la date de création, de modif plus grand que la veille

            self.copy_oracle_base(Individu.objects.using('oracle').filter(etapes__cod_dip__in=liste_diplome,
                                                                          etapes__cod_anu=annee).distinct())

            #ADRESSE annuelle
            self.copy_oracle_base(ADRESSE.objects.using('oracle').filter(cod_ind_ina__etapes__cod_dip__in=liste_diplome,
                                                                         cod_ind_ina__etapes__cod_anu=annee,
                                                                         cod_anu_ina=annee)
                                                                 .exclude(cod_ind_ina__lib_pr1_ind='DOUBLONS'))
            #            #ADRESSE fixe
            self.copy_oracle_base(ADRESSE.objects.using('oracle').filter(cod_ind__etapes__cod_dip__in=liste_diplome,
                                                                         cod_ind__etapes__cod_anu=annee)
                                                                 .exclude(cod_ind__lib_pr1_ind='DOUBLONS'))
            # self.copy_oracle_base(INS_ADM_ANU.objects.using('oracle').filter(
            #     COD_IND__etapes__COD_DIP__in=liste_diplome,
            #                                                                 COD_IND__etapes__COD_ANU=annee)
            #                                                         .exclude(COD_IND__LIB_PR1_IND='DOUBLONS'))

            #            on retire les doublons
            for x in INDIVIDU.objects.using('oracle').filter(lib_pr1_ind='DOUBLONS'):
                x.delete(using='default')

                #on met à jour les etapes (date de modif, annualtion ,création

            for x in INS_ADM_ETP.objects.using("oracle").filter(cod_dip__in=liste_diplome, cod_anu=annee):
                x.save_copy()

            send_mail('remontee', 'la remontee s\'est  bien passée', 'nepasrepondre@iedparis8.net',
                      ['paul.guichon@iedparis8.net'])
        except Exception, e:
            send_mail('remontee', 'la remontee ne s\'est pas bien passée %s' % e, 'nepasrepondre@iedparis8.net',
                      ['paul.guichon@iedparis8.net'])

    def copy_oracle_base(self, queryset):
        fichier = NamedTemporaryFile(suffix='.json')
        data = serializers.serialize("json", queryset)
        fichier.writelines(data)
        fichier.flush()

        call_command('loaddata', fichier.name.__str__())
        fichier.close()
