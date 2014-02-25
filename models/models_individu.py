# coding=utf-8
import os
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
import unicodedata
from mailrobot.models import Mail
from apogee.managers import EtapeNonCondiValideManagerOracle, EtapeCondiValideManagerOracle, EtapeNonCondiValideManager, EtapeCondiValideManager
from apogee.models import StepApogee, AnneeUni, ApogeeComBdi, ApogeePays
from foad.models import FoadUser, FoadDip, FoadCourUser, CompteMail
from django.conf import settings
from inscription.utils import make_ied_password

__author__ = 'paul'
from django.db import models


class IND_OPI(models.Model):
    COD_IND_OPI = models.IntegerField(u"Code Dossier OPI", primary_key=True)
    COD_SIM = models.CharField(verbose_name=u"Code Situation militaire", max_length=1, null=True,
                               db_column="COD_SIM")
    COD_PAY_NAT = models.CharField(verbose_name=u"Code Pays INSEE", max_length=3, null=True, db_column="COD_PAY_NAT")
    COD_ETB = models.CharField(verbose_name=u"Code National de l'Etablissement de première inscription",
                               max_length=8, null=True,
                               db_column='COD_ETB')
    COD_IND = models.IntegerField(u"Code Dossier OPI", db_column="COD_IND")
    COD_NNE_IND_OPI = models.CharField(u"Identifiant National Etudiant", max_length=10, null=True,
                                       db_column="COD_NNE_IND_OPI")
    COD_CLE_NNE_IND_OPI = models.CharField(u"Cle de l'Identifiant National Etudiant", max_length=1, null=True,
                                           db_column="COD_CLE_NNE_IND_OPI")
    COD_DAP = models.CharField(u"Code Domaine Activite Professionnelle", max_length=2, null=True, db_column="COD_DAP")
    DATE_NAI_IND_OPI = models.DateField(u"Date de naissance de l'individu OPI", db_column="DATE_NAI_IND_OPI")
    TEM_DATE_NAI_REL_OPI = models.CharField(u"Témoin indiquant si la date de naissance estestimée", max_length=1,
                                            default="N", db_column="TEM_DATE_NAI_REL_OPI")
    DAA_LBT_IND_OPI = models.CharField(u"Annee de liberation de l'etudiant qui se trouve sous les drapeaux",
                                       max_length=4, null=True, db_column="DAA_LBT_IND_OPI")
    DMM_LBT_IND_OPI = models.CharField(u"Mois de liberation de l'etudiant qui se trouve sous les drapeaux",
                                       max_length=2, null=True, db_column="DMM_LBT_IND_OPI")
    DAA_ENT_ETB_OPI = models.CharField(u"Annee de premiere inscription dans une universite francaise", max_length=4,
                                       null=True, db_column="DAA_ENT_ETB_OPI")
    LIB_NOM_PAT_IND_OPI = models.CharField(u"Nom Patronymique Etudiant", max_length=30, db_column="LIB_NOM_PAT_IND_OPI")
    LIB_NOM_USU_IND_OPI = models.CharField(u"Nom Usuel Etudiant", max_length=30, null=True,
                                           db_column="LIB_NOM_USU_IND_OPI")
    LIB_PR1_IND_OPI = models.CharField(u"Prenom Premier Etudiant", max_length=20, db_column="LIB_PR1_IND_OPI")
    LIB_PR2_IND_OPI = models.CharField(u"Deuxieme prenom de l'etudiant potentiel", max_length=20, null=True,
                                       db_column="LIB_PR2_IND_OPI")
    LIB_PR3_IND_OPI = models.CharField(u"Troisieme prenom de l'etudiant potentiel", max_length=20, null=True,
                                       db_column="LIB_PR3_IND_OPI")
    NUM_TEL_IND_OPI = models.CharField(u"Numero Telephone Etudiant", max_length=15, null=True,
                                       db_column="NUM_TEL_IND_OPI")
    COD_ETU_OPI = models.IntegerField(null=True)
    LIB_VIL_NAI_ETU_OPI = models.CharField(u"Ville Naissance Etudiant", max_length=30, null=True,
                                           db_column="LIB_VIL_NAI_ETU_OPI")
    COD_OPI_INT_EPO = models.CharField(u"Code de l'etudiant potentiel dans l'interface amont", max_length=10,
                                       db_column="COD_OPI_INT_EPO")
    TEM_MI_TPS_EPO = models.IntegerField(u"Proportion du temps partiel", null=True, db_column="TEM_MI_TPS_EPO")
    COD_FAM = models.CharField(u"(COPIED)Code Situation Famille", max_length=1, null=True, db_column="COD_FAM")
    COD_PCS = models.CharField(u"(COPIED)Code Categorie Socio Professionnelle", max_length=2, null=True,
                               db_column="COD_PCS")
    COD_DEP_PAY_NAI = models.CharField("Département ou pays de naissance", max_length=3, null=True,
                                       db_column="COD_DEP_PAY_NAI")
    COD_TYP_DEP_PAY_NAI = models.CharField(u"Département ou pays de naissance", max_length=1, null=True,
                                           db_column="COD_TYP_DEP_PAY_NAI")
    DAA_ENS_SUP_OPI = models.CharField(u"Année de 1er inscription dans l'enseignementsupérieur", max_length=4,
                                       null=True,
                                       db_column="DAA_ENS_SUP_OPI")
    DAA_ETB_OPI = models.CharField(u"Année de 1er inscription dans l'établissement", max_length=4, null=True,
                                   db_column="DAA_ETB_OPI")
    COD_SEX_ETU_OPI = models.CharField(u"Code sexe OPI de l étudiant", max_length=1, null=True,
                                       db_column="COD_SEX_ETU_OPI")
    COD_THP_OPI = models.CharField(u"Code Handicap OPI de l étudiant", max_length=2, null=True, db_column="COD_THP_OPI")
    COD_THB_OPI = models.CharField(u"Type de l hébergement annuel OPI", max_length=1, null=True,
                                   db_column="COD_THB_OPI")
    ADR_MAIL_OPI = models.CharField(u"Adresse mail de l étudiant", max_length=200, null=True, db_column="ADR_MAIL_OPI")
    NUM_TEL_POR_OPI = models.CharField(u"Numéro de téléphone portable de l étudiant", max_length=15, null=True,
                                       db_column="NUM_TEL_POR_OPI")
    COD_TPE_ANT_IAA = models.CharField(u"Code du type du dernier établissement fréquenté OPI", max_length=2, null=True,
                                       db_column="COD_TPE_ANT_IAA")
    COD_ETB_ANT_IAA = models.CharField(u"Code du dernier établissement fréquenté OPI", max_length=8, null=True,
                                       db_column="COD_ETB_ANT_IAA")  # on est la
    COD_DEP_PAY_ANT_IAA_OPI = models.CharField(u"Code Département ou Pays du dernier établissement fréquenté OPI",
                                               max_length=3, null=True, db_column="COD_DEP_PAY_ANT_IAA_OPI")
    COD_TYP_DEP_PAY_ANT_IAA_OPI = models.CharField(u"Type Département ou Pays du dernier établissement fréquenté OPI",
                                                   max_length=1, null=True, db_column="COD_TYP_DEP_PAY_ANT_IAA_OPI")
    DAA_ETB_ANT_IAA_OPI = models.CharField(u"Année universitaire du dernier établissement fréquenté OPI",
                                           max_length=9, null=True, db_column="DAA_ETB_ANT_IAA_OPI")
    COD_SIS_ANN_PRE_OPI = models.CharField(u"Code situation SISE année précédente OPI", max_length=1, null=True,
                                           db_column="COD_SIS_ANN_PRE_OPI")
    COD_ETB_ANN_PRE_OPI = models.CharField(u"Code établissement de la situation année précédente OPI", max_length=8,
                                           null=True, db_column="COD_ETB_ANN_PRE_OPI")
    COD_DEP_PAY_ANN_PRE_OPI = models.CharField(u"Code Département ou Pays de la situation de lannée précédente OPI",
                                               max_length=3, null=True, db_column="COD_DEP_PAY_ANN_PRE_OPI")
    COD_TYP_DEP_PAY_ANN_PRE_OPI = models.CharField(
        u"Type Département ou Pays de la situation de l année précédente OPI",
        max_length=1, null=True, db_column="COD_TYP_DEP_PAY_ANN_PRE_OPI")
    COD_TDS_OPI = models.CharField(u"Code type diplôme SISE du dernier diplôme obtenu", max_length=1,
                                   null=True, db_column="COD_TDS_OPI")
    COD_ETB_DER_DIP = models.CharField(u"Code établissement où le dernier diplôme a été obtenu", max_length=8,
                                       null=True, db_column="COD_ETB_DER_DIP")
    DAA_ETB_DER_DIP = models.CharField(u"Année universitaire où le dernier diplôme a été obtenu", max_length=9,
                                       null=True, db_column="DAA_ETB_DER_DIP")
    COD_TPE_ANN_CRT = models.CharField(u"Code du type de l autre établissement fréquenté pour l année en cours OPI",
                                       max_length=2, null=True, db_column="COD_TPE_ANN_CRT")
    COD_ETB_ANN_CRT = models.CharField(u"Code de l autre établissement fréquenté pour l année en cours OPI",
                                       max_length=8, null=True, db_column="COD_ETB_ANN_CRT")
    DAA_ETR_SUP = models.CharField(u"Témoin d inscription parallèle dans l autre établissement pour l année en cours",
                                   max_length=9, null=True, db_column="DAA_ETR_SUP")
    COD_TDE_DER_DIP = models.CharField(u"Code du type de dernier diplome", max_length=3, null=True,
                                       db_column="COD_TDE_DER_DIP")
    COD_DEP_PAY_DER_DIP = models.CharField(u"Code pays ou departement du dernier diplome obtenu", max_length=3,
                                           null=True, db_column="COD_DEP_PAY_DER_DIP")
    COD_TYP_DEP_PAY_DER_DIP = models.CharField(u"Code du type du pays ou departement du dernier diplome obtenu",
                                               max_length=1, null=True, db_column="COD_TYP_DEP_PAY_DER_DIP")
    NB_ENF_ETU_OPI = models.IntegerField(u"Nombre d'enfant de l'étudiant", null=True, db_column="NB_ENF_ETU_OPI")
    COD_PCS_AP = models.CharField(u"Code categorie socio-professionnelle autre parent", max_length=2,
                                  default='99', null=True, db_column="COD_PCS_AP")

    class Meta:
        db_table = u'IND_OPI'
        managed = False
        app_label = 'apogee'


