# coding=utf-8
from __future__ import unicode_literals
__author__ = 'paul'
from managers import EtapeNonCondiValideManagerOracle, EtapeCondiValideManagerOracle, EtapeNonCondiValideManager, EtapeCondiValideManager
from models import Etape, AnneeUni, ComBdi, Pays
from django.db import models


class IndOpi(models.Model):
    """
    Table opi pour l'individu.
    Cette classe permet d'insérer les individus d'une application externe vers apogée via OPI.
    L'ensemble des tables ne doivent jamais être créés car les models contiennent le nécessaire pour l'envoie de données
    dans apogée ainsi que la lecture, mais il n'y a pas le nécessaire pour la création de la table et la liaison des
    données vers d'autres modèles (clè primaire composite.
    """
    cod_ind_opi = models.IntegerField(u"Code Dossier OPI", primary_key=True)
    cod_sim = models.CharField(verbose_name=u"Code Situation militaire", max_length=1, null=True,
                               db_column="COD_SIM")
    cod_pay_nat = models.CharField(verbose_name=u"Code Pays INSEE", max_length=3, null=True, db_column="COD_PAY_NAT")
    cod_etb = models.CharField(verbose_name=u"Code National de l'Etablissement de première inscription",
                               max_length=8, null=True,
                               db_column='COD_ETB')
    cod_ind = models.IntegerField(u"Code Dossier OPI", db_column="COD_IND")
    cod_nne_ind_opi = models.CharField(u"Identifiant National Etudiant", max_length=10, null=True,
                                       db_column="COD_NNE_IND_OPI")
    cod_cle_nne_ind_opi = models.CharField(u"Cle de l'Identifiant National Etudiant", max_length=1, null=True,
                                           db_column="COD_CLE_NNE_IND_OPI")
    cod_dap = models.CharField(u"Code Domaine Activite Professionnelle", max_length=2, null=True, db_column="COD_DAP")
    date_nai_ind_opi = models.DateField(u"Date de naissance de l'individu OPI", db_column="DATE_NAI_IND_OPI")
    tem_date_nai_rel_opi = models.CharField(u"Témoin indiquant si la date de naissance estestimée", max_length=1,
                                            default="N", db_column="TEM_DATE_NAI_REL_OPI")
    daa_lbt_ind_opi = models.CharField(u"Annee de liberation de l'etudiant qui se trouve sous les drapeaux",
                                       max_length=4, null=True, db_column="DAA_LBT_IND_OPI")
    dmm_lbt_ind_opi = models.CharField(u"Mois de liberation de l'etudiant qui se trouve sous les drapeaux",
                                       max_length=2, null=True, db_column="DMM_LBT_IND_OPI")
    daa_ent_etb_opi = models.CharField(u"Annee de premiere inscription dans une universite francaise", max_length=4,
                                       null=True, db_column="DAA_ENT_ETB_OPI")
    lib_nom_pat_ind_opi = models.CharField(u"Nom Patronymique Etudiant", max_length=30, db_column="LIB_NOM_PAT_IND_OPI")
    lib_nom_usu_ind_opi = models.CharField(u"Nom Usuel Etudiant", max_length=30, null=True,
                                           db_column="LIB_NOM_USU_IND_OPI")
    lib_pr1_ind_opi = models.CharField(u"Prenom Premier Etudiant", max_length=20, db_column="LIB_PR1_IND_OPI")
    lib_pr2_ind_opi = models.CharField(u"Deuxieme prenom de l'etudiant potentiel", max_length=20, null=True,
                                       db_column="LIB_PR2_IND_OPI")
    lib_pr3_ind_opi = models.CharField(u"Troisieme prenom de l'etudiant potentiel", max_length=20, null=True,
                                       db_column="LIB_PR3_IND_OPI")
    num_tel_ind_opi = models.CharField(u"Numero Telephone Etudiant", max_length=15, null=True,
                                       db_column="NUM_TEL_IND_OPI")
    cod_etu_opi = models.IntegerField(null=True)
    lib_vil_nai_etu_opi = models.CharField(u"Ville Naissance Etudiant", max_length=30, null=True,
                                           db_column="LIB_VIL_NAI_ETU_OPI")
    cod_opi_int_epo = models.CharField(u"Code de l'etudiant potentiel dans l'interface amont", max_length=10,
                                       db_column="COD_OPI_INT_EPO")
    tem_mi_tps_epo = models.IntegerField(u"Proportion du temps partiel", null=True, db_column="TEM_MI_TPS_EPO")
    cod_fam = models.CharField(u"(COPIED)Code Situation Famille", max_length=1, null=True, db_column="COD_FAM")
    cod_pcs = models.CharField(u"(COPIED)Code Categorie Socio Professionnelle", max_length=2, null=True,
                               db_column="COD_PCS")
    cod_dep_pay_nai = models.CharField("Département ou pays de naissance", max_length=3, null=True,
                                       db_column="COD_DEP_PAY_NAI")
    cod_typ_dep_pay_nai = models.CharField(u"Département ou pays de naissance", max_length=1, null=True,
                                           db_column="COD_TYP_DEP_PAY_NAI")
    daa_ens_sup_opi = models.CharField(u"Année de 1er inscription dans l'enseignementsupérieur", max_length=4,
                                       null=True,
                                       db_column="DAA_ENS_SUP_OPI")
    daa_etb_opi = models.CharField(u"Année de 1er inscription dans l'établissement", max_length=4, null=True,
                                   db_column="DAA_ETB_OPI")
    cod_sex_etu_opi = models.CharField(u"Code sexe OPI de l étudiant", max_length=1, null=True,
                                       db_column="COD_SEX_ETU_OPI")
    cod_thp_opi = models.CharField(u"Code Handicap OPI de l étudiant", max_length=2, null=True, db_column="COD_THP_OPI")
    cod_thb_opi = models.CharField(u"Type de l hébergement annuel OPI", max_length=1, null=True,
                                   db_column="COD_THB_OPI")
    adr_mail_opi = models.CharField(u"Adresse mail de l étudiant", max_length=200, null=True, db_column="ADR_MAIL_OPI")
    num_tel_por_opi = models.CharField(u"Numéro de téléphone portable de l étudiant", max_length=15, null=True,
                                       db_column="NUM_TEL_POR_OPI")
    cod_tpe_ant_iaa = models.CharField(u"Code du type du dernier établissement fréquenté OPI", max_length=2, null=True,
                                       db_column="COD_TPE_ANT_IAA")
    cod_etb_ant_iaa = models.CharField(u"Code du dernier établissement fréquenté OPI", max_length=8, null=True,
                                       db_column="COD_ETB_ANT_IAA")  # on est la
    cod_dep_pay_ant_iaa_opi = models.CharField(u"Code Département ou Pays du dernier établissement fréquenté OPI",
                                               max_length=3, null=True, db_column="COD_DEP_PAY_ANT_IAA_OPI")
    cod_typ_dep_pay_ant_iaa_opi = models.CharField(u"Type Département ou Pays du dernier établissement fréquenté OPI",
                                                   max_length=1, null=True, db_column="COD_TYP_DEP_PAY_ANT_IAA_OPI")
    daa_etb_ant_iaa_opi = models.CharField(u"Année universitaire du dernier établissement fréquenté OPI",
                                           max_length=9, null=True, db_column="DAA_ETB_ANT_IAA_OPI")
    cod_sis_ann_pre_opi = models.CharField(u"Code situation SISE année précédente OPI", max_length=1, null=True,
                                           db_column="COD_SIS_ANN_PRE_OPI")
    cod_etb_ann_pre_opi = models.CharField(u"Code établissement de la situation année précédente OPI", max_length=8,
                                           null=True, db_column="COD_ETB_ANN_PRE_OPI")
    cod_dep_pay_ann_pre_opi = models.CharField(u"Code Département ou Pays de la situation de lannée précédente OPI",
                                               max_length=3, null=True, db_column="COD_DEP_PAY_ANN_PRE_OPI")
    cod_typ_dep_pay_ann_pre_opi = models.CharField(
        u"Type Département ou Pays de la situation de l année précédente OPI",
        max_length=1, null=True, db_column="COD_TYP_DEP_PAY_ANN_PRE_OPI")
    cod_tds_opi = models.CharField(u"Code type diplôme SISE du dernier diplôme obtenu", max_length=1,
                                   null=True, db_column="COD_TDS_OPI")
    cod_etb_der_dip = models.CharField(u"Code établissement où le dernier diplôme a été obtenu", max_length=8,
                                       null=True, db_column="COD_ETB_DER_DIP")
    daa_etb_der_dip = models.CharField(u"Année universitaire où le dernier diplôme a été obtenu", max_length=9,
                                       null=True, db_column="DAA_ETB_DER_DIP")
    cod_tpe_ann_crt = models.CharField(u"Code du type de l autre établissement fréquenté pour l année en cours OPI",
                                       max_length=2, null=True, db_column="COD_TPE_ANN_CRT")
    cod_etb_ann_crt = models.CharField(u"Code de l autre établissement fréquenté pour l année en cours OPI",
                                       max_length=8, null=True, db_column="COD_ETB_ANN_CRT")
    daa_etr_sup = models.CharField(u"Témoin d inscription parallèle dans l autre établissement pour l année en cours",
                                   max_length=9, null=True, db_column="DAA_ETR_SUP")
    cod_tde_der_dip = models.CharField(u"Code du type de dernier diplome", max_length=3, null=True,
                                       db_column="COD_TDE_DER_DIP")
    cod_dep_pay_der_dip = models.CharField(u"Code pays ou departement du dernier diplome obtenu", max_length=3,
                                           null=True, db_column="COD_DEP_PAY_DER_DIP")
    cod_typ_dep_pay_der_dip = models.CharField(u"Code du type du pays ou departement du dernier diplome obtenu",
                                               max_length=1, null=True, db_column="COD_TYP_DEP_PAY_DER_DIP")
    nb_enf_etu_opi = models.IntegerField(u"Nombre d'enfant de l'étudiant", null=True, db_column="NB_ENF_ETU_OPI")
    cod_pcs_ap = models.CharField(u"Code categorie socio-professionnelle autre parent", max_length=2,
                                  default='99', null=True, db_column="COD_PCS_AP")

    class Meta:
        db_table = u'IND_OPI'
        managed = False
        app_label = 'apogee'


