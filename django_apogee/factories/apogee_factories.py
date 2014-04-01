# coding=utf-8
from __future__ import unicode_literals
from datetime import datetime
import factory
from django_apogee.models import Pays, Departement, SitFam, SitMil, TypHandicap, ComBdi, TypHebergement, BacOuxEqu, \
    SituationSise, Individu, MentionBac, Etablissement

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


class SitFamFactory(factory.DjangoModelFactory):
    FACTORY_FOR = SitFam
    cod_fam = factory.Iterator(['C', 'F', 'X'], cycle=False)
    lib_fam = 'Tototottrofdsq'
    lic_fam = 'dadad'


class SitMilFactory(factory.DjangoModelFactory):
    FACTORY_FOR = SitMil
    cod_sim = factory.Iterator(['1'], cycle=False)
    lib_sim = "exempté"
    lic_sim = 'exce'


class TypHandicapFactory(factory.DjangoModelFactory):
    FACTORY_FOR = TypHandicap
    cod_thp = factory.Iterator(['tr', 'ba', 'ee', 'ff'], cycle=False)
    lib_thp = 'Test Lib Handicap'
    lic_thp = 'tst lic hand'


class TypeHebergementFactory(factory.DjangoModelFactory):
    FACTORY_FOR = TypHebergement
    cod_thb = factory.Iterator(['h', 's', 't'], cycle=False)
    lib_thb = 'example libéle hebergement ....'


class SituationSiseFactory(factory.DjangoModelFactory):
    FACTORY_FOR = SituationSise
    cod_sis = factory.Iterator(['a', 'b', 'c'], cycle=False)
    lib_sis = 'lib sise test'


class BacOuxEquFactory(factory.DjangoModelFactory):
    FACTORY_FOR = BacOuxEqu
    cod_bac = factory.Iterator(['S', 'PRO', 'ST'], cycle=False)
    cod_sis_bac = 'ASDF'
    lib_bac = "Bac test Scientifique"
    lib_bac = "Bac"
    daa_deb_vld_bac = factory.Iterator([datetime.date(2003, 1, 1),
                                       datetime.date(1998, 1, 1),
                                       datetime.date(1991, 1, 1)],
                                       cycle=False)
    daa_fin_vld_bac = factory.Iterator([datetime.date(2010, 1, 1),
                                       datetime.now()+datetime.timedelta(years=2),
                                       datetime.now() - datetime.timedelta(hours=24)],
                                       cycle=False)
    cod_sis = factory.SubFactory(SituationSiseFactory)


class MentionBacFactory(factory.DjangoModelFactory):
    FACTORY_FOR = MentionBac
    cod_mnb = factory.Iterator(['BI', 'TB', 'EX'],
                               cycle=False)
    lib_mnb = 'Truc Test MNB'
    lic_mnb = 'trc tsts mnb'


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


class TypEtbFactory(factory.DjangoModelFactory):
    cod_tpe = factory.Iterator(['DO', 'TO', 'LY', 'UN'],
                               cycle=False)
    lib_tpe = 'type etablisement example1'
    lic_tpe = 'tp etablismnt exmpl'


class EtablissementFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Etablissement
    cod_etb = factory.Iterator(['12345678', '21314235'], cycle=False)
    cod_tpe = factory.SubFactory(TypEtbFactory)
    cod_dep = factory.SubFactory(DepartementFactory)


class DepartementFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Departement
#sophie : 235663 5224
def sophie_individu(save=False):
    individu = IndividuFactory.cree(save,
                                    COD_IND=235663,
                                    COD_ETU='235663',
                                    LIB_NOM_PAT_IND="BRION",
                                    LIB_PR1_IND='SOPHIE',
                                    DATE_NAI_IND=datetime.date(1986, 10, 8))
    return individu
