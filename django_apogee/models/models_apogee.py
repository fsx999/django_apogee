# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

__author__ = 'paul'
import re
from django.db import models


@python_2_unicode_compatible
class AnneeUni(models.Model):
    cod_anu = models.CharField(u'Année', max_length=4, primary_key=True, db_column='COD_ANU')
    eta_anu_iae = models.CharField(u"Etat ouverture année", max_length=1, choices=(
        ('F', u"Fermé"),
        ('O', 'Ouvert')), db_column='ETA_ANU_IAE')

    def __str__(self):
        return str(self.cod_anu)

    class Meta:
        db_table = 'ANNEE_UNI'
        ordering = ['-cod_anu']
        app_label = 'django_apogee'


@python_2_unicode_compatible
class Pays(models.Model):
    cod_pay = models.CharField(max_length=3, primary_key=True, db_column='COD_PAY')
    cod_sis_pay = models.CharField(max_length=3, db_column='COD_SIS_PAY')
    lib_pay = models.CharField(max_length=50, db_column='LIB_PAY')
    lic_pay = models.CharField(max_length=20, db_column='LIC_PAY')
    lib_nat = models.CharField(max_length=50, db_column='LIB_NAT')
    tem_ouv_drt_sso_pay = models.CharField(max_length=1, db_column='TEM_OUV_DRT_SSO_PAY')
    tem_en_sve_pay = models.CharField(max_length=1, db_column='TEM_EN_SVE_PAY')
    tem_del = models.CharField(max_length=1, db_column='TEM_DEL')
    tem_afl_dec_ind_pay = models.CharField(max_length=1, db_column='TEM_AFL_DEC_IND_PAY')

    class Meta:
        db_table = u'PAYS'
        ordering = ['lic_pay']
        app_label = 'django_apogee'

    def __str__(self):
        return self.lib_pay


@python_2_unicode_compatible
class Departement(models.Model):
    cod_dep = models.CharField(max_length=3, primary_key=True)
    cod_acd = models.IntegerField()
    lib_dep = models.CharField(max_length=60)
    lic_dep = models.CharField(max_length=20)
    tem_en_sve_dep = models.CharField(max_length=1)

    class Meta:
        db_table = u'DEPARTEMENT'
        ordering = ['lib_dep']
        app_label = 'django_apogee'

    def __str__(self):
        return self.lib_dep


@python_2_unicode_compatible
class SitFam(models.Model):
    """
    Les status familiales
    """
    cod_fam = models.CharField(max_length=1, primary_key=True)
    cod_sis_fam = models.CharField(max_length=1, null=True, blank=True)
    lib_fam = models.CharField(max_length=40)
    lic_fam = models.CharField(max_length=10)
    tem_en_sve_fam = models.CharField(max_length=1, choices=(('O', 'O'), ('N', 'N')))
    
    def __str__(self):
        return u"%s" % self.lib_fam

    class Meta:
        db_table = u'pal_family_status'
        app_label = 'django_apogee'


@python_2_unicode_compatible
class TypHandicap(models.Model):
    """Type d'handicap de l'étudiant
    """
    cod_thp = models.CharField(u"code type handicap", max_length=2,
                               primary_key=True)
    lib_thp = models.CharField(u"libelle long", max_length=50)
    lic_thp = models.CharField(u"lielle court", max_length=20)
    tem_tie_tps = models.CharField(u"temoin handicap permet tiers temps",
                                   max_length=1, choices=(('O', 'O'), ('N', 'N')), default='O')
    tem_en_sve_thp = models.CharField(u"temoin en service", max_length=1,
                                      choices=(('O', 'O'), ('N', 'N')), default='O')

    def __str__(self):
        return self.lib_thp

    class Meta:
        db_table = u"TYP_HANDICAP"
        app_label = 'django_apogee'