class OpiBac(models.Model):
    cod_ind_opi = models.IntegerField(primary_key=True, db_column="COD_IND_OPI")
    cod_bac = models.CharField(u"(COPIED)Code Baccalaureat ou Equivalence", max_length=4, null=True,
                               db_column="COD_BAC")
    cod_etb = models.CharField(u"(COPIED)Code National de l'Etablissement", max_length=8, null=True,
                               db_column="COD_ETB")
    cod_tpe = models.CharField(u"(COPIED)Code Type Etablissement", max_length=2, null=True, db_column="COD_TPE")
    cod_dep = models.CharField(u"COPIED)Code Departement", max_length=3, null=True, db_column="COD_DEP")
    cod_mnb = models.CharField(u"(COPIED)Code Mention Niveau Bac", max_length=2, null=True, db_column="COD_MNB")
    daa_obt_bac_oba = models.CharField(u"Annee de la date d'obtention du bac", max_length=4, null=True,
                                       db_column="DAA_OBT_BAC_OBA")

    class Meta:
        db_table = u"OPI_BAC"
        managed = False
        app_label = 'apogee'


class AdresseOpi(models.Model):
    """
    Classe pour l'adresse pour OPI.
    Attention :
    contrairement au code, la clé primaire est composite et est sur
    cod_ind_opi et cod_typ_adr_opi.
    """
    cod_ind_opi = models.IntegerField(primary_key=True, db_column="COD_IND_OPI")
    cod_typ_adr_opi = models.CharField(u"Type de l'adresse OPI", max_length=1, null=True, db_column="COD_TYP_ADR_OPI")
    cod_pay = models.CharField(u"Code Pays INSEE", max_length=3, null=True, db_column="COD_PAY")
    cod_bdi = models.CharField(u"Code Bureau Distributeur", max_length=5, null=True, db_column="COD_BDI")
    cod_com = models.CharField(u"Code Commune", max_length=5, null=True, db_column="COD_COM")
    lib_ad1 = models.CharField(u"Libellé adresse 1", max_length=32, null=True, db_column="LIB_AD1")
    lib_ad2 = models.CharField(u"Libellé adresse 1", max_length=32, null=True, db_column="LIB_AD2")
    lib_ad3 = models.CharField(u"Libellé adresse 1", max_length=32, null=True, db_column="LIB_AD3")
    lib_ade = models.CharField(u"Libellé adresse 1", max_length=32, null=True, db_column="LIB_ADE")

    class Meta:
        db_table = u"ADRESSE_OPI"
        managed = False
        app_label = 'apogee'


