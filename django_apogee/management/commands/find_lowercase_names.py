from django.core.management.base import BaseCommand
from django_apogee.models import InsAdmEtpInitial


class Command(BaseCommand):

    def t(self, nom):
        return nom.upper() != nom

    def handle(self, *args, **options):
        etapes = [['L1NPSY', 'L2NPSY', 'L3NPSY'],
                  ['L1NDRO', 'L2NDRO', 'L3NDRO'],
                  ['M1NPCL', 'M2NPCL'],
                  ['M1NPEA', 'M2NPEA'],
                  ['M1NPST', 'M2NPST'],
                  ['DSNPCA'],
                  ['L3NEDU', 'M1NEFI', 'M1NEFI'],
                  ['L1NINF', 'L2NINF', 'L3NINF']]
        for etape in etapes:
            print ''
            print etape
            etudiants = InsAdmEtpInitial.objects.using('oracle').filter(cod_etp__in=etape).filter(cod_anu='2015').order_by('cod_ind__lib_nom_pat_ind')
            before = ''
            for x in etudiants:
                nom = x.cod_ind.lib_nom_pat_ind
                nom_usu = x.cod_ind.lib_nom_usu_ind
                prn1 = x.cod_ind.lib_pr1_ind
                prn2 = x.cod_ind.lib_pr2_ind
                prn3 = x.cod_ind.lib_pr3_ind
                cod_etu = x.cod_ind.cod_etu

                if cod_etu != before and (self.t(nom) or self.t(nom_usu) or self.t(prn1) or self.t(prn2) or self.t(prn3)):
                    print str(cod_etu) + ' ' + nom + ' ' + nom_usu + ' ' + prn1 + ' ' + prn2 + ' ' + prn3
                before = cod_etu
