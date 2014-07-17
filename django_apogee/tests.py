from __future__ import unicode_literals

from django.test import TestCase
from django_apogee.factories import AnneeUniFactory, PaysFactory, DepartementFactory, SitFamFactory, SitMilFactory, \
    TypHandicapFactory, TypeHebergementFactory, SituationSiseFactory, BacOuxEquFactory, MentionBacFactory, ComBdiFactory, \
    TypEtbFactory, EtablissementFactory, CatSocPflFactory, QuotiteTraFactory, DomaineActPflFactory, \
    TypeDiplomeExtFactory, RegimeParentFactory, MtfNonAflSsoFactory, SitSocialeFactory, BourseFactory, ComposanteFactory, \
    CentreGestionFactory, EtapeFactory, EtpGererCgeFactory, ElpFactory, ElpLibelleFactory, DiplomeFactory, \
    CmpHabiliterVdiFactory, VersionEtapeFactory, VdiFractionnerVetFactory
from django_apogee.factories.individu_factories import IndividuFactory, AdressFactory, InsAdmEtpFactory
from django_apogee.models import Individu, Adresse, InsAdmEtp, Pays, Departement, SitFam, SitMil, TypHandicap, \
    TypHebergement, SituationSise, BacOuxEqu, MentionBac, ComBdi, TypEtb, Etablissement, CatSocPfl, QuotiteTra, \
    DomaineActPfl, TypeDiplomeExt, RegimeParent, MtfNonAflSso, SitSociale, Bourse, Composante, CentreGestion, Etape, \
    EtpGererCge, Elp, ElpLibelle, Diplome, CmpHabiliterVdi, VersionEtape, VdiFractionnerVet


class AnimalTestCase(TestCase):

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        print "TestStarting"


class IndividuTestCase(TestCase):

    def test_indvidu_build(self):
        IndividuFactory.build()

    def test_individu_create(self):
        indiv = IndividuFactory.create_individu_with_two_adresses()
        self.assertEqual(1, Individu.objects.count())
        self.assertEqual(2, Adresse.objects.count())

    def test_individu_adresse(self):
        indiv = IndividuFactory.create()
        self.assertEqual("", indiv.get_full_adresse(2010))
        indiv = IndividuFactory.create_individu_with_two_adresses()
        indiv = Individu.objects.get(pk=indiv.pk)
        self.assertNotEqual('', indiv.get_full_adresse(2010))


class InsAdmEtpTestCase(TestCase):

    def test_insadmetp_create(self):
        ins = InsAdmEtpFactory.create()
        self.assertEqual(InsAdmEtp.objects.count(), 1)


class AnneeUniTestCase(TestCase):

    def test_anneeuni_case(self):
        annee1 = AnneeUniFactory.create()
        annee2 = AnneeUniFactory.create()
        self.assertEqual('2013', annee1.cod_anu)
        self.assertEqual('2014', annee2.cod_anu)

    def tearDown(self):
        AnneeUniFactory._declarations['cod_anu'].reset()


class PaysTestCase(TestCase):

    def test_pays_create(self):
        pays = PaysFactory.create()
        self.assertEqual(1, Pays.objects.all().count())


class DepartementTestCase(TestCase):

    def test_departement_create(self):
        dep = DepartementFactory.create()
        self.assertEqual(1, Departement.objects.all().count())


class SitFamTestCase(TestCase):

    def test_sitfam_create(self):
        tst = SitFamFactory.create()
        self.assertEqual(1, SitFam.objects.all().count())

    def tearDown(self):
        SitFamFactory._declarations['cod_fam'].reset()


class SitMilTestCase(TestCase):

    def test_sitmil_create(self):
        tst = SitMilFactory.create()
        self.assertEqual(1, SitMil.objects.all().count())

    def tearDown(self):
        SitMilFactory._declarations['cod_sim'].reset()


class TypHandicapTestCase(TestCase):

    def test_tyhandicap_create(self):
        tst = TypHandicapFactory.create()
        self.assertEqual(1, TypHandicap.objects.all().count())

    def tearDown(self):
        TypHandicapFactory._declarations['cod_thp'].reset()