class SituationMilitaire(models.Model):
    """Situation Militair de l'étudiant
    """
    cod_sim = models.CharField(u"Code Situation militaire",
                               max_length=1, primary_key=True)
    lib_sim = models.CharField(u"Libelle Long Situation Militaire",
                               max_length=50)
    lic_sim = models.CharField(u"lib court", max_length=20)
    tem_sai_dmm_lbt = models.CharField(
        u"temoin permettant une saisie coherente code situation militaire",
        max_length=1, choices=(('O', 'O'), ('N', 'N')), default='O')
    tem_en_sve_sim = models.CharField(u"temoin en service", max_length=1,
                                      choices=(('O', 'O'), ('N', 'N')), default='O')
    tem_del_dip = models.CharField(u"Temoin de délivrance du diplome",
                                   max_length=1, choices=(('O', 'O'), ('N', 'N')), default='N')

    def __str__(self):
        return self.lib_sim

    class Meta:
        db_table = u"situation_militaire"
        app_label = 'django_apogee'


class ComBdi(models.Model):
    """

    """
    cod_bdi = models.CharField(max_length=6, primary_key=True)
    cod_com = models.CharField(max_length=6)
    lib_ach = models.CharField(max_length=26)
    eta_ptc_loc = models.CharField(max_length=3)
    eta_ptc_ach = models.CharField(max_length=3)
    tem_en_sve_cbd = models.CharField(max_length=3)
    cod_fic_cbd = models.CharField(max_length=3)

    def __str__(self):
        return "%s %s" % (self.cod_bdi, self.lib_ach)

    class Meta:
        db_table = 'COM_BDI'
        managed = False
        ordering = ['lib_ach']
        app_label = 'django_apogee'


class ComBdiCopie(models.Model):
    """

    """
    id = models.CharField(max_length=12, primary_key=True)
    cod_bdi = models.CharField(max_length=6)
    cod_com = models.CharField(max_length=6)
    lib_ach = models.CharField(max_length=26)
    eta_ptc_loc = models.CharField(max_length=3)
    eta_ptc_ach = models.CharField(max_length=3)
    tem_en_sve_cbd = models.CharField(max_length=3)
    cod_fic_cbd = models.CharField(max_length=3)

    def __str__(self):
        return "%s %s" % (self.cod_bdi, self.lib_ach)

    class Meta:
        db_table = u'apogee_com_bdi'
        #managed= False
        ordering = ['lib_ach']
        app_label = 'django_apogee'


class TypeHebergement(models.Model):
    cod_thb = models.CharField("code type hébergement", max_length=1,
                               primary_key=True)
    lib_thb = models.CharField("libelle long type hébergement", max_length=60)
    tem_en_sve_thb = models.CharField("temoin en service", max_length=1,
                                      default='O', choices=(('O', 'O'),
                                                            ('N', 'N')))

    def __str__(self):
        return self.lib_thb

    class Meta:
        db_table = u"typ_hebergement"
        app_label = 'django_apogee'


class BacOuxEqui(models.Model):
    CHOICES = (
        ('O', 'O'),
        ('N', 'N'),)
    cod_bac = models.CharField(
        "Code Baccalaureat ou Equivalence",
        max_length=4)
    cod_sis_bac = models.CharField(
        "Code SISE Baccalaureat ou Equivalence",
        max_length=4)
    lib_bac = models.CharField(
        "Libelle Long Baccalaureat ou Equivalence",
        max_length=80)
    lic_bac = models.CharField("Libelle Court Baccalaureat ou Equivalence",
                               max_length=20)
    tem_etb = models.CharField(
        "Temoin Existence ou Suivi Etablissementd'Origine",
        max_length=1, choices=CHOICES, default='O')
    tem_mnb = models.CharField(
        'Temoin Existence ou Suivi Mention Niveau Bac Obtenue',
        max_length=1, choices=CHOICES, default='O')
    tem_nat_bac = models.CharField('Temoin Nature de Bac',
                                   max_length=1, choices=CHOICES, default='O')
    tem_obt_tit_etb_sec = models.CharField(
        'Temoin Preparation Bac Etablissement Secondaire',
        max_length=1, choices=CHOICES, default='O')
    tem_en_sve_bac = models.CharField('Temoin en Service',
                                      max_length=1, choices=CHOICES, default='O')
    tem_deb = models.CharField('Temoin Departement du Bac',
                               max_length=1, choices=CHOICES, default='O')
    tem_del = models.CharField("Temoin d'Autorisation de Mise Hors Service",
                               max_length=1, choices=CHOICES, default='O')
    daa_deb_vld_bac = models.CharField(
        "Annee de debut de periode de validite du baccalaureat",
        max_length=8, null=True, default=None)
    daa_fin_vld_bac = models.CharField(
        'Annee de fin de periode de validite du baccalaureat',
        max_length=8, null=True, default=None)
    tem_type_equi = models.CharField(
        'Temoin precisant si la serie de bac est une equivalence',
        max_length=1, choices=CHOICES, default='N')
    cod_sis = models.CharField(
        "Code de la situation de l'annee precedente unique",
        max_length=1, null=True)
    cod_tds = models.CharField("Code du type de dernier diplome obtenu unique",
                               max_length=1, null=True)

    def __str__(self):
        return re.sub(r'([0-9]{4}-)', '', self.lib_bac).title()

    class Meta:
        db_table = u'pal_apogee_bac_oux_equi'
        app_label = 'django_apogee'


