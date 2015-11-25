from django.core.management.base import BaseCommand
from django.db.models import Q
from django_apogee.models import InsAdmEtpInitial


def get_lowercase_names():
    etapes = [
        'L1NPSY', 'L2NPSY', 'L3NPSY',
        'L1NDRO', 'L2NDRO', 'L3NDRO',
        'M1NPCL', 'M2NPCL',
        'M1NPEA', 'M2NPEA',
        'M1NPST', 'M2NPST',
        'DSNPCA',
        'L3NEDU', 'M1NEFI', 'M1NEFI',
        'L1NINF', 'L2NINF', 'L3NINF'
    ]

    q = Q(cod_ind__lib_nom_pat_ind__regex=r'[[:lower:]]') |\
        Q(cod_ind__lib_nom_usu_ind__regex=r'[[:lower:]]') |\
        Q(cod_ind__lib_pr1_ind__regex=r'[[:lower:]]') |\
        Q(cod_ind__lib_pr2_ind__regex=r'[[:lower:]]') |\
        Q(cod_ind__lib_pr3_ind__regex=r'[[:lower:]]')

    etudiants = InsAdmEtpInitial.objects.using('oracle').filter(cod_etp__in=etapes, cod_anu='2015')\
        .filter(q)\
        .order_by('cod_etp', 'cod_ind__lib_nom_pat_ind')
    return etudiants


def get_lowercase_names_list():
    etudiants = get_lowercase_names()
    etudiants_list = [['Code etudiant', 'Nom', "Nom d'usage", 'Prenom 1', 'Prenom 2', 'Prenom 3']]
    for x in etudiants:
        nom = x.cod_ind.lib_nom_pat_ind
        nom_usu = x.cod_ind.lib_nom_usu_ind
        prn1 = x.cod_ind.lib_pr1_ind
        prn2 = x.cod_ind.lib_pr2_ind
        prn3 = x.cod_ind.lib_pr3_ind
        cod_etu = x.cod_ind.cod_etu
        etudiants_list += [cod_etu, nom, nom_usu, prn1, prn2, prn3]
    return etudiants_list


class Command(BaseCommand):

    def handle(self, *args, **options):
        etudiants = get_lowercase_names()
        for x in etudiants:
            print x



