# -*- coding: utf-8 -*-
from django.core import serializers
from django.core.files.temp import NamedTemporaryFile
from django.core.mail import send_mail
from django.core.management import call_command


__author__ = 'paul'
from django.core.management.base import BaseCommand
from optparse import make_option

#
# class Command(BaseCommand):
#     def handle(self, *args, **options):
#         #on récupére les personnes du jour (soit la date de création, de modif plus grand que la veille
#         self.copy_oracle_base(Composante.objects.using('oracle').all())
#         #ADRESSE annuelle
#         self.copy_oracle_base(CentreGestion.objects.using('oracle').all())
#
#         self.copy_oracle_base(Etape.objects.using('oracle').all())
#         self.copy_oracle_base(EtpGererCge.objects.using('oracle').all())
#
#     def copy_oracle_base(self, queryset):
#         fichier = NamedTemporaryFile(suffix='.json')
#         data = serializers.serialize("json", queryset)
#         fichier.writelines(data)
#         fichier.flush()
#
#         call_command('loaddata', fichier.name.__str__())
#         fichier.close()
