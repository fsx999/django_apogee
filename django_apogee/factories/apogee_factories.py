# coding=utf-8
from __future__ import unicode_literals
from datetime import datetime, date, timedelta
import factory
from django_apogee.models import Pays, Departement, SitFam, SitMil, TypHandicap, ComBdi, TypHebergement, BacOuxEqu, \
    SituationSise, Individu, MentionBac, Etablissement, CatSocPfl, QuotiteTra, DomaineActPfl, RegimeParent, MtfNonAflSso, \
    SitSociale, Bourse, Composante, CentreGestion, Etape, EtpGererCge, Elp, ElpLibelle, Diplome, CmpHabiliterVdi, \
    VersionDiplome, VersionEtape, VdiFractionnerVet, AnneeUni, TypEtb, TypeDiplomeExt

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


class AnneeUniFactory(factory.Factory):
    FACTORY_FOR = AnneeUni
    cod_anu = factory.Iterator(['2013', '2014'], cycle=False)


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
    cod_sim = factory.Iterator(['1', '2'], cycle=False)
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
    daa_deb_vld_bac = factory.Iterator([date(2003, 1, 1),
                                       date(1998, 1, 1),
                                       date(1991, 1, 1)],
                                       cycle=False)
    daa_fin_vld_bac = factory.Iterator([date(2010, 1, 1),
                                       datetime.now() + timedelta(hours=24),
                                       datetime.now() - timedelta(hours=24)],
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


class TypEtbFactory(factory.DjangoModelFactory):
    FACTORY_FOR = TypEtb
    cod_tpe = factory.Iterator(['DO', 'TO', 'LY', 'UN'],
                               cycle=False)
    lib_tpe = 'type etablisement example1'
    lic_tpe = 'tp etablismnt exmpl'


class EtablissementFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Etablissement
    cod_etb = factory.Iterator(['12345678', '21314235'], cycle=False)
    cod_tpe = factory.SubFactory(TypEtbFactory)
    cod_dep = factory.SubFactory(DepartementFactory)
    lib_etb = "Un Etablisement quelque part example"
    cod_pos_adr_etb = "75022"
    cod_aff_dep_etb = "101"
    cod_aff_etb = "110"
    lib_off_etb = "Libele Officiel Example"
    lib_art_off_etb = "ASDF"
    cod_pay_adr_etb = factory.SubFactory(PaysFactory)


class DepartementFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Departement
    cod_dep = factory.Iterator(['75022', '75023', '75024'],
                               cycle=False)
    cod_acd = 3
    lib_dep = "Le departement qui n'existe pas"
    lic_dep = "Le dep imaginaire"
    tem_en_sve_dep = "C"


class CatSocPflFactory(factory.DjangoModelFactory):
    FACTORY_FOR = CatSocPfl
    cod_pcs = factory.Iterator(['IG', 'CA', 'DR'], cycle=False)
    lib_pcs = 'Example libelle'
    lib_web_pcs = 'Example libelle web'


class QuotiteTraFactory(factory.DjangoModelFactory):
    FACTORY_FOR = QuotiteTra
    cod_qtr = factory.Iterator(['1', '2', '3'], cycle=False)
    lib_qtr = 'adadssqddqqd'
    lic_qtr = 'adadssqddqqd'
    lim1_qtr = 'asd'
    lib_web_qtr = 'weeeb'


class DomaineActPflFactory(factory.DjangoModelFactory):
    FACTORY_FOR = DomaineActPfl
    cod_dap = factory.Iterator(['SA', 'AS', 'AD'], cycle=False)
    lib_web_dap = 'KDaqddcscgb'


class SituationSiseFactory(factory.DjangoModelFactory):
    FACTORY_FOR = SituationSise
    cod_sis = factory.Iterator(['I', 'A', 'B'], cycle=False)
    lib_sis = "An example de sise"


class TypeDiplomeExtFactory(factory.DjangoModelFactory):
    FACTORY_FOR = TypeDiplomeExt
    cod_tde = factory.Iterator(['SA', 'AS', 'AD'], cycle=False)
    lib_web_tde = "An example addq"
    lib_tde = "qsdqqs"


class RegimeParentFactory(factory.DjangoModelFactory):
    FACTORY_FOR = RegimeParent
    cod_rgp = factory.Iterator(['SA', 'AS', 'AD'], cycle=False)
    lib_rgp = "Example rgsp"
    ordre_tri_rgp = "aa"


class MtfNonAflSsoFactory(factory.DjangoModelFactory):
    FACTORY_FOR = MtfNonAflSso
    cod_mns = factory.Iterator(['a', 'b', 'c'], cycle=False)
    lib_mns = 'Example adasd'
    lic_mns = 'exampl'


class SitSocialeFactory(factory.DjangoModelFactory):
    FACTORY_FOR = SitSociale
    cod_soc = factory.Iterator(['aa', 'ab', 'ac'], cycle=False)
    lib_soc = 'Example situation'
    lic_soc = 'exmpl sitsoc'


class BourseFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Bourse
    cod_brs = factory.Iterator(['aa', 'ab', 'ac'], cycle=False)
    lim1_brs = "Bourse Trucsas"
    cod_soc = factory.SubFactory(SitSocialeFactory)


class ComposanteFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Composante
    cod_cmp = factory.Iterator(['cge', 'abc', 'cba'], cycle=False)
    cod_tpc = 'trc'
    lib_cmp = 'Ied trucs bla'


class CentreGestionFactory(factory.DjangoModelFactory):
    FACTORY_FOR = CentreGestion
    cod_cge = factory.Iterator(['ers', 'sss', 'eee'], cycle=False)
    lib_cge = 'Estoy bueno'


class EtapeFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Etape
    cod_etp = factory.Iterator(['ersess', 'ssseer', 'eeerrr'], cycle=False)
    cod_cyc = 'a'
    cod_cur = 'u'
    lib_etp = 'Libellé trucs'


class EtpGererCgeFactory(factory.DjangoModelFactory):
    FACTORY_FOR = EtpGererCge
    cod_etp = factory.SubFactory(EtapeFactory)
    cod_cge = factory.SubFactory(CentreGestionFactory)
    cod_cmp = factory.SubFactory(ComposanteFactory)


class ElpFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Elp
    cod_elp = factory.Iterator(['ersess', 'ssseer', 'eeerrr'], cycle=False)
    cod_cmp = factory.SubFactory(ComposanteFactory)
    lib_elp = "Libellé d'un cours"
    eta_elp = 'a'


class ElpLibelleFactory(factory.DjangoModelFactory):
    FACTORY_FOR = ElpLibelle
    id = factory.Iterator(['ersess', 'ssseer', 'eeerrr'], cycle=False)
    cod_elp = factory.SubFactory(ElpFactory)
    cod_lng = 'abnc'
    lib_elp_lng = 'Salut les gars coucu'


class DiplomeFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Diplome
    cod_dip = factory.Iterator(['ersess', 'ssseer', 'eeerrr'], cycle=False)
    lib_dip = 'Example lib dipl'


class CmpHabiliterVdiFactory(factory.DjangoModelFactory):
    FACTORY_FOR = CmpHabiliterVdi
    id = factory.Iterator(['ersess', 'ssseer', 'eeerrr'], cycle=False)
    cod_cmp = factory.SubFactory(ComposanteFactory)
    cod_dip = factory.SubFactory(DiplomeFactory)
    cod_vrs_vdi = '123'
    tem_en_sve_cvd = 'O'


class VersionDiplomeFactory(factory.DjangoModelFactory):
    FACTORY_FOR = VersionDiplome
    id = factory.Iterator(['ersess', 'ssseer', 'eeerrr'], cycle=False)
    cod_dip = factory.SubFactory(DiplomeFactory)
    cod_vrs_vdi = 'qsd'
    lic_vdi = 'Salut tous le monde '


class VersionEtapeFactory(factory.DjangoModelFactory):
    FACTORY_FOR = VersionEtape
    id = factory.Iterator(['ersess', 'ssseer', 'eeerrr'], cycle=False)
    cod_etp = 'dazdazd'
    cod_vrs_vet = 'dadasd qasd'


class VdiFractionnerVetFactory(factory.DjangoModelFactory):
    FACTORY_FOR = VdiFractionnerVet
    id = factory.Iterator(['ersess', 'ssseer', 'eeerrr'], cycle=False)
    cod_etp = 'abc'
    cod_vrs_vet = 'abc'
    cod_dip = 'abc'
    cod_vrs_vdi = 'abc'
    cod_sis_daa_min = 'abc'