class OPI_BAC(models.Model):
    COD_IND_OPI = models.IntegerField(primary_key=True, db_column="COD_IND_OPI")
    COD_BAC = models.CharField(u"(COPIED)Code Baccalaureat ou Equivalence", max_length=4, null=True,
                               db_column="COD_BAC")
    COD_ETB = models.CharField(u"(COPIED)Code National de l'Etablissement", max_length=8, null=True,
                               db_column="COD_ETB")
    COD_TPE = models.CharField(u"(COPIED)Code Type Etablissement", max_length=2, null=True, db_column="COD_TPE")
    COD_DEP = models.CharField(u"COPIED)Code Departement", max_length=3, null=True, db_column="COD_DEP")
    COD_MNB = models.CharField(u"(COPIED)Code Mention Niveau Bac", max_length=2, null=True, db_column="COD_MNB")
    DAA_OBT_BAC_OBA = models.CharField(u"Annee de la date d'obtention du bac", max_length=4, null=True,
                                       db_column="DAA_OBT_BAC_OBA")

    class Meta:
        db_table = u"OPI_BAC"
        managed = False
        app_label = 'apogee'


class ADRESSE_OPI(models.Model):
    COD_IND_OPI = models.IntegerField(primary_key=True, db_column="COD_IND_OPI")
    COD_TYP_ADR_OPI = models.CharField(u"Type de l'adresse OPI", max_length=1, null=True, db_column="COD_TYP_ADR_OPI")
    COD_PAY = models.CharField(u"Code Pays INSEE", max_length=3, null=True, db_column="COD_PAY")
    COD_BDI = models.CharField(u"Code Bureau Distributeur", max_length=5, null=True, db_column="COD_BDI")
    COD_COM = models.CharField(u"Code Commune", max_length=5, null=True, db_column="COD_COM")
    LIB_AD1 = models.CharField(u"Libellé adresse 1", max_length=32, null=True, db_column="LIB_AD1")
    LIB_AD2 = models.CharField(u"Libellé adresse 1", max_length=32, null=True, db_column="LIB_AD2")
    LIB_AD3 = models.CharField(u"Libellé adresse 1", max_length=32, null=True, db_column="LIB_AD3")
    LIB_ADE = models.CharField(u"Libellé adresse 1", max_length=32, null=True, db_column="LIB_ADE")

    class Meta:
        db_table = u"ADRESSE_OPI"
        managed = False
        app_label = 'apogee'