class MentionBac(models.Model):
    """Mention Bac
    """
    cod_mnb = models.CharField("code mention niveau bac", max_length=2,
                               primary_key=True)
    lib_mnb = models.CharField("libelle long", max_length=50)
    lic_mnb = models.CharField("libelle court", max_length=20)
    tem_en_sve_mnb = models.CharField("temoin code en service", max_length=1,
                                      choices=(('O', 'O'), ('N', 'N')), default='O')

    def __str__(self):
        return self.lib_mnb

    class Meta:
        db_table = u"mention_niv_bac"
        app_label = 'django_apogee'


class TypeEtablissement(models.Model):
    """Type établissement
    """
    cod_tpe = models.CharField("code type etablissement",
                               max_length=2, primary_key=True)
    cod_sis_tpe = models.CharField(
        "Correspondance Code SISE type établissement",
        max_length=2, null=True)
    lib_tpe = models.CharField("libelle long", max_length=50)
    lic_tpe = models.CharField("libelle court", max_length=20)

    tem_det_tpe = models.CharField(
        "temoin detail possibl sur ce type d'etablissement", max_length=1,
        choices=(('O', 'O'), ('N', 'N')), default='O')
    tem_en_sve_tpe = models.CharField("temoin code en service",
                                      max_length=1, choices=(('O', 'O'), ('N', 'N')), default='O')
    tem_ges_trf_tpe = models.CharField("temoin gestion des transfert",
                                       max_length=1, choices=(('O', 'O'), ('N', 'N')), default='O')
    tem_prop_autre_etb = models.CharField("temoin etablissement en cours",
                                          max_length=1, choices=(('O', 'O'), ('N', 'N')), default='N')

    class Meta:
        db_table = u"typ_etb"
        app_label = 'django_apogee'

    def __str__(self):
        return self.lib_tpe


class Etablissement(models.Model):
    cod_etb = models.CharField("code", max_length=8, primary_key=True)
    cod_tpe = models.ForeignKey(TypeEtablissement, db_column='cod_tpe')
    cod_dep = models.ForeignKey(Departement, db_column='cod_dep')
    lib_etb = models.CharField("libelle long", max_length=50)
    cod_pos_adr_etb = models.CharField("Code postal", max_length=20, null=True, default=None)
    tem_en_sve_etb = models.CharField("temoin en service", max_length=1,
                                      default='O', choices=(('O', 'O'), ('N', 'N')))
    tem_aut_sis_etb = models.CharField("temoin en service", max_length=1,
                                       default='O', choices=(('O', 'O'), ('N', 'N')))
    cod_aff_dep_etb = models.CharField("code", max_length=3, null=True)

    cod_aff_etb = models.CharField("code", max_length=3, null=True)

    lib_off_etb = models.CharField("libelle officiel", max_length=60)
    lib_art_off_etb = models.CharField(
        "article defini precedant le nom officiel",
        max_length=5)
    cod_pay_adr_etb = models.ForeignKey(Pays, null=True,
                                        db_column='cod_pay_adr_etb')

    def __str__(self):
        if self.cod_tpe_id == '10':
            return unicode(self.lib_etb)
        else:
            return self.lib_off_etb

    def get_type(self):
        if self.cod_pay_adr_etb and self.cod_pay_adr_etb.cod_pay != 100:
            return 'P'
        else:
            return 'D'

    def get_pays_dep(self):
        if self.cod_pay_adr_etb and self.cod_pay_adr_etb.cod_pay != 100:
            return self.cod_pay_adr_etb.cod_pay
        else:
            return self.cod_dep.cod_dep

    class Meta:
        db_table = u"etablissement"
        ordering = ['lib_etb']
        app_label = 'django_apogee'


