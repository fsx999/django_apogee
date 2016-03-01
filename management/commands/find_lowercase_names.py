from django.core.management.base import BaseCommand
from django.db.models import Q
import xlwt
from django_apogee.models import InsAdmEtpInitial
from unidecode import unidecode
from django_apogee.utils import flatten, is_flat


def get_etudiants(etapes):
    etudiants = InsAdmEtpInitial.inscrits.using('oracle').prefetch_related('cod_ind')\
        .filter(cod_etp__in=etapes, cod_anu='2015')\
        .order_by('cod_ind__lib_nom_pat_ind')
    return etudiants


def get_transferts():
    etapes = [
        'L1NDRO', 'L2NDRO', 'L3NDRO',
        'L1NINF', 'L2NINF', 'L3NINF'
    ]

    etudiants = get_etudiants(etapes).order_by('cod_etp', 'cod_ind__lib_nom_pat_ind')\
        .values_list('cod_etp', 'cod_ind__cod_etu', 'cod_ind__lib_nom_pat_ind', 'cod_ind__lib_pr1_ind')
    return etudiants


def get_lowercase_names_list(etapes):

    q = Q(cod_ind__lib_nom_pat_ind__regex=r'[[:lower:]]') |\
        Q(cod_ind__lib_pr1_ind__regex=r'[[:lower:]]') |\
        Q(cod_ind__lib_nom_usu_ind__regex=r'[[:lower:]]') |\
        Q(cod_ind__lib_pr2_ind__regex=r'[[:lower:]]') |\
        Q(cod_ind__lib_pr3_ind__regex=r'[[:lower:]]')

    etudiants = get_etudiants(etapes).filter(q).values_list(
        'cod_ind__cod_etu', 'cod_etp',
        'cod_ind__lib_nom_pat_ind', 'cod_ind__lib_pr1_ind', 'cod_ind__lib_pr2_ind', 'cod_ind__lib_pr3_ind',
        'cod_ind__lib_nom_usu_ind',
    )
    etudiants_list = [['Code etudiant', 'Code Etape', 'Nom', 'Prenom 1', 'Prenom 2', 'Prenom 3', "Nom d'usage", 'Nom', 'Prenom 1', 'Prenom 2', 'Prenom 3', "Nom d'usage"]]

    for etudiant in etudiants:
        flattened = [flatten(x) for x in etudiant]
        line = flattened + list(etudiant[2:])
        etudiants_list.append(line)
    return etudiants_list


def get_dash_in_name_list(etapes):

    q = Q(cod_ind__lib_nom_pat_ind__regex=r'-$') |\
        Q(cod_ind__lib_pr1_ind__regex=r'-$') |\
        Q(cod_ind__lib_nom_usu_ind__regex=r'-$]') |\
        Q(cod_ind__lib_pr2_ind__regex=r'-$') |\
        Q(cod_ind__lib_pr3_ind__regex=r'-$')

    etudiants = get_etudiants(etapes).filter(q).values_list(
        'cod_ind__cod_etu', 'cod_etp',
        'cod_ind__lib_nom_pat_ind', 'cod_ind__lib_pr1_ind', 'cod_ind__lib_pr2_ind', 'cod_ind__lib_pr3_ind',
        'cod_ind__lib_nom_usu_ind',
    )
    etudiants_list = [['Code etudiant', 'Code Etape', 'Nom', 'Prenom 1', 'Prenom 2', 'Prenom 3', "Nom d'usage"]] + list(etudiants)
    return etudiants_list


def get_accent_in_name_list(etapes):

    etudiants = InsAdmEtpInitial.objects.using('oracle').prefetch_related('cod_ind')\
        .filter(cod_anu='2015')\
        .order_by('cod_ind__lib_nom_pat_ind').values_list(
        'cod_ind__cod_etu', 'cod_etp',
        'cod_ind__lib_nom_pat_ind', 'cod_ind__lib_pr1_ind', 'cod_ind__lib_pr2_ind', 'cod_ind__lib_pr3_ind',
        'cod_ind__lib_nom_usu_ind',
    )

    etudiants_list = [['Code etudiant', 'Code Etape', 'Nom', 'Prenom 1', 'Prenom 2', 'Prenom 3', "Nom d'usage"]]

    for etudiant in etudiants:
        all_flat = [is_flat(x) for x in etudiant[2:]]
        if False in all_flat:
            # print all_flat
            etudiants_list.append(etudiant)

    return etudiants_list


def save_worksheet(filename, data):
    '''
    Saves data to an excel named filename
    :param filename: The name of the file to be created
    :param data: data is a list of lists. It's a list of lines, and each line is a list of fields
    :return:
    '''
    wb = xlwt.Workbook()
    ws = wb.add_sheet('sheet 1')

    for i, line in enumerate(data):
        for j, field in enumerate(line):
            ws.write(i, j, field)
    wb.save(filename)


class Command(BaseCommand):

    def handle(self, *args, **options):
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
        etudiants = get_lowercase_names_list(etapes) + get_dash_in_name_list(etapes)

        for etudiant in etudiants:
            print ' '.join(str(x) for x in etudiant)
        print len(etudiants)

        save_worksheet('etudiants_avec_problem.xls', etudiants)
        save_worksheet('etudiants_transfert.xls', get_transferts())