class Individu(models.Model):
    cod_ind = models.IntegerField(u"Code Etudiant au sein de l'Etablissement", primary_key=True, db_column="COD_IND")
    cod_ind_opi = models.IntegerField(IndOpi, db_column="COD_IND_OPI", null=True)
    dat_cre_ind = models.DateTimeField(u"Date de création de l'individu", db_column="DAT_CRE_IND", null=True)
    dat_mod_ind = models.DateTimeField(u"Date de modification de l'individu", db_column="DAT_MOD_IND", null=True)
    date_nai_ind = models.DateTimeField(u"Date de naissance de l'individu", db_column="DATE_NAI_IND", null=True)
    lib_nom_pat_ind = models.CharField(u"Nom Patronymique Etudiant", max_length=30, null=True,
                                       db_column="LIB_NOM_PAT_IND")
    lib_nom_usu_ind = models.CharField(u"Nom Usuel Etudiant", max_length=30, null=True, db_column="LIB_NOM_USU_IND")
    lib_pr1_ind = models.CharField(u"Prenom 1 de l'Etudiant", max_length=20, null=True, db_column="LIB_PR1_IND")
    lib_pr2_ind = models.CharField(u"Prenom 2 de l'Etudiant", max_length=20, null=True, db_column="LIB_PR2_IND")
    lib_pr3_ind = models.CharField(u"Prenom 3 de l'Etudiant", max_length=20, null=True, db_column="LIB_PR3_IND")
    cod_etu = models.IntegerField(u"Code Etudiant", db_column="COD_ETU", null=True)
    cod_sex_etu = models.CharField(u"Code Sexe de l'Etudiant", max_length=1, null=True, db_column="COD_SEX_ETU")
    cod_fam = models.CharField(u"Code famiale", max_length=1, null=True, db_column="COD_FAM")
    cod_nne_ind = models.CharField(u"Identifiant National de l'étudiant",
                                   max_length=10, null=True, db_column="COD_NNE_IND")
    cod_cle_nne_ind = models.CharField(u"Cle de l'identifiant national etudiant", max_length=1, null=True,
                                       db_column="COD_CLE_NNE_IND")

    def ine(self):
        return u"%s%s" % (self.cod_nne_ind, self.cod_cle_nne_ind)

    def __unicode__(self):
        return u"%s %s %s" % (self.lib_nom_pat_ind, self.lib_pr1_ind, self.cod_etu)

    class Meta:
        db_table = "INDIVIDU"
        verbose_name = u"étudiant"
        app_label = 'apogee'

    def identite(self):
        return u"%s %s %s" % (self.lib_nom_pat_ind, self.lib_nom_usu_ind, self.lib_pr1_ind)
    identite.short_description = u"identité"

    def get_adresse_annuelle(self, annee):
        adresse_annuelle = self.adresse_annuelle.filter(cod_anu_ina=annee)
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

    def get_adresse(self, annee):

        adresse_annuelle = self.adresse_annuelle.filter(cod_anu_ina=annee)
        if adresse_annuelle:
            return adresse_annuelle[0].get_str()
        else:
            return self.adresse_fixe.all()[0].get_str()

    def get_code_postal(self, annee):
        adresse_annuelle = self.adresse_annuelle.filter(cod_anu_ina=annee)
        if adresse_annuelle:
            return adresse_annuelle[0].COD_BDI or adresse_annuelle[0].LIB_ADE
        else:
            return self.adresse_fixe.all()[0].COD_BDI or self.adresse_fixe.all()[0].LIB_ADE

    def get_pays(self, annee):
        adresse_annuelle = self.adresse_annuelle.filter(COD_ANU_INA=annee)
        if adresse_annuelle:
            return adresse_annuelle[0].COD_PAY.lib_pay
        else:
            return self.adresse_fixe.all()[0].COD_PAY.lib_pay

    def get_full_adresse(self, annee):
        try:
            adresse_annuelle = self.adresse_annuelle.filter(COD_ANU_INA=annee)
            if adresse_annuelle:
                return adresse_annuelle[0].__unicode__()
            else:
                return self.adresse_fixe.all()[0].__unicode__()
        except IndexError:
            return u""

    def get_adresse_html(self, annee):
        try:
            adresse_annuelle = self.adresse_annuelle.filter(COD_ANU_INA=self)
            if adresse_annuelle:
                return adresse_annuelle[0].html()
            else:
                return self.adresse_fixe.all()[0].html()
        except IndexError:
            return u""

    get_full_adresse.short_description = 'Adresse'

    def get_dico_adresse(self, annee):
        adresse_annuelle = self.adresse_annuelle.filter(COD_ANU_INA=annee)
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


