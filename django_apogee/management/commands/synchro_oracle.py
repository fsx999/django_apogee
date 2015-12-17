# -*- coding: utf-8 -*-
from django.core import serializers
from django.core.files.temp import NamedTemporaryFile
from django.core.mail import send_mail
from django.core.management import call_command
from django_apogee.models import InsAdmEtp, Individu, Adresse, AnneeUni, ConfAnneeUni, EtpGererCge, InsAdmEtpInitial

__author__ = 'paul'
from django.core.management.base import BaseCommand
from optparse import make_option
from foad.models import Remontee


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
        etps = list(EtpGererCge.objects.filter(cod_cmp='034').values_list('cod_etp', flat=True))
        annees = list(ConfAnneeUni.objects.filter(synchro=True).values_list('cod_anu', flat=True))
        try:
            # on récupére les personnes du jour (soit la date de création, de modif plus grand que la veille
            # Remontee.objects.filter(is_valide=True).update(is_valide=False)

            # self.copy_oracle_base(Individu.objects.using('oracle').filter(etapes__cod_etp__in=etps,
            #                                                               etapes__cod_anu__in=annees).distinct(), ['default'])
            # self.copy_oracle_base(Individu.objects.using('oracle').filter(
            #     etapes__cod_etp__in=etps,
            #     etapes__cod_anu__in=annees).distinct(), ['default'])
            # ADRESSE annuelle
            # self.copy_oracle_base(Adresse.objects.using('oracle').filter(
            #     cod_ind_ina__etapes__cod_etp__in=etps,
            #     cod_ind_ina__etapes__cod_anu__in=annees,
            #     cod_anu_ina__in=annees).exclude(cod_ind_ina__lib_pr1_ind='DOUBLONS'), ['default'])
            # #ADRESSE fixe
            # self.copy_oracle_base(Adresse.objects.using('oracle').filter(cod_ind__etapes__cod_etp__in=etps,
            #                                                              cod_ind__etapes__cod_anu__in=annees)
            #                                                      .exclude(cod_ind__lib_pr1_ind='DOUBLONS'), ['default'])
            #
            for x in InsAdmEtpInitial.objects.using("oracle").filter(cod_etp__in=etps, cod_anu__in=annees):
                c = x.copy()

                # x.copy(using='duck_bo_etu')
                # if not hasattr(c, 'remontee'):
                #     Remontee.objects.using('default').create(etape=c, is_valide=True)
                # else:
                #     c.remontee.is_valide = True
                #     c.remontee.save(using='default')

            send_mail('synchro oracle', 'la synchro s\'est  bien passée', 'nepasrepondre@iedparis8.net',
                          ['paul.guichon@iedparis8.net'])

        except TypeError, e:
            send_mail('synchro oracle', 'la synchro ne s\'est pas bien passée %s' % e, 'nepasrepondre@iedparis8.net',
                      ['paul.guichon@iedparis8.net'])

    def copy_oracle_base(self, queryset, usings=['default']):
        fichier = NamedTemporaryFile(suffix='.json')
        data = serializers.serialize("json", queryset)
        fichier.writelines(data)
        fichier.flush()
        for using in usings:
            call_command('loaddata', fichier.name.__str__(), database=using)
        fichier.close()
