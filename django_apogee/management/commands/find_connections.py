from difflib import SequenceMatcher
from datetime import datetime
from pprint import pprint
import os
from django.core.management.base import BaseCommand
from django.db.models import Count, Q
from duck_inscription.models import Individu
import pickle
from django_apogee.models import Individu as IndividuA, InsAdmEtp, InsAdmEtpInitial
from django_apogee.utils import flatten


def get_etudiants(pickle_file):
    '''
    Executes the query to get students, and pickles the result in picklefile
    '''
    etudiants = InsAdmEtpInitial.inscrits.using('oracle').prefetch_related('cod_ind').filter(cod_anu='2015').values(
        'cod_etp',
        'cod_ind__cod_etu', 'cod_ind__cod_nne_ind', 'cod_ind__cod_cle_nne_ind',
        'cod_ind__lib_nom_pat_ind', 'cod_ind__lib_nom_usu_ind',
        'cod_ind__lib_pr1_ind', 'cod_ind__lib_pr2_ind', 'cod_ind__lib_pr3_ind',
        'cod_ind__num_brs_etu', 'cod_ind__cod_nni_etu', 'cod_ind__cod_cle_nni_etu',
        'cod_ind__cod_sex_etu', 'cod_ind__date_nai_ind',
        'cod_ind__cod_ind_opi',
    )
    print "Create Pickle"
    pickle.dump(etudiants, open(pickle_file, "wb"))
    return etudiants


def get_ine(dictionary):
    ine = dictionary['cod_ind__cod_nne_ind'] + dictionary['cod_ind__cod_cle_nne_ind']
    return str(ine).upper()


def is_same(string1, string2):
    return flatten(string1) == flatten(string2)


def is_same_person(individu_tuple, etudiant):
    individu = individu_tuple[1]
    i_nom = flatten(individu.last_name)
    e_nom = flatten(etudiant['cod_ind__lib_nom_pat_ind'])
    i_prenom = flatten(individu.first_name1)
    e_prenom = flatten(etudiant['cod_ind__lib_pr1_ind'])
    i_date = individu.birthday
    e_date = datetime.strptime(str(etudiant['cod_ind__date_nai_ind']), '%Y-%m-%d %H:%M:%S').date()
    if i_date == e_date:
        if i_nom == e_nom and i_prenom == e_prenom:
            return True
        else:
            ratio = round(SequenceMatcher(None, i_nom + i_prenom, e_nom + e_prenom).ratio(), 2)
            if ratio < 0.7:
                pass
            # print '{}, {}, {}, {}, {}, {}, {}'.format(ratio, etudiant['cod_etp'], etudiant['cod_ind__cod_etu'], i_nom, i_prenom, e_nom, e_prenom)
            return False
    else:
        print '{}, {}, '.format(i_date, e_date) + '{}, {}, {}, {}, {}, {}'.format(etudiant['cod_etp'], etudiant['cod_ind__cod_etu'], i_nom, i_prenom, e_nom, e_prenom)
        return False