class CatSocPfl(models.Model):
    cod_pcs = models.CharField("code", max_length=2, primary_key=True)
    lib_pcs = models.CharField("libelle long", max_length=50)
    tem_en_sve_pcs = models.CharField("temoin en service", max_length=1,
                                      default='O', choices=(('O', 'O'), ('N',
                                                                         'N')))
    lib_web_pcs = models.CharField("libelle long", max_length=120)
    tem_sai_qtr = models.CharField("temoin en service", max_length=1,
                                   default='O', choices=(('O', 'O'), ('N',
                                                                      'N')))

    def __str__(self):
        return self.lib_web_pcs

    class Meta:
        db_table = u"cat_soc_pfl"
        app_label = 'django_apogee'


class QuotiteTra(models.Model):
    cod_qtr = models.CharField("code", max_length=1, primary_key=True)
    lib_qtr = models.CharField("libelle long", max_length=50)
    lic_qtr = models.CharField("libelle court", max_length=50)
    lim1_qtr = models.CharField("libelle court", max_length=50)
    lib_web_qtr = models.CharField("libelle court", max_length=120)
    tem_en_sve_qtr = models.CharField(
        "temoin en service",
        max_length=1,
        default='O',
        choices=(('O', 'O'), ('N', 'N')))
    TEM_COU_AUT_REG_QTR = models.CharField(
        "couverture sécu",
        max_length=1,
        default='O',
        choices=(('O', 'O'), ('N', 'N')))

    def __str__(self):
        return self.lib_web_qtr

    class Meta:
        db_table = u"quotite_tra"
        app_label = 'django_apogee'


class DomaineActPfl(models.Model):
    cod_dap = models.CharField(max_length=2, primary_key=True, db_column="COD_DAP")
    lib_web_dap = models.CharField(max_length=120, db_column="LIB_WEB_DAP", null=True)

    def __str__(self):
        return self.lib_web_dap

    class Meta:
        db_table = u"DOMAINE_ACT_PFL"
        app_label = "apogee"


class SituationSise(models.Model):
    cod_sis = models.CharField("code", max_length=1, primary_key=True)
    lib_sis = models.CharField("libelle long", max_length=130)
    tem_en_sve_sis = models.CharField(
        "temoin en service",
        max_length=1,
        default='O',
        choices=(('O', 'O'), ('N', 'N')))

    def __str__(self):
        return self.lib_sis

    class Meta:
        db_table = u"situation_sise"
        app_label = 'django_apogee'


class TypeDiplomeExt(models.Model):
    cod_tde = models.CharField("code", max_length=3, primary_key=True)
    lib_web_tde = models.CharField("libelle long", max_length=130)
    lib_tde = models.CharField("libelle long", max_length=130)

    tem_en_sve_tde = models.CharField(
        "temoin en service",
        max_length=1,
        default='O',
        choices=(('O', 'O'), ('N', 'N')))

    def __str__(self):
        return self.lib_tde

    class Meta:
        db_table = u"typ_diplome_ext"
        app_label = 'django_apogee'