class TypHebergementTestCase(TestCase):

    def test_typhebergement_create(self):
        tst = TypeHebergementFactory.create()
        self.assertEqual(1, TypHebergement.objects.all().count())

    def tearDown(self):
        TypeHebergementFactory._declarations['cod_thb'].reset()


class SituationSiseTestCase(TestCase):

    def test_situationsise_create(self):
        tst = SituationSiseFactory.create()
        self.assertEqual(1, SituationSise.objects.all().count())

    def tearDown(self):
        SituationSiseFactory._declarations['cod_sis'].reset()


class BacOuxEquTestCase(TestCase):

    def test_create_bacouxequ(self):
        tst = BacOuxEquFactory.create()
        self.assertEqual(1, BacOuxEqu.objects.all().count())

    def tearDown(self):
        BacOuxEquFactory._declarations['cod_bac'].reset()


class MentionBacTestCase(TestCase):

    def test_create_mentionbac(self):
        tst = MentionBacFactory.create()
        self.assertEqual(1, MentionBac.objects.all().count())

    def tearDown(self):
        MentionBacFactory._declarations['cod_mnb'].reset()


class ComBdiTestCase(TestCase):

    def test_create_combdi(self):
        tst = ComBdiFactory.create()
        self.assertEqual(1, ComBdi.objects.all().count())


class TypEtbTestCase(TestCase):

    def test_create_typeetb(self):
        tst = TypEtbFactory.create()
        self.assertEqual(1, TypEtb.objects.all().count())

    def tearDown(self):
        TypEtbFactory._declarations['cod_tpe'].reset()


class EtablissementTestCase(TestCase):

    def test_create_etablissement(self):
        tst = EtablissementFactory.create()
        self.assertEqual(1, Etablissement.objects.all().count())
        self.assertEqual(1, TypEtb.objects.all().count())
        self.assertEqual(1, Departement.objects.all().count())

    def tearDown(self):
        EtablissementFactory._declarations['cod_etb'].reset()


class DepartementTestCase(TestCase):

    def test_create_departement(self):
        tst = DepartementFactory.create()
        self.assertEqual(1, Departement.objects.all().count())

    def tearDown(self):
        DepartementFactory._declarations['cod_dep'].reset()

class CatSocPflTestCase(TestCase):

    def test_create_catsocpfl(self):
        tst = CatSocPflFactory.create()
        self.assertEqual(1, CatSocPfl.objects.all().count())

    def tearDown(self):
        CatSocPflFactory._declarations['cod_pcs'].reset()


class QuotiteTraTestCase(TestCase):

    def test_create_quotitetra(self):
        tst = QuotiteTraFactory.create()
        self.assertEqual(1, QuotiteTra.objects.all().count())

    def tearDown(self):
        QuotiteTraFactory._declarations['cod_qtr'].reset()


class DomaineActPflTestCase(TestCase):

    def test_create_domaineactpfl(self):
        tst = DomaineActPflFactory.create()
        self.assertEqual(1, DomaineActPfl.objects.all().count())

    def tearDown(self):
        DomaineActPflFactory._declarations['cod_dap'].reset()


class SituationSiseTestCase(TestCase):

    def test_create_situationsise(self):
        tst = SituationSiseFactory.create()
        self.assertEqual(1, SituationSise.objects.all().count())

    def tearDown(self):
        SituationSiseFactory._declarations['cod_sis'].reset()


class TypeDiplomeExtTestCase(TestCase):

    def test_create_typediplome(self):
        tst = TypeDiplomeExtFactory.create()
        self.assertEqual(1, TypeDiplomeExt.objects.all().count())

    def tearDown(self):
        TypeDiplomeExtFactory._declarations['cod_tde'].reset()


class RegimeParentTestCase(TestCase):

    def test_create_regimeparent(self):
        tst = RegimeParentFactory.create()
        self.assertEqual(1, RegimeParent.objects.all().count())

    def tearDown(self):
        RegimeParentFactory._declarations['cod_rgp'].reset()


class MtfNonAflSsoTestCase(TestCase):

    def test_create_mtfnonaflsso(self):
        tst = MtfNonAflSsoFactory.create()
        self.assertEqual(1, MtfNonAflSso.objects.all().count())

    def tearDown(self):
        MtfNonAflSsoFactory._declarations['cod_mns'].reset()