class INDIVIDU(models.Model):
    COD_IND = models.IntegerField(u"Code Etudiant au sein de l'Etablissement", primary_key=True, db_column="COD_IND")
    COD_IND_OPI = models.IntegerField(IND_OPI, db_column="COD_IND_OPI", null=True)
    DAT_CRE_IND = models.DateTimeField(u"Date de création de l'individu", db_column="DAT_CRE_IND", null=True)
    DAT_MOD_IND = models.DateTimeField(u"Date de modification de l'individu", db_column="DAT_MOD_IND", null=True)
    DATE_NAI_IND = models.DateTimeField(u"Date de naissance de l'individu", db_column="DATE_NAI_IND", null=True)
    LIB_NOM_PAT_IND = models.CharField(u"Nom Patronymique Etudiant", max_length=30, null=True,
                                       db_column="LIB_NOM_PAT_IND")
    LIB_NOM_USU_IND = models.CharField(u"Nom Usuel Etudiant", max_length=30, null=True, db_column="LIB_NOM_USU_IND")
    LIB_PR1_IND = models.CharField(u"Prenom 1 de l'Etudiant", max_length=20, null=True, db_column="LIB_PR1_IND")
    LIB_PR2_IND = models.CharField(u"Prenom 2 de l'Etudiant", max_length=20, null=True, db_column="LIB_PR2_IND")
    LIB_PR3_IND = models.CharField(u"Prenom 3 de l'Etudiant", max_length=20, null=True, db_column="LIB_PR3_IND")
    COD_ETU = models.IntegerField(u"Code Etudiant", db_column="COD_ETU", null=True)
    COD_SEX_ETU = models.CharField(u"Code Sexe de l'Etudiant", max_length=1, null=True, db_column="COD_SEX_ETU")
    COD_FAM = models.CharField(u"Code famiale", max_length=1, null=True, db_column="COD_FAM")
    COD_NNE_IND = models.CharField(u"Identifiant National de l'étudiant",
                                   max_length=10, null=True, db_column="COD_NNE_IND")
    COD_CLE_NNE_IND = models.CharField(u"Cle de l'identifiant national etudiant", max_length=1, null=True,
                                       db_column="COD_CLE_NNE_IND")

    def __init__(self, *args, **kwargs):
        super(INDIVIDU, self).__init__(*args, **kwargs)
        from inscription.models import AnneeEnCour
        self.annee = AnneeEnCour.objects.get(annee_en_cours=True)

    def password(self):
        return u"<label>%s</label>" % make_ied_password(self.COD_ETU)
    password.short_description = 'Mot de passe'
    password.allow_tags = True

    def ine(self):
        return u"%s%s" % (self.COD_NNE_IND, self.COD_CLE_NNE_IND)

    def __unicode__(self):
        return u"%s %s %s" % (self.LIB_NOM_PAT_IND, self.LIB_PR1_IND, self.COD_ETU)

    class Meta:
        db_table = "INDIVIDU"
        verbose_name = u"étudiant"
        app_label = 'apogee'

    def identite(self):
        return u"%s %s %s" % (self.LIB_NOM_PAT_IND, self.LIB_NOM_USU_IND, self.LIB_PR1_IND)

    identite.short_description = u"identité"

    def get_adresse_annuelle(self):
        adresse_annuelle = self.adresse_annuelle.filter(COD_ANU_INA=self.annee)
        if adresse_annuelle:
            return adresse_annuelle[0].get_dico()
        else:
            return {'lib_ad1': '',
                    'lib_ad2': '',
                    'lib_ad3': '',
                    'cod_bdi': '',
                    'lib_ach': '',
                    'lib_ade': '',
                    'lib_pay': '',
                    'cod_pay': '',
                    'cod_com': ''}

    def get_adresse_fixe(self):
        adresse_fixe = self.adresse_fixe.all()
        if adresse_fixe:
            return adresse_fixe[0].get_dico()
        else:
            pass
        return {'lib_ad1': '',
                'lib_ad2': '',
                'lib_ad3': '',
                'cod_bdi': '',
                'lib_ach': '',
                'lib_ade': '',
                'lib_pay': '',
                'cod_pay': '',
                'cod_com': ''}

    def get_adresse(self):

        adresse_annuelle = self.adresse_annuelle.filter(COD_ANU_INA=self.annee)
        if adresse_annuelle:
            return adresse_annuelle[0].get_str()
        else:
            return self.adresse_fixe.all()[0].get_str()

    def get_code_postal(self):
        adresse_annuelle = self.adresse_annuelle.filter(COD_ANU_INA=self.annee)
        if adresse_annuelle:
            return adresse_annuelle[0].COD_BDI or adresse_annuelle[0].LIB_ADE
        else:
            return self.adresse_fixe.all()[0].COD_BDI or self.adresse_fixe.all()[0].LIB_ADE

    def get_pays(self):
        adresse_annuelle = self.adresse_annuelle.filter(COD_ANU_INA=self.annee)
        if adresse_annuelle:
            return adresse_annuelle[0].COD_PAY.lib_pay
        else:
            return self.adresse_fixe.all()[0].COD_PAY.lib_pay

    def get_full_adresse(self):
        try:
            adresse_annuelle = self.adresse_annuelle.filter(COD_ANU_INA=self.annee)
            if adresse_annuelle:
                return adresse_annuelle[0].__unicode__()
            else:
                return self.adresse_fixe.all()[0].__unicode__()
        except IndexError:
            return u""

    def get_adresse_html(self):
        try:
            adresse_annuelle = self.adresse_annuelle.filter(COD_ANU_INA=self.annee)
            if adresse_annuelle:
                return adresse_annuelle[0].html()
            else:
                return self.adresse_fixe.all()[0].html()
        except IndexError:
            return u""

    get_full_adresse.short_description = 'Adresse'

    def get_dico_adresse(self):
        adresse_annuelle = self.adresse_annuelle.filter(COD_ANU_INA=self.annee)
        if adresse_annuelle:
            return adresse_annuelle[0].get_dico()
        else:
            return self.adresse_fixe.all()[0].get_dico()

    def get_tel_fixe(self):
        if self.adresse_fixe.all()[0].NUM_TEL != u'':
            return self.adresse_fixe.all()[0].NUM_TEL
        else:
            return self.adresse_fixe.all()[0].NUM_TEL_PORT

    def get_tel_annuel(self):
        adresse_annuelle = self.adresse_annuelle.filter(COD_ANU_INA=self.annee)
        if adresse_annuelle and adresse_annuelle[0].NUM_TEL != u'':
            return adresse_annuelle[0].NUM_TEL
        else:
            return adresse_annuelle[0].NUM_TEL_PORT

    def get_tel(self):
        adresse_annuelle = self.adresse_annuelle.filter(COD_ANU_INA=self.annee)
        if adresse_annuelle and adresse_annuelle[0].NUM_TEL != u'':
            return adresse_annuelle[0].NUM_TEL
        elif adresse_annuelle and adresse_annuelle[0].NUM_TEL_PORT != u'':
            return adresse_annuelle[0].NUM_TEL_PORT
        else:
            return self.adresse_fixe.all()[0].NUM_TEL

    def get_email(self):
        try:
            adresse_annuelle = self.adresse_annuelle.filter(COD_ANU_INA=self.annee)
            if adresse_annuelle and adresse_annuelle[0].ADR_MAIL != '':
                email = adresse_annuelle[0].ADR_MAIL
            else:
                email = self.adresse_fixe.all()[0].ADR_MAIL
        except IndexError:
            email = u""
        return email
    get_email.short_description = u"email personnel"

    def email_ied(self):
        return u"%s@foad.iedparis8.net" % self.COD_ETU
    email_ied.short_description = u"Email Ied"


