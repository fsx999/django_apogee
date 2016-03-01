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

    def test_get_code_secret(self):
        indiv = IndividuFactory.create()
        d = {
            # cod_etu: get_code_secret
            14511970: '6879',
            14511502: '6494',
            10270047: '3071',
        }
        for k, v in d.iteritems():
            indiv.cod_etu = k
            self.assertEqual(v, indiv.get_code_secret())

    def test_ine(self):
        indiv = IndividuFactory.create()
        d = {
            # cod_nne_ind: cod_cle_nne_ind
            '2596027058': 'S',
            '2598052337': 'G',
            '0G4145005D': '3',
        }
        for k, v in d.iteritems():
            indiv.cod_nne_ind = k
            indiv.cod_cle_nne_ind = v
            self.assertEqual(indiv.ine(), "{}{}".format(k, v))

    def test_identite(self):
        indiv = IndividuFactory.create()

        self.assertEqual(indiv.identite(),
                         "{} {} {}".format(indiv.lib_nom_pat_ind,
                                           indiv.lib_nom_usu_ind,
                                           indiv.lib_pr1_ind))

    def test_get_adresse_annuelle(self):
        indiv = IndividuFactory.create_individu_with_two_adresses()
        self.assertIsNotNone(indiv.get_adresse_annuelle(2014)['lib_pay'])

    def test_get_adresse_fixe(self):
        indiv = IndividuFactory.create_individu_with_two_adresses()
        self.assertIsNotNone(indiv.get_adresse_fixe()['lib_pay'])

    def test_get_adresse(self):
        indiv = IndividuFactory.create_individu_with_two_adresses()
        self.assertEqual(list, type(indiv.get_adresse(2014)))

    def test_get_code_postal(self):
        indiv = IndividuFactory.create_individu_with_two_adresses()
        self.assertIsNone(indiv.get_code_postal(2014))

    def test_get_pays(self):
        indiv = IndividuFactory.create_individu_with_two_adresses()
        self.assertIsNotNone(indiv.get_pays(2014))

    def test_get_full_adresse(self):
        indiv = IndividuFactory.create_individu_with_two_adresses()
        self.assertIsNotNone(indiv.get_full_adresse(2014))

    def test_get_adresse_html(self):
        indiv = IndividuFactory.create_individu_with_two_adresses()
        self.assertIsNotNone(indiv.get_adresse_html())

    def test_get_dico_adresse(self):
        indiv = IndividuFactory.create_individu_with_two_adresses()
        self.assertEqual(dict, type(indiv.get_dico_adresse(2014)))

    def test_get_tel_fixe(self):
        indiv = IndividuFactory.create_individu_with_two_adresses()
        self.assertIsNotNone(indiv.get_tel_fixe())

    def test_get_tel_annuel(self):
        indiv = IndividuFactory.create_individu_with_two_adresses()
        self.assertIsNotNone(indiv.get_tel_annuel(2014))

    def test_get_tel(self):
        indiv = IndividuFactory.create_individu_with_two_adresses()
        self.assertIsNotNone(indiv.get_tel(2014))

    def test_get_email(self):
        indiv = IndividuFactory.create_individu_with_two_adresses()
        self.assertIsNotNone(indiv.get_email(2014))

    def test_get_etiquette(self):
        indiv = IndividuFactory.create()
        self.assertIsNone(indiv.get_etiquette())

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


class SitMilTestCase(TestCase):

    def test_sitmil_create(self):
        tst = SitMilFactory.create()
        self.assertEqual(1, SitMil.objects.all().count())


class TypHandicapTestCase(TestCase):

    def test_tyhandicap_create(self):
        tst = TypHandicapFactory.create()
        self.assertEqual(1, TypHandicap.objects.all().count())


class TypHebergementTestCase(TestCase):

    def test_typhebergement_create(self):
        tst = TypeHebergementFactory.create()
        self.assertEqual(1, TypHebergement.objects.all().count())


class SituationSiseTestCase(TestCase):

    def test_situationsise_create(self):
        tst = SituationSiseFactory.create()
        self.assertEqual(1, SituationSise.objects.all().count())


class BacOuxEquTestCase(TestCase):

    def test_create_bacouxequ(self):
        tst = BacOuxEquFactory.create()
        self.assertEqual(1, BacOuxEqu.objects.all().count())


class MentionBacTestCase(TestCase):

    def test_create_mentionbac(self):
        tst = MentionBacFactory.create()
        self.assertEqual(1, MentionBac.objects.all().count())


class ComBdiTestCase(TestCase):

    def test_create_combdi(self):
        tst = ComBdiFactory.create()
        self.assertEqual(1, ComBdi.objects.all().count())


