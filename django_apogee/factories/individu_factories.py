import datetime
from django.contrib.auth.models import User
import factory
from factory.fuzzy import FuzzyDate, FuzzyInteger, FuzzyChoice
from django_apogee.factories import PaysFactory, FamilyStatusFactory, ComBdiFactory, BacOuxEquFactory
from django_apogee.models import Individu, Adresse

__author__ = 'juggernut'


class IndividuFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Individu
    dat_cre_ind = datetime.now()
    dat_mod_ind = datetime.now()
    date_nai_ind = FuzzyDate(datetime.datetime(1980, 1, 1), datetime.datetime(1996, 1, 1))
    lib_nom_pat_ind = factory.Sequence(lambda n: 'Guichon%d' % n)
    lib_nom_usu_ind = factory.Sequence(lambda n: 'Polo%d' % n)
    lib_pr1_ind = factory.Sequence(lambda n: 'Paul%d' % n)
    lib_pr2_ind = factory.Sequence(lambda n: 'George%d' % n)
    lib_pr3_ind = factory.Sequence(lambda n: 'Stefan%d' % n)
    cod_etu = FuzzyInteger(11111111, 29999999)
    cod_sex_etu = FuzzyChoice(('M', 'F'))


class AdressFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Adresse
    com_bdi = factory.SubFactory(ComBdiFactory)
    label_adr_1 = u"7 bis rue des peupliers"
    code_pays = factory.SubFactory(PaysFactory, cod_pay=100, lib_pay=u"FRANCE")
    listed_number = u"0146382652"
    type = u"1"