class Individu(INDIVIDU):
    class Meta:
        proxy = True


class ADRESSE(models.Model):
    COD_ADR = models.IntegerField(u"Code adresse", primary_key=True, db_column="COD_ADR")

    COD_IND = models.ForeignKey(INDIVIDU, db_column="COD_IND", null=True, related_name="adresse_fixe")
    COD_ANU_INA = models.CharField(u"Code Annee Universitaire pour adresse", max_length=4, null=True,
                                   db_column="COD_ANU_INA")
    COD_IND_INA = models.ForeignKey(INDIVIDU, verbose_name=u"Code individu pour adresse annuelle", null=True,
                                    db_column="COD_IND_INA", related_name="adresse_annuelle")

    COD_PAY = models.ForeignKey(ApogeePays, verbose_name=u"Code Pays INSEE", null=True, db_column="COD_PAY")
    COD_BDI = models.CharField(u"Code Bureau Distributeur", max_length=5, null=True, db_column="COD_BDI")
    COD_COM = models.CharField(u"Code Commune", max_length=5, null=True, db_column="COD_COM")
    LIB_AD1 = models.CharField(u"Libellé adresse 1", max_length=32, null=True, db_column="LIB_AD1")
    LIB_AD2 = models.CharField(u"Libellé adresse 2", max_length=32, null=True, db_column="LIB_AD2")
    LIB_AD3 = models.CharField(u"Libellé adresse 3", max_length=32, null=True, db_column="LIB_AD3")
    LIB_ADE = models.CharField(u"Libellé adresse étrangère", max_length=32, null=True, db_column="LIB_ADE")
    NUM_TEL = models.CharField(u"Numéro de téléphone", max_length=15, null=True, db_column="NUM_TEL")
    NUM_TEL_PORT = models.CharField(u"Numéro de téléphone portable de l'étudiant", max_length=15, null=True,
                                    db_column="NUM_TEL_PORT")
    ADR_MAIL = models.CharField(u"Adresse Mail personnelle de l'étudiant", max_length=200, null=True,
                                db_column="ADR_MAIL")

    def get_str(self):
        if self.COD_COM and self.COD_BDI:
            lib_ach = ApogeeComBdi.objects.get(cod_com=self.COD_COM, cod_bdi=self.COD_BDI).lib_ach
        else:
            lib_ach = ""
        if self.COD_IND:
            nom = u"%s %s" % (self.COD_IND.LIB_NOM_PAT_IND, self.COD_IND.LIB_NOM_USU_IND)
            prenom = self.COD_IND.LIB_PR1_IND
        else:
            nom = u"%s %s" % (self.COD_IND_INA.LIB_NOM_PAT_IND, self.COD_IND_INA.LIB_NOM_USU_IND)
            prenom = self.COD_IND_INA.LIB_PR1_IND

        return [nom, prenom, self.LIB_AD1, self.LIB_AD2, self.LIB_AD3, self.COD_BDI, lib_ach, self.LIB_ADE,
                self.COD_PAY.lib_pay]

    def get_dico(self):
        if self.COD_COM and self.COD_BDI:
            lib_ach = ApogeeComBdi.objects.get(cod_com=self.COD_COM, cod_bdi=self.COD_BDI).lib_ach
        else:
            lib_ach = ""

        return {'lib_ad1': self.LIB_AD1,
                'lib_ad2': self.LIB_AD2,
                'lib_ad3': self.LIB_AD3,
                'cod_bdi': self.COD_BDI,
                'cod_com': self.COD_COM,
                'lib_ach': lib_ach,
                'lib_ade': self.LIB_ADE,
                'lib_pay': self.COD_PAY.lib_pay,
                'cod_pay': self.COD_PAY.cod_pay}

    def __unicode__(self):
        adresse = u""
        for x in self.get_str():
            if unicode(x) != u"":
                adresse += unicode(x) + u' '
        if adresse != u"":
            return adresse[:-1]
        else:
            return adresse

    def html(self):
        adresse = u""
        d = self.get_dico()
        a = ['lib_ad1', 'lib_ad2', 'lib_ad3', 'cod_bdi', 'lib_ach', 'lib_ade', 'lib_pay']

        for x in a:
            if unicode(d[x]) != u"":
                adresse += unicode(d[x]) + u'<br>'
        return adresse

    class Meta:
        db_table = u"ADRESSE"
        app_label = 'apogee'


