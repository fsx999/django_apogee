# coding=utf-8
from __future__ import unicode_literals
from django_apogee.models import Individu
import xadmin


class IndividuAdmin(object):
    search_fields = ['lib_nom_pat_ind', 'lib_nom_usu_ind', 'lib_pr1_ind', 'cod_etu']
    list_display = ['lib_nom_pat_ind', 'lib_nom_usu_ind', 'lib_pr1_ind', 'cod_etu']
xadmin.site.register(Individu, IndividuAdmin)