class ADRESSE(models.Model):
    cod_adr = models.IntegerField(u"Code adresse", primary_key=True, db_column="COD_ADR")

    cod_ind = models.ForeignKey(Individu, db_column="COD_IND", null=True, related_name="adresse_fixe")
    cod_anu_ina = models.CharField(u"Code Annee Universitaire pour adresse", max_length=4, null=True,
                                   db_column="COD_ANU_INA")
    cod_ind_ina = models.ForeignKey(Individu, verbose_name=u"Code individu pour adresse annuelle", null=True,
                                    db_column="COD_IND_INA", related_name="adresse_annuelle")

    cod_pay = models.ForeignKey(Pays, verbose_name=u"Code Pays INSEE", null=True, db_column="COD_PAY")
    cod_bdi = models.CharField(u"Code Bureau Distributeur", max_length=5, null=True, db_column="COD_BDI")
    cod_com = models.CharField(u"Code Commune", max_length=5, null=True, db_column="COD_COM")
    lib_ad1 = models.CharField(u"Libellé adresse 1", max_length=32, null=True, db_column="LIB_AD1")
    lib_ad2 = models.CharField(u"Libellé adresse 2", max_length=32, null=True, db_column="LIB_AD2")
    lib_ad3 = models.CharField(u"Libellé adresse 3", max_length=32, null=True, db_column="LIB_AD3")
    lib_ade = models.CharField(u"Libellé adresse étrangère", max_length=32, null=True, db_column="LIB_ADE")
    num_tel = models.CharField(u"Numéro de téléphone", max_length=15, null=True, db_column="NUM_TEL")
    num_tel_port = models.CharField(u"Numéro de téléphone portable de l'étudiant", max_length=15, null=True,
                                    db_column="NUM_TEL_PORT")
    adr_mail = models.CharField(u"Adresse Mail personnelle de l'étudiant", max_length=200, null=True,
                                db_column="ADR_MAIL")

    def get_str(self):
        if self.COD_COM and self.COD_BDI:
            lib_ach = ComBdi.objects.get(cod_com=self.cod_com, cod_bdi=self.cod_bdi).lib_ach
        else:
            lib_ach = ""
        if self.COD_IND:
            nom = u"%s %s" % (self.cod_ind.lib_nom_pat_ind, self.cod_ind.lib_nom_usu_ind)
            prenom = self.cod_ind.lib_pr1_ind
        else:
            nom = u"%s %s" % (self.cod_ind_ina.lib_nom_pat_ind, self.cod_ind_ina.lib_nom_usu_ind)
            prenom = self.cod_ind_ina.lib_pr1_ind

        return [nom, prenom, self.lib_ad1, self.lib_ad2, self.lib_ad3, self.cod_bdi, lib_ach, self.lib_ade,
                self.cod_pay.lib_pay]

    def get_dico(self):
        if self.cod_com and self.cod_bdi:
            lib_ach = ComBdi.objects.get(cod_com=self.cod_com, cod_bdi=self.cod_bdi).lib_ach
        else:
            lib_ach = ""

        return {'lib_ad1': self.lib_ad1,
                'lib_ad2': self.lib_ad2,
                'lib_ad3': self.lib_ad3,
                'cod_bdi': self.cod_bdi,
                'cod_com': self.cod_com,
                'lib_ach': lib_ach,
                'lib_ade': self.lib_ade,
                'lib_pay': self.cod_pay.lib_pay,
                'cod_pay': self.cod_pay.cod_pay}

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


