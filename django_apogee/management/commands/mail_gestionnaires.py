# -*- coding: utf-8 -*-

from django.core.mail import send_mail
from django.conf import settings
from django.core.management.base import BaseCommand
from django_apogee.models import InsAdmEtpInitial
from duck_utils.utils import get_recipients


class Command(BaseCommand):
    help = 'Send mail to psychology students, informing them who is their gestionnaire'

    message_permanent = """
Bonjour {nom} {prenom},

Votre gestionnaire à l'IED est Madame {gestionnaire} qui est en charge des étudiants dont le nom commence de {first} à {last}.

Elle est à votre disposition pour toutes vos questions administratives liées à votre scolarité à l'IED.

Vous pouvez la contacter par:

Téléphone: {tel}
Mail: {mail}

Cordialement,
Équipe IED

"""
    message_temporaire = """
Bonjour {nom} {prenom},

Le recrutement du gestionnaire en charge de votre suivi administratif est en cours.

Vous serez informé sur la plateforme des coordonnées de la personne en charge des étudiants dont le nom commence de {first} à {last} à partir du mois de décembre.

En attendant, pour toutes questions administratives liées à votre scolarité à l'IED, vous pouvez vous adresser à la coordinatrice de la Licence, Madame {gestionnaire}.

Vous pouvez la contacter par:

Téléphone: {tel}
Mail: {mail}

Cordialement,
Équipe IED
"""

    def __init__(self):
        ###
        # :var gest_per_letter: Dictionary with all the alphabet letters and the corresponding email adress
        # of a gestionnaire
        # :var gestionnaires: Dictionary with gestionnaire emails, corresponding to their data (name, telephone)
        # :var ranges: List of tuples (range of letters, gestionnaire responsible for those letters,
        # gestionnaire is permanent (True) or temporary (False))
        ###
        self.ranges = [
            ('A', 'B', 'siham.teguia@iedparis8.net', True),
            ('C', 'G', 'khadija.ferhan-oyoukou@iedparis8.net', True),
            ('H', 'O', 'siham.teguia@iedparis8.net', False),
            ('P', 'Z', 'jessie.bramble@iedparis8.net', True)
        ]
        self.gestionnaires = {
            'siham.teguia@iedparis8.net': ('Siham LAMOURI-TEGUIA', '01 49 40 72 57',),
            'khadija.ferhan-oyoukou@iedparis8.net': ('Khadija FERHAN-OYOUKOU', '01 49 40 72 35',),
            'jessie.bramble@iedparis8.net': ('Jessie BRAMBLE', '01 49 40 72 14',),
        }
        self.gest_per_letter = {}
        for ab_range in self.ranges:
            a, b, email, is_permanent = ab_range
            for letter in range(ord(a.lower()), ord(b.lower())+1) + range(ord(a.upper()), ord(b.upper())+1):
                self.gest_per_letter[chr(letter)] = ab_range
        super(Command, self).__init__()

    def handle(self, *args, **options):
        # send_mail('Subject', 'Message', 'nepasrepondre@iedparis8.net', ['nikosgpet@gmail.com'], fail_silently=False)
        settings.DEBUG = False
        etudiants = InsAdmEtpInitial.objects.using('oracle').filter(cod_etp__in=['L1NPSY', 'L2NPSY', 'L3NPSY'], cod_anu='2015').order_by('cod_ind__lib_nom_pat_ind')
        before = ''
        for x in etudiants:
            nom_etu = x.cod_ind.lib_nom_pat_ind.title()
            prenom_etu = x.cod_ind.lib_pr1_ind.title()
            mails_etu = get_recipients(x.cod_ind, 2015)
            first_letter, last_letter, mail_gest, is_permanent = self.gest_per_letter[nom_etu[0]]
            nom_gest, tel_gest = self.gestionnaires[mail_gest]
            message = self.message_permanent if is_permanent else self.message_temporaire
            message = message.format(nom=nom_etu, prenom=prenom_etu, gestionnaire=nom_gest, first=first_letter,
                                     last=last_letter, tel=tel_gest, mail=mail_gest)

            if mails_etu[0] != before:
                print nom_etu + ', ' + prenom_etu + ', ' + mail_gest + ', ' + nom_gest + ', ' + first_letter + last_letter + ', ' + str(mails_etu)
                # print message
                # send_mail("[IED] Votre gestionnaire de scolarité", message, 'nepasrepondre@iedparis8.net', list(mails_etu), fail_silently=False)
            before = mails_etu[0]