class RegimeSecuNonSecu(models.Model):
    """
    Il s'agit de tout les cas du dossier inscripiton qui dispense de la sécu
    """

    lib_rsns = models.CharField("libelle long", max_length=300)
    tem_affiliation_parent = models.CharField(
        "temoin en service",
        max_length=1,
        default='O',
        choices=(('O', 'O'), ('N', 'N')))

    def __str__(self):
        return self.lib_rsns

    class Meta:
        db_table = u"pal_apogee_regime_secu_non_secu"
        app_label = 'django_apogee'


class SitSociale(models.Model):
    cod_soc = models.CharField("code situation sociale", max_length=2, primary_key=True)
    lim1_soc = models.CharField("libelle long", max_length=35)

    class Meta:
        db_table = u'sit_sociale'
        app_label = 'django_apogee'

    def __str__(self):
        return unicode(self.lim1_soc)


class Bourse(models.Model):
    cod_brs = models.CharField("code situation sociale", max_length=2, primary_key=True)
    lim1_brs = models.CharField("libelle long", max_length=35)

    class Meta:
        db_table = u'bourse'
        app_label = 'django_apogee'


class Banque(models.Model):
    abr_ban = models.CharField(u"Abréviation de l'établissement bancaire", max_length=5, primary_key=True)
    cod_ban = models.CharField(u"Code de l'établissement bancaire", max_length=5, null=True)
    lib_ban = models.CharField(u"Libellé de l'établissement bancaire", max_length=35)

    class Meta:
        db_table = u'banque'
        ordering = ['lib_ban']
        app_label = 'django_apogee'

    def __str__(self):
        return unicode(self.lib_ban)


class Composante(models.Model):
    """
    Composante de la fac
    IED = 034
    """
    cod_cmp = models.CharField(u"code composante", max_length=3, db_column="COD_CMP", primary_key=True)
    cod_tpc = models.CharField(u"code type composante", max_length=3, null=True, db_column="COD_TPC")
    lib_cmp = models.CharField(u"libelle", max_length=40, null=True, db_column="LIB_CMP")

    def __str__(self):
        return u"%s %s" % (self.cod_cmp, self.lib_cmp)

    class Meta:
        app_label = 'django_apogee'
        db_table = "COMPOSANTE"


class CentreGestion(models.Model):
    """
    les centre de gestion : ceux sont les centres financiers à différencier des composantes.
    Une composante peut être un centre de gestion.
    """
    cod_cge = models.CharField(u"code centre de gestion", max_length=3, db_column="COD_CGE", primary_key=True)
    lib_cge = models.CharField(u"libellé", max_length=40, null=True, db_column="LIB_CGE")

    def __str__(self):
        return u"%s %s" % (self.cod_cge, self.lib_cge)

    class Meta:
        app_label = "apogee"
        db_table = "CENTRE_GESTION"


class Etape(models.Model):
    cod_etp = models.CharField(u"Code etape", max_length=6, db_column="COD_ETP", primary_key=True)
    cod_cyc = models.CharField(u"code sise", max_length=1, null=True, db_column="COD_CYC")
    cod_cur = models.CharField(u"cursus lmd", max_length=1, null=True, db_column="COD_CUR")
    lib_etp = models.CharField(u"label", max_length=60, null=True, db_column="LIB_ETP")

    def __str__(self):
        return u"%s" % self.lib_etp

    class Meta:
        app_label = 'django_apogee'
        verbose_name = "Etape d'un cursus"
        verbose_name_plural = "Etapes d'un cursus"
        db_table = "ETAPE"


class EtpGererCge(models.Model):
    cod_etp = models.ForeignKey(Etape, verbose_name=u"code etape", db_column="COD_ETP", primary_key=True)
    cod_cge = models.ForeignKey(CentreGestion, verbose_name=u"code centre gestion",
                                db_column="cod_cge", related_name="etape_centre_gestion")
    cod_cmp = models.ForeignKey(Composante, verbose_name=u"code composante", db_column='COD_CMP')

    def __str__(self):
        return u"%s" % self.cod_etp

    class Meta:
        app_label = 'django_apogee'
        db_table = 'ETP_GERER_CGE'


