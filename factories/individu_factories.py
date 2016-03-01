# coding=utf-8
from __future__ import unicode_literals
from datetime import datetime, date, timedelta
from django.contrib.auth.models import User
import factory
from factory.fuzzy import FuzzyDate, FuzzyInteger, FuzzyChoice, FuzzyText
from django_apogee.factories import PaysFactory, AnneeUniFactory
from django_apogee.models import Individu, Adresse, InsAdmEtp

__author__ = 'juggernut'


class IndividuFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Individu
    cod_ind = factory.Sequence(lambda n: n)
    dat_cre_ind = datetime.now()
    dat_mod_ind = datetime.now()
    date_nai_ind = FuzzyDate(datetime(1980, 1, 1), datetime(1996, 1, 1))
    lib_nom_pat_ind = factory.Sequence(lambda n: 'Guichon%d' % n)
    lib_nom_usu_ind = factory.Sequence(lambda n: 'Polo%d' % n)
    lib_pr1_ind = factory.Sequence(lambda n: 'Paul%d' % n)
    lib_pr2_ind = factory.Sequence(lambda n: 'George%d' % n)
    lib_pr3_ind = factory.Sequence(lambda n: 'Stefan%d' % n)
    cod_etu = FuzzyInteger(11111111, 29999999)
    cod_sex_etu = FuzzyChoice(('M', 'F'))

    @staticmethod
    def create_individu_with_two_adresses():
        """
        Permet de créer un individu avec deux adresses, une fixe et une annuelle
        """
        indiv = IndividuFactory.create()
        AdressFactory.create(cod_ind=None, cod_ind_ina=indiv)
        AdressFactory.create(cod_ind=indiv, cod_ind_ina=None)

        return indiv


class AdressFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Adresse
    cod_adr = factory.Sequence(lambda n: n)
    cod_ind = factory.SubFactory(IndividuFactory)
    cod_anu_ina = '2014'
    cod_ind_ina = factory.SubFactory(IndividuFactory)
    cod_pay = factory.SubFactory(PaysFactory)
    num_tel = FuzzyText(length=15, chars='0123456789')
    num_tel_port = FuzzyText(length=15, chars='0123456789')
    adr_mail = factory.LazyAttribute(lambda obj: 'user{}@example.com'.format(obj.cod_adr))


class InsAdmEtpFactory(factory.DjangoModelFactory):
    FACTORY_FOR = InsAdmEtp
    id = factory.Sequence(lambda n: 'insadm%d' % n)
    cod_anu = factory.SubFactory(AnneeUniFactory)
    cod_ind = factory.SubFactory(IndividuFactory)
    cod_vrs_vet = 'vet'
