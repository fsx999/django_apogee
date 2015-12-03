# coding=utf-8
from __future__ import unicode_literals

import simpleldap

from django_apogee.models import Individu, InsAdmEtp, InsAdmEtpInitial
import xadmin
from django_apogee.models.models_configuration import ConfAnneeUni
from foad.moodle_models import MdlUser, MdlCohortMembers


class InsAdmEtpInline(object):

    model = InsAdmEtpInitial
    style = 'table'

    exclude = ['pk', 'cod_vrs_vet', 'cod_vrs_vdi', 'cod_dip', 'cod_vrs_vdi'
               'dat_cre_iae', 'dat_mod_iae',
               'dat_annul_res_iae']
    readonly_fields = ['cod_etp', 'date', 'cod_anu', 'num_occ_iae', 'cod_cge',
                       'nbr_ins_cyc', 'nbr_ins_etp', 'tem_iae_prm', 'nbr_ins_dip',
                       'eta_iae', 'eta_pmt_iae', 'cod_pru','dat_cre_iae', 'dat_mod_iae',
               'dat_annul_res_iae']

    extra = 0

    def has_add_permission(self):
        return False

    def has_delete_permission(self, obj=None):
        return False

    def queryset(self):
        """
        Returns a QuerySet of all model instances that can be edited by the
        admin site. This is used by changelist_view.
        """
        return InsAdmEtpInitial.objects.using('oracle').all()


class IndividuAdmin(object):
    site_title = "Consultation des dossiers étudiants en Apogée"
    search_fields = ['lib_nom_pat_ind', 'lib_nom_usu_ind', 'lib_pr1_ind', 'cod_etu']
    list_display = ['identite', 'ine', 'cod_etu', 'get_code_secret', 'get_etiquette']
    fields = ['lib_nom_pat_ind', 'lib_nom_usu_ind',
              'lib_pr1_ind', 'lib_pr2_ind', 'lib_pr3_ind', 'cod_etu', 'get_etiquette', 'get_ldap_student',
              'get_cohorts_moodle']
    readonly_fields = ['lib_nom_pat_ind', 'lib_nom_usu_ind',
                       'lib_pr1_ind', 'lib_pr2_ind', 'lib_pr3_ind',
                       'cod_etu', 'get_code_secret', 'get_etiquette', 'get_ldap_student', 'get_cohorts_moodle']
    style = 'table'
    inlines = [InsAdmEtpInline]
    hidden_menu = True

    def get_ldap_student(self, obj):
        if getattr(self, '_user_ldap', None):
            return getattr(self, '_user_ldap', 'None')

        filtre = '(&(uid=*)(up8Diplome=*)(supannetuid={}))'.format(obj.cod_etu)

        attr = [
            'sn',
            'givenName',
            'supannEtuId',
            'uid'
        ]
        search = {'base_dn': 'dc=univ-paris8,dc=fr', 'list': 'sn,uid,givenName,supannEtuId'}
        conn = simpleldap.Connection('ldap.etud.univ-paris8.fr',
                                     dn='cn=admin,dc=univ-paris8,dc=fr',
                                     search_defaults=search,
                                     password='p8SARiH3')
        # results = conn.search(filtre,
        #                       attrs=attr
                              # )
        try:
            results = conn.get('supannetuid={}'.format(obj.cod_etu))
            self._user_ldap = str(results['uid'][0])
            return self._user_ldap
        except simpleldap.ObjectNotFound:
            return None

        # self.ldap_user = {x['supannEtuId'][0]: x['uid'][0] for x in results}

    def get_cohorts_moodle(self, obj):
        user = self.get_ldap_student(obj)
        try:
            user = MdlUser.objects.using('moodle').get(username=user)
            return " ".join([m.cohortid.idnumber for m in MdlCohortMembers.objects.using('moodle').filter(userid=user.id)])

        except MdlUser.DoesNotExist:
            return "rien"

    def has_add_permission(self):
        return False

    def has_delete_permission(self, obj=None):
        return False

    def queryset(self):
        """
        Returns a QuerySet of all model instances that can be edited by the
        admin site. This is used by changelist_view.
        """
        return Individu.objects.using('oracle').all()

xadmin.site.register(Individu, IndividuAdmin)
xadmin.site.register(ConfAnneeUni)