class Command(BaseCommand):

    def handle(self, *args, **options):
        tested_by_hand = {
            '15609653': 7721112, #MEZIOUT BRAHIMI MALIKA, nom prenom inversees
            '14511097': 7718634, #PEDRONO ANNE-CLAIRE, same ine by mistake
            '11299481': 7722497, #PAPAGEORGIOU STYLIANI MARIA, wrong name, and surname by mistake
        }

        use_pickle = True
        pickle_file = 'etudiants.pickle'

        individus = Individu.objects.all().filter(wishes__valide=True).prefetch_related('wishes__paiementallmodel__moyen_paiement', 'wishes__etape')

        print individus.filter(code_opi=7718634)
        if use_pickle and os.path.isfile(pickle_file):
            print "Use Pickle"
            etudiants = pickle.load(open(pickle_file, "rb"))
        else:
            etudiants = get_etudiants(pickle_file)

        print 'Individus: {}'.format(individus.count())
        print 'Etudiants: {}'.format(len(etudiants))

        individus_etu = {str(x.student_code): x for x in individus}
        print 'finished student code dic'
        individus_ine = {str(x.ine).upper(): x for x in individus}
        print 'finished ine dic'
        individus_opi = {x.code_opi: x for x in individus}
        print 'finished opi dic'
        a = individus_opi[7733565]

        # o = individus_etu['12318389'].wishes.all()[0].etape
        # pprint(vars(o))
        # return

        individus_etudiants = {}
        etudiants_not_found = {}
        nombre_not_found = 0
        nombre_false_positive = 0
        for i, etudiant in enumerate(etudiants):
            ine = get_ine(etudiant)
            cod_etu = str(etudiant['cod_ind__cod_etu'])
            cod_opi = etudiant['cod_ind__cod_ind_opi']
            e_nom = etudiant['cod_ind__lib_nom_pat_ind']
            e_prenom = etudiant['cod_ind__lib_pr1_ind']

            # if cod_etu in individus_etudiants:
            #     print 'This is weird'
            #     print '{} {} {}'.format(cod_etu, e_nom, e_prenom)
            #     print individus_etudiants[cod_etu]

            if cod_etu in tested_by_hand:
                individus_etudiants[cod_etu] = ('manual', individus_opi[tested_by_hand[cod_etu]])
            elif ine and ine in individus_ine:
                individus_etudiants[cod_etu] = ('ine', individus_ine[ine])
            elif cod_etu and cod_etu in individus_etu:
                individus_etudiants[cod_etu] = ('etu', individus_etu[cod_etu])
            elif cod_etu and cod_opi in individus_opi:
                individus_etudiants[cod_etu] = ('opi', individus_opi[cod_opi])
            else:
                e_date = datetime.strptime(str(etudiant['cod_ind__date_nai_ind']), '%Y-%m-%d %H:%M:%S').date()
                i_found = individus.filter(Q(first_name1__icontains=e_prenom) | Q(last_name__icontains=e_nom))\
                    .filter(birthday=e_date)
                if i_found.exists():
                    individus_etudiants[cod_etu] = ('name', individus_opi[i_found[0].code_opi])
                else:
                    print 'Individu not found'
                    nombre_not_found += 1
                    etudiants_not_found[cod_etu] = etudiant
                    print '{} {} {}'.format(cod_etu, e_nom, e_prenom)

        for i, etudiant in enumerate(etudiants):
            cod_etu = str(etudiant['cod_ind__cod_etu'])
            if cod_etu in individus_etudiants:
                if not is_same_person(individus_etudiants[cod_etu], etudiant):
                    nombre_false_positive += 1

            # if nombre_not_found > 10:
            #     break

        # print nombre_not_found
        print 'Etudiants found {}'.format(len(individus_etudiants))
        print 'False Positive {}'.format(nombre_false_positive)
        print 'Etudiants not found {}'.format(nombre_not_found)



        individus_etudiants_same_wish = {}
        individus_etudiants_similar_wish = {}
        for i, etudiant in enumerate(etudiants):
            cod_etu = str(etudiant['cod_ind__cod_etu'])
            e_cod_etp = etudiant['cod_etp']
            if cod_etu in individus_etudiants:
                ind = individus_etudiants[cod_etu][1]
                for w in ind.wishes.all():
                    i_cod_etp = w.etape.cod_etp
                    if i_cod_etp == e_cod_etp:
                        individus_etudiants_same_wish[cod_etu] = (i_cod_etp, e_cod_etp)
                        individus_etudiants_similar_wish.pop(cod_etu, None)
                        break
                    elif str(i_cod_etp)[2:] == str(e_cod_etp)[2:]:
                        individus_etudiants_similar_wish[cod_etu] = (i_cod_etp, e_cod_etp)
                if cod_etu not in individus_etudiants_same_wish and cod_etu not in individus_etudiants_similar_wish:
                    print '{} {} {}'.format(cod_etu, w.etape.cod_etp, e_cod_etp)

        print 'Same wishes found {}'.format(len(individus_etudiants_same_wish))
        print 'Similar wishes found {}'.format(len(individus_etudiants_similar_wish))

        for i, etudiant in enumerate(etudiants):
            cod_etu = str(etudiant['cod_ind__cod_etu'])
            if cod_etu in individus_etudiants_same_wish and cod_etu in individus_etudiants_similar_wish:
                print '{}'.format(cod_etu)
        # individus_cb = {}
        # for cod_etu, i in individus_etudiants.items():
        #     wishes = i[1].wishes.all()
        #     for w in wishes:
        #         if w.is_ok:
        #             try:
        #                 p = w.paiementallmodel
        #                 moyen = p.moyen_paiement
        #                 if moyen.type == 'CB':
        #                     individus_cb[cod_etu] = i[0]
        #                     if not p.paiement_request.payment_successful:
        #                         print i
        #
        #             except Exception, e:
        #                 continue
        #
        # print 'Carte Bancaire: {}'.format(len(individus_cb))