class INS_ADM_ANU(models.Model):
    COD_ANU = models.CharField(u"Code Annee Universitaire", max_length=4, db_column="COD_ANU", primary_key=True)
    COD_IND = models.ForeignKey(INDIVIDU, db_column='COD_IND',
                                related_name="inscription_annuelle")
    COD_RGI = models.CharField(u"Code régime inscription", max_length=1, null=True, db_column="COD_RGI")
    COD_STU = models.CharField(u"Statut de l'étudiant", max_length=2, null=True, db_column="COD_STU")

    class Meta:
        db_table = u"INS_ADM_ANU"
        verbose_name = u"Etape annuelle d'un étudiant"
        verbose_name_plural = u"Etapes annuelles des étudiants"
        app_label = 'apogee'


class INS_ADM_ETP_IED(models.Model):
    id = models.CharField(primary_key=True, max_length=26)
    COD_ANU = models.ForeignKey(AnneeUni, verbose_name=u"Code Annee Universitaire")
    COD_IND = models.ForeignKey(INDIVIDU, db_column='COD_IND', related_name="etapes_ied")
    COD_ETP = models.CharField(u"Code Etape", max_length=8, null=True,
                               db_column="COD_ETP")
    COD_VRS_VET = models.CharField(u"(COPIED)Numero Version Etape", max_length=3, db_column="COD_VRS_VET")
    NUM_OCC_IAE = models.CharField(u"", max_length=2, null=True, db_column="NUM_OCC_IAE")
    COD_DIP = models.CharField(u"(COPIED)Code Diplome Etablissement", max_length=7, null=True, db_column="COD_DIP")
    COD_CGE = models.CharField(u"(COPIED)Code Centre de Gestion", max_length=3, null=True, db_column="COD_CGE")
    DAT_CRE_IAE = models.DateTimeField(u"Date de création de l'IAE", null=True, db_column="DAT_CRE_IAE")
    DAT_MOD_IAE = models.DateTimeField(u"Date de modification de l'IAE", null=True, db_column="DAT_MOD_IAE")
    NBR_INS_CYC = models.IntegerField(u'Nombre d\'Inscriptions dans le Cycle', null=True, db_column="NBR_INS_CYC")
    NBR_INS_ETP = models.IntegerField(u"Nombre d'Inscriptions dans l'Etape", null=True, db_column="NBR_INS_ETP")
    DAT_ANNUL_RES_IAE = models.DateTimeField(u"Date annulation ou résiliation IA", null=True,
                                             db_column="DAT_ANNUL_RES_IAE")
    TEM_IAE_PRM = models.CharField(u"Temoin Etape Premiere ou Seconde", max_length=1, null=True,
                                   db_column="TEM_IAE_PRM")
    NBR_INS_DIP = models.IntegerField(u"Nombre d'Inscriptions dans le DIP", null=True, db_column="NBR_INS_DIP")
    ETA_IAE = models.CharField(u"etat de l'inscription", null=True, max_length=1, db_column='ETA_IAE')
    ETA_PMT_IAE = models.CharField(u"Etat des paiements des droits", null=True, max_length=1, db_column="ETA_PMT_IAE")
    COD_PRU = models.CharField(u"Code profil étudiant", null=True, max_length=2, db_column="COD_PRU")
    exoneration = models.CharField(u"Exonération", max_length=1, blank=True, null=True, choices=(('T', 'Total'),
                                                                                                 ('P', 'Partiel')))
    step = models.ForeignKey(StepApogee, null=True)
    demi_annee = models.BooleanField(u"Demi année", default=False)
    force_encaissement = models.BooleanField(u"Forcée l'encaissement", blank=True, default=False)
    #remontee = models.BooleanField(default=False)
    objects = models.Manager()
    inscrits = EtapeNonCondiValideManager()
    inscrits_condi = EtapeCondiValideManager()

    class Meta:
        db_table = u"INS_ADM_ETP_IED"
        verbose_name = u"Etape"
        verbose_name_plural = u"etapes de l'étudiant"
        app_label = 'apogee'

    # def  get_absolute_url(self):
    #     return u"%s/%s" % (self.COD_ANU, self.pk)

    def remontee_claroline(self, cours=None, envoi_mail=True, mail=None, email_perso=None):
        c2i = ["L1NDRO", "L2NDRO", "L3NDRO", "L1NPSY", "L2NPSY", "L3NPSY", "L3NEDU"]
        cod_etp = self.COD_ETP
        individu = self.COD_IND

        # on cherche le étape en dessous pour les licences
        if cod_etp[0] == 'L' and cod_etp != 'L3NEDU':
            etapes = ['L' + str(x+1) + cod_etp[2:] for x in range(int(cod_etp[1]))]
        else:
            etapes = [cod_etp]
        user_foad = FoadUser.objects.using('foad').filter(username=str(individu.COD_ETU))
        if not user_foad.count():
            user_foad = FoadUser.objects.using('foad').filter(username=individu.COD_ETU)
        if user_foad.count():
            user_foad = user_foad[0]
        else:
            user_foad = FoadUser(username=individu.COD_ETU)
        if not individu.COD_ETU:
            raise Exception(u"Il n'y a pas de code étudiant")
        user_foad.email = str(individu.COD_ETU) + '@foad.iedparis8.net'
        user_foad.nom = individu.LIB_NOM_PAT_IND
        user_foad.prenom = individu.LIB_PR1_IND
        user_foad.statut = 5
        user_foad.official_code = individu.COD_ETU
        user_foad.password = make_ied_password(individu.COD_ETU)
        user_foad.save(using='foad')  # création de l'user
        for e in etapes:
            dips = FoadDip.objects.using('foad').filter(user_id=user_foad.user_id, dip_id=e)
            if not dips.count():
                FoadDip.objects.using('foad').create(user_id=user_foad.user_id, dip_id=e)
            if cours:
                for cour in cours[e]:
                    t = FoadCourUser.objects.using('foad').get_or_create(user_id=user_foad.user_id,
                                                                         code_cours=cour,
                                                                         statut=5)
        FoadCourUser.objects.using('foad').get_or_create(user_id=user_foad.user_id,
                                                         code_cours="EEIED",
                                                         statut=5)
        FoadCourUser.objects.using('foad').get_or_create(user_id=user_foad.user_id,
                                                         code_cours="RD",
                                                         statut=5)
        FoadCourUser.objects.using('foad').get_or_create(user_id=user_foad.user_id,
                                                         code_cours="ISIED",
                                                         statut=5)
        new = FoadCourUser.objects.using('foad').get_or_create(user_id=user_foad.user_id,
                                                               code_cours="EU",
                                                               statut=5)[1]
        if self.COD_ETP in c2i:
            FoadCourUser.objects.using('foad').get_or_create(user_id=user_foad.user_id,
                                                         code_cours="EDR2INFA12",
                                                         statut=5)
            FoadCourUser.objects.using('foad').get_or_create(user_id=user_foad.user_id,
                                                         code_cours="C2IIED",
                                                         statut=5)
        if not CompteMail.objects.using('vpopmail').filter(pw_name=user_foad.username):
            cod = user_foad.prenom.replace(" ", "\\ ").replace("'", "\\'") + '-' + user_foad.nom.replace(" ", "\\ ").replace("'", "\\'")
            cod = unicodedata.normalize('NFKD', unicode(cod)).encode("ascii", "ignore").upper()
            command = u'/home/ied-www/bin/vadduser  -q 500000000 -c "%s" %s %s' % (
                cod,
                user_foad.email,
                user_foad.password
            )

            os.system(command)
        if not email_perso:
            email = [individu.get_email(), individu.email_ied()] if not settings.DEBUG else ['paul.guichon@iedparis8.net']
        else:
            email = [email_perso]
        if envoi_mail:
            if not mail:
                mail = Mail.objects.get(name='remontee')
            message = mail.make_message(
                recipients=email,
                context={
                    'etape': cod_etp,
                    'prenom': user_foad.prenom,
                    'username': user_foad.username,
                    'password': user_foad.password,
                    'email': user_foad.email,

                    })
            message.send()
        self.remontee.remontee = True
        self.remontee.save()
        return 1

    def get_foad_user_dip(self):
        from inscription.models import AnneeEnCour
        annee = AnneeEnCour.objects.get(annee_en_cours=True).annee

        if str(annee) != str(self.COD_ANU):
            return u"Ancienne inscription"
        response = u""
        if not self.COD_IND:
            return u"ERREUR"
        try:
            user = FoadUser.objects.using('foad').get(username=self.COD_IND.COD_ETU)
            dips = user.foaddip_set.all()

            for dip in dips:
                response += u"%s <br>" % dip.dip_id
        except FoadUser.DoesNotExist:
            response += u"L'utisateur n'est pas dans la plateforme"
        except Exception, e:
            response += unicode(e)

        return response
    get_foad_user_dip.short_description = u"Inscription dans la plateforme"
    get_foad_user_dip.allow_tags = True

    def save(self, force_insert=False, force_update=False, using=None):
        if not self.pk:
            self.pk = str(self.COD_ANU_id) + str(self.COD_IND_id) + str(self.COD_ETP) + str(self.COD_VRS_VET) \
                      + str(self.NUM_OCC_IAE)
        if not self.step:
            step_id = StepApogee.objects.using("default").get(annee__cod_anu=self.COD_ANU, name=self.COD_ETP).id
            self.step_id = step_id
        try:
            self.etiquettes
            return super(INS_ADM_ETP_IED, self).save(force_insert=force_insert, force_update=force_update,
                                                     using=using)
        except:
            a = super(INS_ADM_ETP_IED, self).save(force_insert=force_insert, force_update=force_update, using=using)
            EtiquetteEtape.objects.get_or_create(etape=self)
            return a

    def cod_opi(self):
        return u"%s" % self.COD_IND.COD_IND_OPI

    cod_opi.short_description = u"Code opi"

    def is_reins(self):
        if self.NBR_INS_ETP == 1:
            return False
        else:
            return True

    def can_demi_annee(self):
        if self.NBR_INS_ETP == 1 and self.step.demi_tarif:
            return True
        else:
            return False

    def get_tarif(self):
        tarif = self.step.get_tarif_paiement(reins=self.is_reins(), semestre=self.demi_annee)
        if self.exoneration:
            if self.exoneration == 'T':
                tarif = 0
            elif self.exoneration == 'P':
                tarif /= 2.0
        total_payer = 0
        for x in self.paiements.filter(is_ok=False):
            total_payer += x.somme
        reste = tarif - total_payer
        return "Total : %s | Saisi : %s | Reste %s" % (tarif, total_payer, reste)

    get_tarif.short_description = "Tarif"

    def nom(self):
        return unicode(self.COD_IND.LIB_NOM_PAT_IND)

    nom.short_description = 'Nom'

    def prenom(self):
        return unicode(self.COD_IND.LIB_PR1_IND)

    prenom.short_description = 'Prenom'

    def cod_etu(self):
        return unicode(self.COD_IND.COD_ETU)

    cod_etu.short_description = 'Code étudiant'

    def adresse(self):
        return unicode(self.COD_IND.get_full_adresse())

    adresse.short_description = 'Adresse'

    def annulation(self):
        etat = self.ETA_IAE
        if etat == "E":
            return u"En cours"
        elif etat == 'R':
            return u"Résiliée"
        elif etat == 'A':
            return u"Annulée le %s" % self.DAT_ANNUL_RES_IAE
        else:
            return u'<span class="input label label-warning">Dossier détruit Annomalie</span>'

    annulation.short_description = "Etat de l'inscription administrative"
    annulation.allow_tags = True

    def __unicode__(self):
        return u"%s %s %s" % (self.COD_IND.COD_ETU, self.COD_ETP, self.COD_ANU)

    def resume(self):
        return u"Etape : %s | Année : %s |Centre de gestion %s" % (self.COD_ETP, self.COD_ANU, self.COD_CGE)

    resume.short_description = u"Etape"

    def date(self):
        return u"Date de création : %s | Date de modification : %s | Date de résiliation : %s" % (
            self.DAT_CRE_IAE, self.DAT_MOD_IAE if self.DAT_MOD_IAE else u"",
            self.DAT_ANNUL_RES_IAE if self.DAT_ANNUL_RES_IAE else u""
        )

    date.short_description = u"Dates d'opération"

    def condi(self):

        if self.COD_PRU == 'NO':
            return u"Normal"
        elif self.COD_PRU == 'AJ':
            return u"Ajac"
        elif self.COD_PRU == 'FP':
            return u"Formation permanente"
        else:
            return u"INCONNU"

    condi.short_description = u"Niveau de l'inscription"


