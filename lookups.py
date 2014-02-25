# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.db.models.query_utils import Q

__author__ = 'paul'

from ajax_select import LookupChannel
from apogee.models import ApogeeComBdi, ApogeeEtablissement


class ApogeeComBdiLookup(LookupChannel):
    model = ApogeeComBdi
    min_length = 5
    search_field = 'cod_bdi'

    def check_auth(self, request):
        if request.user.is_anonymous():
            raise PermissionDenied

    def get_query(self, q, request):
        return ApogeeComBdi.objects.filter(Q(cod_bdi__istartswith=q)).order_by('lib_ach')

    def get_objects(self, ids):
        ids = [(10 - len(str(x))) * "0" + str(x) for x in ids]
        return ApogeeComBdi.objects.filter(pk__in=ids)


class ApogeeEtablissementLookup(LookupChannel):
    model = ApogeeEtablissement
    min_length = 2
    search_field = "cod_dep__cod_dep"

    def check_auth(self, request):
        if request.user.is_anonymous():
            raise PermissionDenied

    def get_query(self, q, request):
        type_eta = request.GET.get('type', '15')
        if type_eta == u'15' or type_eta == u'10':
            return ApogeeEtablissement.objects.filter(cod_tpe__cod_tpe__icontains=type_eta).exclude(
                lib_off_etb='INCONNU')
        return ApogeeEtablissement.objects.filter(cod_dep__cod_dep__icontains=q,
                                                  cod_tpe__cod_tpe__icontains=type_eta).exclude(lib_off_etb='INCONNU')


class UserLookup(LookupChannel):
    model = User
    search_field = "username"

    def check_auth(self, request):
        if not request.user.is_staff:
            raise PermissionDenied

    def get_query(self, q, request):
        return User.objects.filter(Q(username__istartswith=q))

    def get_objects(self, ids):
        return User.objects.filter(pk__in=ids)
