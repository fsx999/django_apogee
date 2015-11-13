from django.core.mail import send_mail
from django.core.management.base import BaseCommand
from django_apogee.models import InsAdmEtpInitial


class Command(BaseCommand):
    help = 'Send mail to psychology students, informing them who is their gestionnaire'

    ranges = [
            ('siham.teguia@iedparis8.net', 'a', 'b'),
            ('khadija.ferhan-oyoukou@iedparis8.net', 'c', 'g'),
            ('siham.teguia@iedparis8.net', 'h', 'o'),
            ('jessie.bramble@iedparis8.net', 'p', 'z')
    ]

    mail_per_letter = {}

    def __init__(self):
        for email, start, end in self.ranges:
            for letter in range(ord(start.lower()), ord(end.lower())+1) + range(ord(start.upper()), ord(end.upper())+1):
                self.mail_per_letter[chr(letter)] = email
        super(Command, self).__init__()

    def handle(self, *args, **options):
        # send_mail('Subject', 'Message', 'nepasrepondre@iedparis8.net', ['nikosgpet@gmail.com'], fail_silently=False)

        result = InsAdmEtpInitial.objects.using('oracle').filter(cod_etp__in=['L1NPSY']).filter(cod_anu='2015').order_by('cod_ind__lib_nom_pat_ind')
        for x in result:
            nom = x.cod_ind.lib_nom_pat_ind
            gestionnaire = self.mail_per_letter[nom[0]]
            email = x.cod_ind.get_email(2015)
            print nom + ' ' + email + ' ' + gestionnaire + ' '

            message1 = """
Bonjour,

Pour toutes questions administratives liées à votre scolarité à l'IED,
votre gestionnaire est Madame X.
Vous pouvez la contacter au 01.... ou par mail à l'adresse suivante : ....

Bonne année à l'IED. "

"""

            message2 = """
Bonjour,

Le recrutement du gestionnaire en charge de votre suivi administratif
est en cours.

Vous serez informé sur la plateforme des coordonnées de la personne à
contacter à partir du mois de décembre.

En attendant, pour toutes questions administratives liées à votre
scolarité à l'IED, vous pouvez vous adresser à la coordinatrice de la
Licence, Madame Siham LAMOURI-TEGUIA.

Vous pouvez la contacter au 01.... ou par mail à l'adresse suivante : ....

Bonne année à l'IED.
            """


            # send_mail('Votre gestionnaire IED', 'Message', 'nepasrepondre@iedparis8.net', [email], fail_silently=False)