class InsAdmAnu(models.Model):
    cod_anu = models.CharField(u"Code Annee Universitaire", max_length=4, db_column="COD_ANU", primary_key=True)
    cod_ind = models.ForeignKey(Individu, db_column='COD_IND',
                                related_name="inscription_annuelle")
    cod_rgi = models.CharField(u"Code régime inscription", max_length=1, null=True, db_column="COD_RGI")
    cod_stu = models.CharField(u"Statut de l'étudiant", max_length=2, null=True, db_column="COD_STU")

    class Meta:
        db_table = u"INS_ADM_ANU"
        verbose_name = u"Etape annuelle d'un étudiant"
        verbose_name_plural = u"Etapes annuelles des étudiants"
        app_label = 'apogee'


class InsAdmAnuCopy(models.Model):
    id = models.CharField(primary_key=True, max_length=26)
    cod_anu = models.ForeignKey(AnneeUni, verbose_name=u"Code Annee Universitaire")
    cod_ind = models.ForeignKey(Individu, db_column='COD_IND', related_name="etapes_ied")
    cod_etp = models.CharField(u"Code Etape", max_length=8, null=True,
                               db_column="COD_ETP")
    cod_vrs_vet = models.CharField(u"(COPIED)Numero Version Etape", max_length=3, db_column="COD_VRS_VET")
    num_occ_iae = models.CharField(u"", max_length=2, null=True, db_column="NUM_OCC_IAE")
    cod_dip = models.CharField(u"(COPIED)Code Diplome Etablissement", max_length=7, null=True, db_column="COD_DIP")
    cod_cge = models.CharField(u"(COPIED)Code Centre de Gestion", max_length=3, null=True, db_column="COD_CGE")
    dat_cre_iae = models.DateTimeField(u"Date de création de l'IAE", null=True, db_column="DAT_CRE_IAE")
    dat_mod_iae = models.DateTimeField(u"Date de modification de l'IAE", null=True, db_column="DAT_MOD_IAE")
    nbr_ins_cyc = models.IntegerField(u'Nombre d\'Inscriptions dans le Cycle', null=True, db_column="NBR_INS_CYC")
    nbr_ins_etp = models.IntegerField(u"Nombre d'Inscriptions dans l'Etape", null=True, db_column="NBR_INS_ETP")
    dat_annul_res_iae = models.DateTimeField(u"Date annulation ou résiliation IA", null=True,
                                             db_column="DAT_ANNUL_RES_IAE")
    tem_iae_prm = models.CharField(u"Temoin Etape Premiere ou Seconde", max_length=1, null=True,
                                   db_column="TEM_IAE_PRM")
    nbr_ins_dip = models.IntegerField(u"Nombre d'Inscriptions dans le DIP", null=True, db_column="NBR_INS_DIP")
    eta_iae = models.CharField(u"etat de l'inscription", null=True, max_length=1, db_column='ETA_IAE')
    eta_pmt_iae = models.CharField(u"Etat des paiements des droits", null=True, max_length=1, db_column="ETA_PMT_IAE")
    cod_pru = models.CharField(u"Code profil étudiant", null=True, max_length=2, db_column="COD_PRU")

    objects = models.Manager()
    inscrits = EtapeNonCondiValideManager()
    inscrits_condi = EtapeCondiValideManager()

    class Meta:
        db_table = u"INS_ADM_ETP_IED"
        verbose_name = u"Etape"
        verbose_name_plural = u"etapes de l'étudiant"
        app_label = 'apogee'


    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.pk:
            self.pk = str(self.cod_anu_id) + str(self.COD_IND_id) + str(self.COD_ETP) + str(self.COD_VRS_VET) \
                      + str(self.NUM_OCC_IAE)
        if not self.step:
            step_id = StepApogee.objects.using("default").get(annee__cod_anu=self.COD_ANU, name=self.COD_ETP).id
            self.step_id = step_id

        return super(InsAdmAnuCopy, self).save(force_insert=force_insert, force_update=force_update,
                                                     using=using, update_fields=update_fields)

    def cod_opi(self):
        return u"%s" % self.COD_IND.COD_IND_OPI

    cod_opi.short_description = u"Code opi"

    def is_reins(self):
        if self.NBR_INS_ETP == 1:
            return False
        else:
            return True


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
    cod_anu = models.CharField(u"Code Annee Universitaire", max_length=4, db_column="COD_ANU")
    cod_ind = models.ForeignKey(INDIVIDU, db_column='COD_IND', primary_key=True, related_name="etapes")
    cod_etp = models.CharField(u"(COPIED)(COPIED)Code Etape", max_length=6, null=True, db_column="COD_ETP")
    cod_vrs_vet = models.CharField(u"(COPIED)Numero Version Etape", max_length=3, null=True, db_column="COD_VRS_VET")
    num_occ_iae = models.CharField(u"", max_length=2, null=True, db_column="NUM_OCC_IAE")
    cod_dip = models.CharField(u"(COPIED)Code Diplome Etablissement", max_length=7, null=True, db_column="COD_DIP")
    cod_cge = models.CharField(u"(COPIED)Code Centre de Gestion", max_length=3, null=True, db_column="COD_CGE")
    dat_cre_iae = models.DateTimeField(u"Date de création de l'IAE", null=True, db_column="DAT_CRE_IAE")
    dat_mod_iae = models.DateTimeField(u"Date de modification de l'IAE", null=True, db_column="DAT_MOD_IAE")
    nbr_ins_cyc = models.IntegerField(u'Nombre d\'Inscriptions dans le Cycle', null=True, db_column="NBR_INS_CYC")
    nbr_ins_etp = models.IntegerField(u"Nombre d'Inscriptions dans l'Etape", null=True, db_column="NBR_INS_ETP")
    dat_annul_res_iae = models.DateTimeField(u"Date annulation ou résiliation IA", null=True,
                                             db_column="DAT_ANNUL_RES_IAE")
    tem_iae_prm = models.CharField(u"Temoin Etape Premiere ou Seconde", max_length=1, null=True,
                                   db_column="TEM_IAE_PRM")
    nbr_ins_dip = models.IntegerField(u"Nombre d'Inscriptions dans le DIP", null=True, db_column="NBR_INS_DIP")
    eta_iae = models.CharField(u"etat de l'inscription", null=True, max_length=1, db_column='ETA_IAE')
    eta_pmt_iae = models.CharField(u"Etat des paiements des droits", null=True, max_length=1, db_column="ETA_PMT_IAE")
    cod_pru = models.CharField(u"Code profil étudiant", null=True, max_length=2, db_column="COD_PRU")
    inscrits = EtapeNonCondiValideManagerOracle()
    inscrits_condi = EtapeCondiValideManagerOracle()

    objects = models.Manager()

    class Meta:
        db_table = u"INS_ADM_ETP"
        app_label = 'apogee'

    def save_copy(self, using='default'):
        ins = InsAdmAnuCopy()
        ins.cod_anu_id = self.COD_ANU
        ins.cod_ind = self.COD_IND
        ins.cod_etp = self.COD_ETP
        ins.cod_vrs_vet = self.COD_VRS_VET
        ins.num_occ_iae = self.NUM_OCC_IAE
        ins.cod_dip = self.COD_DIP
        ins.cod_cge = self.COD_CGE
        ins.eta_iae = self.ETA_IAE
        ins.dat_cre_iae = self.DAT_CRE_IAE
        ins.dat_mod_iae = self.DAT_MOD_IAE
        ins.nbr_ins_cyc = self.NBR_INS_CYC
        ins.nbr_ins_etp = self.NBR_INS_ETP
        ins.dat_annul_res_iae = self.DAT_ANNUL_RES_IAE
        ins.tem_iae_prm = self.TEM_IAE_PRM
        ins.nbr_ins_dip = self.NBR_INS_DIP
        ins.eta_pmt_iae = self.ETA_PMT_IAE
        ins.cod_pru = self.COD_PRU

        ins.save(using=using)
        if not hasattr(ins, 'remontee'):
            Remontee.objects.create(etape=ins)