class TypEtbTestCase(TestCase):

    def test_create_typeetb(self):
        tst = TypEtbFactory.create()
        self.assertEqual(1, TypEtb.objects.all().count())


class EtablissementTestCase(TestCase):

    def test_create_etablissement(self):
        tst = EtablissementFactory.create()
        self.assertEqual(1, Etablissement.objects.all().count())
        self.assertEqual(1, TypEtb.objects.all().count())
        self.assertEqual(1, Departement.objects.all().count())


class DepartementTestCase(TestCase):

    def test_create_departement(self):
        tst = DepartementFactory.create()
        self.assertEqual(1, Departement.objects.all().count())


class CatSocPflTestCase(TestCase):

    def test_create_catsocpfl(self):
        tst = CatSocPflFactory.create()
        self.assertEqual(1, CatSocPfl.objects.all().count())


class QuotiteTraTestCase(TestCase):

    def test_create_quotitetra(self):
        tst = QuotiteTraFactory.create()
        self.assertEqual(1, QuotiteTra.objects.all().count())


class DomaineActPflTestCase(TestCase):

    def test_create_domaineactpfl(self):
        tst = DomaineActPflFactory.create()
        self.assertEqual(1, DomaineActPfl.objects.all().count())


class SituationSiseTestCase(TestCase):

    def test_create_situationsise(self):
        tst = SituationSiseFactory.create()
        self.assertEqual(1, SituationSise.objects.all().count())


class TypeDiplomeExtTestCase(TestCase):

    def test_create_typediplome(self):
        tst = TypeDiplomeExtFactory.create()
        self.assertEqual(1, TypeDiplomeExt.objects.all().count())


class RegimeParentTestCase(TestCase):

    def test_create_regimeparent(self):
        tst = RegimeParentFactory.create()
        self.assertEqual(1, RegimeParent.objects.all().count())


class MtfNonAflSsoTestCase(TestCase):

    def test_create_mtfnonaflsso(self):
        tst = MtfNonAflSsoFactory.create()
        self.assertEqual(1, MtfNonAflSso.objects.all().count())


class SitSocialeTestCase(TestCase):

    def test_create_sitsociale(self):
        tst = SitSocialeFactory.create()
        self.assertEqual(1, SitSociale.objects.all().count())


class BourseTestCase(TestCase):

    def test_create_bourse(self):
        tst = BourseFactory.create()
        self.assertEqual(1, Bourse.objects.all().count())
        self.assertEqual(1, SitSociale.objects.all().count())


class ComposanteTestCase(TestCase):

    def test_create_composante(self):
        tst = ComposanteFactory.create()
        self.assertEqual(1, Composante.objects.all().count())


class CentreGestionTestCase(TestCase):

    def test_create_centregestion(self):
        tst = CentreGestionFactory.create()
        self.assertEqual(1, CentreGestion.objects.all().count())


class EtapeTestCase(TestCase):

    def test_create_etape(self):
        tst = EtapeFactory.create()
        self.assertEqual(1, Etape.objects.all().count())


class EtpGererCgeTestCase(TestCase):

    def test_create_etpgerercge(self):
        tst = EtpGererCgeFactory.create()
        self.assertEqual(1, EtpGererCge.objects.all().count())
        self.assertEqual(1, Etape.objects.all().count())
        self.assertEqual(1, Composante.objects.all().count())
        self.assertEqual(1, CentreGestion.objects.all().count())


class ElpTestCase(TestCase):

    def test_create_elp(self):
        tst = ElpFactory.create()
        self.assertEqual(1, Elp.objects.all().count())
        self.assertEqual(1, Composante.objects.all().count())


class ElpLibelleTestCase(TestCase):

    def test_create_elplibelle(self):
        tst = ElpLibelleFactory.create()
        self.assertEqual(1, ElpLibelle.objects.all().count())
        self.assertEqual(1, Elp.objects.all().count())


class DiplomeTestCase(TestCase):

    def test_create_diplome(self):
        tst = DiplomeFactory.create()
        self.assertEqual(1, Diplome.objects.all().count())


class CmpHabiliterVdiTestCase(TestCase):

    def test_create_cmphabilitervdi(self):
        tst = CmpHabiliterVdiFactory.create()
        self.assertEqual(1, CmpHabiliterVdi.objects.all().count())
        self.assertEqual(1, Composante.objects.all().count())
        self.assertEqual(1, Diplome.objects.all().count())


class VersionEtapeTestCase(TestCase):

    def test_create_versionetape(self):
        tst = VersionEtapeFactory.create()
        self.assertEqual(1, VersionEtape.objects.all().count())


class VdiFractionnerVetTestCase(TestCase):

    def test_create_vdifractionner(self):
        tst = VdiFractionnerVetFactory.create()
        self.assertEqual(1, VdiFractionnerVet.objects.all().count())