class SitSocialeTestCase(TestCase):

    def test_create_sitsociale(self):
        tst = SitSocialeFactory.create()
        self.assertEqual(1, SitSociale.objects.all().count())

    def tearDown(self):
        SitSocialeFactory._declarations['cod_soc'].reset()


class BourseTestCase(TestCase):

    def test_create_bourse(self):
        tst = BourseFactory.create()
        self.assertEqual(1, Bourse.objects.all().count())
        self.assertEqual(1, SitSociale.objects.all().count())

    def tearDown(self):
        BourseFactory._declarations['cod_brs'].reset()


class ComposanteTestCase(TestCase):

    def test_create_composante(self):
        tst = ComposanteFactory.create()
        self.assertEqual(1, Composante.objects.all().count())

    def tearDown(self):
        ComposanteFactory._declarations['cod_cmp'].reset()


class CentreGestionTestCase(TestCase):

    def test_create_centregestion(self):
        tst = CentreGestionFactory.create()
        self.assertEqual(1, CentreGestion.objects.all().count())

    def tearDown(self):
        CentreGestionFactory._declarations['cod_cge'].reset()


class EtapeTestCase(TestCase):

    def test_create_etape(self):
        tst = EtapeFactory.create()
        self.assertEqual(1, Etape.objects.all().count())

    def tearDown(self):
        EtapeFactory._declarations['cod_etp'].reset()


class EtpGererCgeTestCase(TestCase):

    def test_create_etpgerercge(self):
        tst = EtpGererCgeFactory.create()
        self.assertEqual(1, EtpGererCge.objects.all().count())
        self.assertEqual(1, Etape.objects.all().count())
        self.assertEqual(1, Composante.objects.all().count())
        self.assertEqual(1, CentreGestion.objects.all().count())

    def tearDown(self):
        EtapeFactory._declarations['cod_etp'].reset()
        CentreGestionFactory._declarations['cod_cge'].reset()
        ComposanteFactory._declarations['cod_cmp'].reset()


class ElpTestCase(TestCase):

    def test_create_elp(self):
        tst = ElpFactory.create()
        self.assertEqual(1, Elp.objects.all().count())
        self.assertEqual(1, Composante.objects.all().count())

    def tearDown(self):
        ElpFactory._declarations['cod_elp'].reset()


class ElpLibelleTestCase(TestCase):

    def test_create_elplibelle(self):
        tst = ElpLibelleFactory.create()
        self.assertEqual(1, ElpLibelle.objects.all().count())
        self.assertEqual(1, Elp.objects.all().count())

    def tearDown(self):
        ElpLibelleFactory._declarations['id'].reset()


class DiplomeTestCase(TestCase):

    def test_create_diplome(self):
        tst = DiplomeFactory.create()
        self.assertEqual(1, Diplome.objects.all().count())

    def tearDown(self):
        DiplomeFactory._declarations['cod_dip'].reset()


class CmpHabiliterVdiTestCase(TestCase):

    def test_create_cmphabilitervdi(self):
        tst = CmpHabiliterVdiFactory.create()
        self.assertEqual(1, CmpHabiliterVdi.objects.all().count())
        self.assertEqual(1, Composante.objects.all().count())
        self.assertEqual(1, Diplome.objects.all().count())

    def tearDown(self):
        DiplomeFactory._declarations['cod_dip'].reset()
        ComposanteFactory._declarations['cod_cmp'].reset()
        CmpHabiliterVdiFactory._declarations['id'].reset()


class VersionEtapeTestCase(TestCase):

    def test_create_versionetape(self):
        tst = VersionEtapeFactory.create()
        self.assertEqual(1, VersionEtape.objects.all().count())

    def tearDown(self):
        VersionEtapeFactory._declarations['id'].reset()


class VdiFractionnerVetTestCase(TestCase):

    def test_create_vdifractionner(self):
        tst = VdiFractionnerVetFactory.create()
        self.assertEqual(1, VdiFractionnerVet.objects.all().count())

    def tearDown(self):
        VdiFractionnerVetFactory._declarations['id'].reset()




















