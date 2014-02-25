# coding=utf-8


__author__ = 'paul'
from apogee.models import (Pays, Departement, FamilyStatus, SituationMilitaire, TypeHandicap,
                           TypeHebergement, BacOuxEqui, Individu, ComBdi)
import factory
import datetime

DEPARTEMENT = [
    ['075', 'PARIS'],
    ['091', 'ESSONNE'],
    ['973', 'GUYANNE']
]

PAYS = [
    ['100', 'FRANCE'],
    ['405', 'MEXIQUE'],
    ['501', 'AUSTRALIE']
]


class PaysFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Pays
    lib_pay = factory.LazyAttributeSequence(lambda a, n: '{0}'.format(PAYS[int(n) % 3][1]))
    cod_pay = factory.LazyAttributeSequence(lambda a, n: '{0}'.format(PAYS[int(n) % 3][0]))


class DepartementFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Departement
    cod_dep = factory.LazyAttributeSequence(lambda a, n: '{0}'.format(DEPARTEMENT[int(n) % 3][0]))
    lib_dep = factory.LazyAttributeSequence(lambda a, n: '{0}'.format(DEPARTEMENT[int(n) % 3][1]))
    cod_acd = "1"
    lic_dep = "truc"
    tem_en_sve_dep = 'O'


class FamilyStatusFactory(factory.DjangoModelFactory):
    FACTORY_FOR = FamilyStatus
    title = "Celibataire"


class SituationMilitaireFactory(factory.DjangoModelFactory):
    FACTORY_FOR = SituationMilitaire
    cod_sim = 1
    lib_sim = u"exempté"


class HandicapFactory(factory.DjangoModelFactory):
    FACTORY_FOR = TypeHandicap


class TypeHebergementFactory(factory.DjangoModelFactory):
    FACTORY_FOR = TypeHebergement
    cod_thb = factory.Sequence(lambda n: n)


class BacOuxEquFactory(factory.DjangoModelFactory):
    FACTORY_FOR = BacOuxEqui
    cod_bac = 'S'
    lib_bac = "Scientifique"


class ComBdiFactory(factory.DjangoModelFactory):
    FACTORY_FOR = ComBdi
    id = factory.lazy_attribute(lambda obj: '%s' % (obj.cod_bdi+obj.cod_com))
    cod_bdi = 92130
    cod_com = 92130
    lib_ach = "Issy les moulineaux"


class IndividuFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Individu
    COD_FAM = 1
    DAT_CRE_IND = datetime.date.today()
    DAT_MOD_IND = datetime.date.today()

    @classmethod
    def cree(cls, save=False, **kwargs):
        from inscription.models import AnneeEnCour
        AnneeEnCour.objects.get_or_create(annee=2013, ouverte_inscription='O', annee_en_cours=True)
        attrs = cls.attributes(create=save, extra=kwargs)
        return cls._generate(save, attrs)


#sophie : 235663 5224
def sophie_individu(save=False):
    individu = IndividuFactory.cree(save,
                                    COD_IND=235663,
                                    COD_ETU='235663',
                                    LIB_NOM_PAT_IND="BRION",
                                    LIB_PR1_IND='SOPHIE',
                                    DATE_NAI_IND=datetime.date(1986, 10, 8))
    return individu