class Remontee(models.Model):
    remontee = models.BooleanField(default=False)
    in_plateforme = models.BooleanField(default=False)
    etape = models.OneToOneField('INS_ADM_ETP_IED', related_name="remontee")

    class Meta:
        db_table = u"pal_remontee"
        app_label = 'apogee'


class INS_ADM_ETP(models.Model):
    COD_ANU = models.CharField(u"Code Annee Universitaire", max_length=4, db_column="COD_ANU")
    COD_IND = models.ForeignKey(INDIVIDU, db_column='COD_IND', primary_key=True, related_name="etapes")
    COD_ETP = models.CharField(u"(COPIED)(COPIED)Code Etape", max_length=6, null=True, db_column="COD_ETP")
    COD_VRS_VET = models.CharField(u"(COPIED)Numero Version Etape", max_length=3, null=True, db_column="COD_VRS_VET")
    NUM_OCC_IAE = models.CharField(u"", max_length=2, null=True, db_column="NUM_OCC_IAE")
    COD_DIP = models.CharField(u"(COPIED)Code Diplome Etablissement", max_length=7, null=True, db_column="COD_DIP")
    COD_CGE = models.CharField(u"(COPIED)Code Centre de Gestion", max_length=3, null=True, db_column="COD_CGE")
    DAT_CRE_IAE = models.DateTimeField(u"Date de création de l'IAE", null=True, db_column="DAT_CRE_IAE")
    DAT_MOD_IAE = models.DateTimeField(u"Date de modification de l'IAE", null=True, db_column="DAT_MOD_IAE")
    NBR_INS_CYC = models.IntegerField(u'Nombre d\'Inscriptions dans le Cycle', null=True, db_column="NBR_INS_CYC")
    NBR_INS_ETP = models.IntegerField(u"Nombre d'Inscriptions dans l'Etape", null=True, db_column="NBR_INS_ETP")
    DAT_ANNUL_RES_IAE = models.DateTimeField(u"Date annulation ou résiliation IA", null=True,
                                             db_column="DAT_ANNUL_RES_IAE")
    TEM_IAE_PRM = models.CharField(u"Temoin Etape Premiere ou Seconde", max_length=1, null=True,
                                   db_column="TEM_IAE_PRM")
    NBR_INS_DIP = models.IntegerField(u"Nombre d'Inscriptions dans le DIP", null=True, db_column="NBR_INS_DIP")
    ETA_IAE = models.CharField(u"etat de l'inscription", null=True, max_length=1, db_column='ETA_IAE')
    ETA_PMT_IAE = models.CharField(u"Etat des paiements des droits", null=True, max_length=1, db_column="ETA_PMT_IAE")
    COD_PRU = models.CharField(u"Code profil étudiant", null=True, max_length=2, db_column="COD_PRU")
    inscrits = EtapeNonCondiValideManagerOracle()
    inscrits_condi = EtapeCondiValideManagerOracle()

    objects = models.Manager()

    class Meta:
        db_table = u"INS_ADM_ETP"
        app_label = 'apogee'

    def save_copy(self, using='default'):
        ins = INS_ADM_ETP_IED()
        ins.COD_ANU_id = self.COD_ANU
        ins.COD_IND = self.COD_IND
        ins.COD_ETP = self.COD_ETP
        ins.COD_VRS_VET = self.COD_VRS_VET
        ins.NUM_OCC_IAE = self.NUM_OCC_IAE
        ins.COD_DIP = self.COD_DIP
        ins.COD_CGE = self.COD_CGE
        ins.ETA_IAE = self.ETA_IAE
        ins.DAT_CRE_IAE = self.DAT_CRE_IAE
        ins.DAT_MOD_IAE = self.DAT_MOD_IAE
        ins.NBR_INS_CYC = self.NBR_INS_CYC
        ins.NBR_INS_ETP = self.NBR_INS_ETP
        ins.DAT_ANNUL_RES_IAE = self.DAT_ANNUL_RES_IAE
        ins.TEM_IAE_PRM = self.TEM_IAE_PRM
        ins.NBR_INS_DIP = self.NBR_INS_DIP
        ins.ETA_PMT_IAE = self.ETA_PMT_IAE
        ins.COD_PRU = self.COD_PRU

        ins.save(using=using)
        if not hasattr(ins, 'remontee'):
            Remontee.objects.create(etape=ins)



class EtiquetteEtape(models.Model):
    etape = models.OneToOneField(INS_ADM_ETP_IED, related_name="etiquettes")
    certif_scol = models.BooleanField(default=False)

    class Meta:
        db_table = u"pal_etiquette_backoffice"
        app_label = 'apogee'


class IndividuApogee(INDIVIDU):

    def __unicode__(self):
        return u"%s %s %s" % (self.LIB_NOM_PAT_IND, self.LIB_PR1_IND, self.DATE_NAI_IND)

    class Meta:
        proxy = True
        app_label = 'apogee'

    def get_pdf_etudiant(self):
        url = reverse('code_etudiant_pdf', kwargs={'id': self.COD_ETU})
        return '<a href="' + url + '" class="btn btn-primary">Imprimer le pdf</a>'

    def password(self):
        return u"%s" % make_ied_password(self.COD_ETU)
    password.short_description = "Code étudiant"

    get_pdf_etudiant.short_description = u"Pdf du code étudiant"
    get_pdf_etudiant.allow_tags = True
