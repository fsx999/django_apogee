# coding=utf-8
from __future__ import unicode_literals
from django_apogee.models import Individu, InsAdmEtp
import xadmin
from django_apogee.models.models_configuration import ConfAnneeUni


class InsAdmEtpInline(object):

    model = InsAdmEtp
    style = 'table'

    exclude = ['id', 'cod_vrs_vet', 'cod_vrs_vdi', 'cod_dip', 'cod_vrs_vdi'
               'dat_cre_iae', 'dat_cre_iae', 'dat_mod_iae',
               'dat_annul_res_iae']
    readonly_fields = ['cod_etp', 'date', 'cod_anu', 'num_occ_iae', 'cod_cge',
                       'nbr_ins_cyc', 'nbr_ins_etp', 'tem_iae_prm', 'nbr_ins_dip',
                       'eta_iae', 'eta_pmt_iae', 'cod_pru']

    extra = 0

    def has_add_permission(self):
        return False

    def has_delete_permission(self, obj=None):
        return False


class InsAdmEtp(object):
    site_title = "Consultation des dossiers étudiants en Apogée"
    search_fields = ['lib_nom_pat_ind', 'lib_nom_usu_ind', 'lib_pr1_ind', 'cod_etu']
    list_display = ['identite', 'ine', 'cod_etu', 'get_etiquette']
    fields = ['lib_nom_pat_ind', 'lib_nom_usu_ind',
              'lib_pr1_ind', 'lib_pr2_ind', 'lib_pr3_ind', 'cod_etu', 'get_etiquette']
    readonly_fields = ['lib_nom_pat_ind', 'lib_nom_usu_ind',
                       'lib_pr1_ind', 'lib_pr2_ind', 'lib_pr3_ind',
                       'cod_etu', 'get_code_secret', 'get_etiquette']
    style = 'table'
    inlines = [InsAdmEtpInline]
    hidden_menu = True

    def has_add_permission(self):
        return False

    def has_delete_permission(self, obj=None):
        return False

xadmin.site.register(Individu, IndividuAdmin)
xadmin.site.register(ConfAnneeUni)
