# coding=utf-8
"""Le Module d'accès aux OPI.

.. warning::

  Toutes les tables ci dessous doivent être en accès direct sur apogée.
  De multiples clés composite se balade un peu partout.

"""
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models


@python_2_unicode_compatible
class IndOpi(models.Model):
    """
    Table opi pour l'individu.
    Cette classe permet d'insérer les individus d'une application externe vers apogée via OPI.
    L'ensemble des tables ne doivent jamais être créés car les models contiennent le nécessaire pour l'envoie de données
    dans apogée ainsi que la lecture, mais il n'y a pas le nécessaire pour la création de la table et la liaison des
    données vers d'autres modèles (clè primaire composite.
    """
    cod_ind_opi = models.IntegerField(u"Code Dossier OPI", primary_key=True, db_column='COD_IND_OPI')
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

    def __str__(self):
        return self.cod_ind_opi

    class Meta:
        db_table = u'IND_OPI'
        managed = False
        app_label = 'django_apoge'


@python_2_unicode_compatible
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

    def __str__(self):
        return self.cod_ind_opi

    class Meta:
        db_table = u"OPI_BAC"
        managed = False
        app_label = 'django_apoge'


@python_2_unicode_compatible
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

    def __str__(self):
        return self.cod_ind_opi

    class Meta:
        db_table = u"ADRESSE_OPI"
        managed = False
        app_label = 'django_apoge'
