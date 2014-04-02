from __future__ import unicode_literals
from factory.fuzzy import FuzzyInteger
from django_apogee.models import IndOpi, AdresseOpi

__author__ = 'juggernut'
import factory
# a faire :)


class IndOpiFactory(factory.DjangoModelFactory):
    FACTORY_FOR = IndOpi
    cod_ind_opi = factory.Sequence(lambda n: n)
    cod_ind = factory.Sequence(lambda n: n)
    lib_nom_pat_ind_opi = factory.Sequence(lambda n: "stefan%d" % n)
    lib_pr1_ind_opi = factory.Sequence(lambda n: "George%d" % n)
    cod_opi_int_epo = FuzzyInteger(11111111, 29999999)


class AdresseOpi(factory.DjangoModelFactory):
    FACTORY_FOR = AdresseOpi
    cod_ind_opi = factory.SubFactory(IndOpiFactory)
