# coding=utf-8
"""
Module d'info sur les étudiants.
"""
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django_apogee.managers import EtapeNonCondiValideManager, EtapeNonCondiValideManagerOracle, \
    EtapeCondiValideManagerOracle
from django_apogee.managers import EtapeCondiValideManager
from django_apogee import utils

__author__ = 'paul'

from django_apogee.models import AnneeUni, ComBdi, Pays, CompositeImplementation, CompositeInitial
from django.db import models, connection, connections, DatabaseError


@python_2_unicode_compatible
class Individu(models.Model):
    cod_ind = models.IntegerField(u"Code Etudiant au sein de l'Etablissement", primary_key=True, db_column="COD_IND")
    cod_thp = models.CharField(u"code type handicap", max_length=2, null=True, db_column="COD_THP")
    cod_fam = models.CharField(u"code situation familiale", max_length=1, null=True, db_column="COD_FAM")
    cod_sim = models.CharField(u"code situation militaire", max_length=1, null=True, db_column="COD_SIM")
    cod_pay_nat = models.CharField(u"code pays insee nationalie", max_length=3, null=True, db_column="COD_PAY_NAT")
    cod_etb = models.CharField(u"code notional de l'etablissement premiere inscription", max_length=8, null=True,
                               db_column="COD_ETB")
    cod_uti = models.CharField(u"code utilisateur de creation de l'individu", max_length=30, null=True,
                               db_column="COD_UTI")
    cod_ind_opi = models.IntegerField('cod_opi', db_column="COD_IND_OPI", null=True)
    cod_nne_ind = models.CharField(u"Identifiant National de l'étudiant",
                                   max_length=10, null=True, db_column="COD_NNE_IND")
    cod_cle_nne_ind = models.CharField(u"Cle de l'identifiant national etudiant", max_length=1, null=True,
                                       db_column="COD_CLE_NNE_IND")
    dat_cre_ind = models.DateTimeField(u"Date de création de l'individu", db_column="DAT_CRE_IND", null=True)
    dat_mod_ind = models.DateTimeField(u"Date de modification de l'individu", db_column="DAT_MOD_IND", null=True)
    date_nai_ind = models.DateTimeField(u"Date de naissance de l'individu", db_column="DATE_NAI_IND", null=True)
    tem_date_nai_rel = models.CharField(u"temoin date estime", max_length=1, null=True, default="O",
                                        db_column="TEM_DATE_NAI_REL")
    daa_lbt_ind = models.CharField(u"annee liberation etudiant sous les drapaux", max_length=4, null=True,
                                   db_column="DAA_LBT_IND")
    dmm_lbt_ind = models.CharField(u"mois de liberation etudiant sous les drapaux", max_length=2, null=True,
                                   db_column="DMM_LBT_IND")
    daa_ent_etb = models.CharField(u"annee premiere inscription universite francaise", max_length=4, null=True,
                                   db_column="DAA_ENT_ETB")

    lib_nom_pat_ind = models.CharField(u"Nom Patronymique Etudiant", max_length=30, null=True,
                                       db_column="LIB_NOM_PAT_IND")
    lib_nom_usu_ind = models.CharField(u"Nom Usuel Etudiant", max_length=30, null=True, db_column="LIB_NOM_USU_IND")
    lib_pr1_ind = models.CharField(u"Prenom 1 de l'Etudiant", max_length=20, null=True, db_column="LIB_PR1_IND")
    lib_pr2_ind = models.CharField(u"Prenom 2 de l'Etudiant", max_length=20, null=True, db_column="LIB_PR2_IND")
    lib_pr3_ind = models.CharField(u"Prenom 3 de l'Etudiant", max_length=20, null=True, db_column="LIB_PR3_IND")

    cod_etu = models.IntegerField(u"Code Etudiant", db_column="COD_ETU", null=True)
    cod_sex_etu = models.CharField(u"Code Sexe de l'Etudiant", max_length=1, null=True, db_column="COD_SEX_ETU")
    
    daa_ens_sup = models.CharField(u"annee de 1er inscription dans l'etablissement superieur", max_length=4, null=True,
                                   db_column="DAA_ENS_SUP")
    daa_etb = models.CharField(u"annee de 1er inscription dans l'etablisseement", max_length=4, null=True,
                               db_column="DAA_ETB")

    def get_code_secret(self):
        return utils.make_etudiant_password(self.cod_etu)

    get_code_secret.short_description = "Code secret:"

    def ine(self):
        return u"%s%s" % (self.cod_nne_ind, self.cod_cle_nne_ind)

    class Meta:
        db_table = "INDIVIDU"
        verbose_name = u"étudiant"
        app_label = 'django_apogee'

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
            return adresse_annuelle[0].cod_bdi or adresse_annuelle[0].lib_ade
        else:
            return self.adresse_fixe.all()[0].cod_bdi or self.adresse_fixe.all()[0].lib_ade

    def get_pays(self, annee):
        adresse_annuelle = self.adresse_annuelle.filter(cod_anu_ina=annee)
        if adresse_annuelle:
            return adresse_annuelle[0].cod_pay.lib_pay
        else:
            return self.adresse_fixe.all()[0].cod_pay.lib_pay

    def get_full_adresse(self, annee):
        try:
            adresse_annuelle = self.adresse_annuelle.filter(cod_anu_ina=annee)
            if adresse_annuelle:
                return adresse_annuelle[0].__str__()
            else:
                return self.adresse_fixe.all()[0].__str__()
        except IndexError:
            return ""

    def get_adresse_html(self):
        try:
            adresse_annuelle = self.adresse_annuelle.filter(cod_anu_ina=self)
            if adresse_annuelle:
                return adresse_annuelle[0].html()
            else:
                return self.adresse_fixe.all()[0].html()
        except IndexError:
            return u""

    get_full_adresse.short_description = 'Adresse'

    def get_dico_adresse(self, annee):
        adresse_annuelle = self.adresse_annuelle.filter(cod_anu_ina=annee)
        if adresse_annuelle:
            return adresse_annuelle[0].get_dico()
        else:
            return self.adresse_fixe.all()[0].get_dico()

    def get_tel_fixe(self):
        if self.adresse_fixe.all()[0].num_tel != u'':
            return self.adresse_fixe.all()[0].num_tel
        else:
            return self.adresse_fixe.all()[0].num_tel_port

    def get_tel_annuel(self):
        adresse_annuelle = self.adresse_annuelle.filter(cod_anu_ina=self.annee)
        if adresse_annuelle and adresse_annuelle[0].num_tel != u'':
            return adresse_annuelle[0].num_tel
        else:
            return adresse_annuelle[0].num_tel_port

    def get_tel(self):
        adresse_annuelle = self.adresse_annuelle.filter(cod_anu_ina=self.annee)
        if adresse_annuelle and adresse_annuelle[0].num_tel != u'':
            return adresse_annuelle[0].num_tel
        elif adresse_annuelle and adresse_annuelle[0].num_tel_port != u'':
            return adresse_annuelle[0].num_tel_port
        else:
            return self.adresse_fixe.all()[0].num_tel

    def get_email(self, annee):
        try:
            adresse_annuelle = self.adresse_annuelle.filter(cod_anu_ina=annee)
            if adresse_annuelle and adresse_annuelle[0].adr_mail != '':
                email = adresse_annuelle[0].adr_mail
            else:
                email = self.adresse_fixe.all()[0].adr_mail
        except IndexError:
            email = u""
        return email
    get_email.short_description = u"email personnel"

    def __str__(self):
        return u"%s" % self.lib_nom_pat_ind


@python_2_unicode_compatible
class Adresse(models.Model):
    """
    **Les adresses des étudiants**

    :Régles Apogée:
      Il y a deux types d'adresses : l'adresse annuelle et l'adresse fixe.
      La représentation en base de donnée : si l'adresse contient le cod_ind dans le champs cod_ind
      il s'aggit de l'adresse fixe. Si c'est dans le champs cod_anu_ina c'est l'adresse annuelle.

    Pour accéder à l'adresse fixe, on uilise adresse_fixe ou adresse_annuelle comme manager à partir d'Individu.
    """
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

    def __str__(self):
        adresse = ''
        for x in self.get_str():
            if unicode(x) != u"":
                adresse += unicode(x) + u' '
        if adresse != u"":
            return adresse[:-1]
        else:
            return adresse

    def get_str(self):
        if self.cod_com and self.cod_bdi:
            lib_ach = ComBdi.objects.get(cod_com=self.cod_com, cod_bdi=self.cod_bdi).lib_ach
        else:
            lib_ach = ""
        if self.cod_ind:
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
        app_label = 'django_apogee'



@python_2_unicode_compatible
class InsAdmEtp(CompositeImplementation):
    id = models.CharField(primary_key=True, max_length=30)
    cod_anu = models.ForeignKey(AnneeUni, verbose_name=u"Code Annee Universitaire")
    cod_ind = models.ForeignKey(Individu, db_column='COD_IND', related_name="etapes_ied")
    cod_etp = models.CharField(u"Code Etape", max_length=8, null=True,
                               db_column="COD_ETP")
    cod_vrs_vet = models.CharField(u"(COPIED)Numero Version Etape", max_length=3, db_column="COD_VRS_VET")
    num_occ_iae = models.CharField(u"Numero d'Occurrence Version Etape Choisie", max_length=2, null=True, db_column="NUM_OCC_IAE")
    cod_dip = models.CharField(u"(COPIED)Code Diplome Etablissement", max_length=7, null=True, db_column="COD_DIP")
    cod_vrs_vdi = models.CharField(u"(COPIED)Numero de Version Diplome", null=True , db_column="COD_VRS_VDI" , max_length=3)
    cod_cge = models.CharField(u"Code Centre de Gestion", max_length=3, null=True, db_column="COD_CGE")
    dat_cre_iae = models.DateTimeField(u"Date de création de l'IAE", null=True, db_column="DAT_CRE_IAE")
    dat_mod_iae = models.DateTimeField(u"Date de modification de l'IAE", null=True, db_column="DAT_MOD_IAE")
    nbr_ins_cyc = models.IntegerField(u'Nombre d\'Inscriptions dans le Cycle', null=True, db_column="NBR_INS_CYC")
    nbr_ins_etp = models.IntegerField(u"Nombre d'Inscriptions dans l'Etape", null=True, db_column="NBR_INS_ETP")
    dat_annul_res_iae = models.DateTimeField(u"Date annulation ou résiliation IA", null=True, db_column="DAT_ANNUL_RES_IAE")
    tem_iae_prm = models.CharField(u"Temoin Etape Premiere ou Seconde", max_length=1, null=True,
                                   db_column="TEM_IAE_PRM")
    nbr_ins_dip = models.IntegerField(u"Nombre d'Inscriptions dans le Diplome", null=True, db_column="NBR_INS_DIP")
    eta_iae = models.CharField(u"etat de l'inscription", null=True, max_length=1, db_column='ETA_IAE')
    eta_pmt_iae = models.CharField(u"Etat des paiements des droits", null=True, max_length=1, db_column="ETA_PMT_IAE")
    cod_pru = models.CharField(u"Code profil étudiant", null=True, max_length=2, db_column="COD_PRU")
    inscrits = EtapeNonCondiValideManager()
    inscrits_condi = EtapeCondiValideManager()
    objects = models.Manager()

    def __str__(self):
        return self.cod_ind.name

    class Meta:
        db_table = u"INS_ADM_ETP_COPY"
        verbose_name = u"Etape"
        verbose_name_plural = u"etapes de l'étudiant"
        app_label = 'django_apogee'


    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.pk:
            self.pk = str(self.cod_anu_id) + str(self.cod_ind_id) + str(self.cod_etp) + str(self.cod_vrs_vet) +\
                        str(self.num_occ_iae)
        return super(InsAdmEtp, self).save(force_insert=force_insert, force_update=force_update,
                                           using=using, update_fields=update_fields)

    def cod_opi(self):
        return u"%s" % self.cod_ind.cod_ind_opi
    cod_opi.short_description = u"Code opi"

    def is_reins(self):
        if self.nbr_ins_etp == 1:
            return False
        else:
            return True

    def nom(self):
        return unicode(self.cod_ind.lib_nom_pat_ind)

    nom.short_description = 'Nom'

    def prenom(self):
        return unicode(self.cod_ind.lib_pr1_ind)

    prenom.short_description = 'Prenom'

    def cod_etu(self):
        return unicode(self.cod_ind.cod_etu)

    cod_etu.short_description = 'Code étudiant'

    def adresse(self):
        return unicode(self.cod_ind.get_full_adresse())

    adresse.short_description = 'Adresse'

    def annulation(self):
        etat = self.eta_iae
        if etat == "E":
            return u"En cours"
        elif etat == 'R':
            return u"Résiliée"
        elif etat == 'A':
            return u"Annulée le %s" % self.dat_annul_res_iae
        else:
            return u'<span class="input label label-warning">Dossier détruit Annomalie</span>'

    annulation.short_description = "Etat de l'inscription administrative"
    annulation.allow_tags = True

    def __str__(self):
        return u"%s %s %s" % (self.cod_ind.cod_etu, self.cod_etp, self.cod_anu)

    def resume(self):
        return u"Etape : %s | Année : %s |Centre de gestion %s" % (self.cod_etp, self.cod_anu, self.cod_cge)

    resume.short_description = u"Etape"

    def date(self):
        return u"Date de création : %s | Date de modification : %s | Date de résiliation : %s" % (
            self.dat_cre_iae, self.dat_mod_iae if self.dat_mod_iae else u"",
            self.dat_annul_res_iae if self.dat_annul_res_iae else u""
        )

    date.short_description = u"Dates d'opération"

    def condi(self):

        if self.cod_pru == 'NO':
            return u"Normal"
        elif self.cod_pru == 'AJ':
            return u"Ajac"
        elif self.cod_pru == 'FP':
            return u"Formation permanente"
        else:
            return u"INCONNU"

    condi.short_description = u"Niveau de l'inscription"

    def bloated_query(self):
        cursor = connections['oracle'].cursor()
        query = """select count(*) from ins_adm_etp where cod_ind = '%s' and tem_iae_prm='O' and cod_dip='%s' and cod_vrs_vdi in (
  select cod_vrs_vdi from VERSION_DIPLOME where cod_sis_vdi in (
    select cod_sis_vdi from version_diplome where cod_vrs_vdi = %s and cod_dip = '%s'));""" % (self.cod_ind.cod_ind, self.cod_dip, self.cod_vrs_vdi, self.cod_dip)
        try:
            cursor.execute(query)
            result = cursor.fetchone()[0]
        except DatabaseError:
            return None
        return result

    @property
    def is_reins(self):
        """
        todo
        reinscription dans la formation
        :return: bool
        """
        value = self.bloated_query()
        if value is None:
            return None
        if value > 1:
            return True
        return False

@python_2_unicode_compatible
class InsAdmEtpInitial(CompositeInitial):
    cod_anu = models.ForeignKey(AnneeUni, max_length=4, db_column="COD_ANU")
    cod_ind = models.ForeignKey(Individu, db_column='COD_IND', primary_key=True, related_name="etapes")
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
    _composite_field = ['cod_anu', 'cod_ind', 'cod_etp', 'cod_vrs_vet', 'num_occ_iae']
    cod_vrs_vdi = models.CharField(u"(COPIED)Numero de Version Diplome", null=True, db_column="COD_VRS_VDI", max_length=3)
    inscrits = EtapeNonCondiValideManagerOracle()
    inscrits_condi = EtapeCondiValideManagerOracle()

    objects = models.Manager()

    def __str__(self):
        return self.cod_anu

    class Meta:
        db_table = u"INS_ADM_ETP"
        app_label = 'django_apogee'
        managed = False


class InsAdmAnu(models.Model):
    cod_anu = models.CharField(u"Code Annee Universitaire", max_length=4, db_column="COD_ANU", primary_key=True)
    cod_ind = models.ForeignKey(Individu, db_column='COD_IND',
                                related_name="inscription_annuelle")
    cod_rgi = models.CharField(u"Code régime inscription", max_length=1, null=True, db_column="COD_RGI")
    cod_stu = models.CharField(u"Statut de l'étudiant", max_length=2, null=True, db_column="COD_STU")
    # etablissemnt anterieur
    cod_tpe_ant = models.CharField(u"code type etablissement anterieur", max_length=2,
                                   null=True, db_column="COD_TPE_ANT")
    cod_etb_ant = models.CharField(u"code national de l'etalblisement anterieur", max_length=8,
                                   null=True, db_column="COD_ETB_ANT")
    cod_dep_ant = models.CharField(u"code departement etabliessement anterieur", max_length=3, null=True,
                                   db_column="COD_DEP_ANT")
    cod_pay_ant = models.CharField(u"code pays etablissement anterieur", max_length=3, null=True,
                                   db_column="COD_PAY_ANT")
    daa_etb_ant_iaa = models.CharField(u"annee du dernier etablissement frequente", max_length=4, null=True,
                                       db_column="DAA_ETB_ANT_IAA")
    # annee precedante
    cod_sis_ann_pre = models.CharField(u"code situation sise annee precedente", max_length=1, null=True,
                                       db_column="COD_SIS_ANN_PRE")
    cod_etb_ann_pre = models.CharField(u"code national de l'etablissement de l'anne precedente", max_length=8,
                                       null=True, db_column="COD_ETB_ANN_PRE")
    cod_dep_ann_pre = models.CharField(u"code département annee precedente", max_length=3, null=True,
                                       db_column="COD_DEP_ANN_PRE")
    cod_tds_ann_pre = models.CharField(u"code type diplome sise annee precedente", max_length=1, null=True,
                                       db_column="COD_TDS_ANN_PRE")
    # dernier diplome obtenu
    cod_dep_pay_der_dpl = models.CharField(u"code departement pays dernier diplom", max_length=3, null=True,
                                           db_column="COD_DEP_PAY_DER_DPL")
    cod_typ_dep_pay_der_dpl = models.CharField(u"code type departement ou pays denier diplome obtenue", max_length=1,
                                               null=True, db_column="COD_TYP_DEP_PAY_DER_DPL")
    daa_etb_der_dpl = models.CharField(u"date obtention dernier diplome", max_length=4, null=True,
                                       db_column="DAA_ETB_DER_DPL")
    cod_tde_der_dpl = models.CharField(u"code type diplome externe dernier diplome obtenu", max_length=3,
                                       null=True, db_column="COD_TDE_DER_DPL")
    cod_etb_der_dpl = models.CharField(u"code etablissement dernier diplome", max_length=8, null=True,
                                       db_column="COD_ETB_DER_DPL")

    class Meta:
        db_table = u"INS_ADM_ANU"
        verbose_name = u"Etape annuelle d'un étudiant"
        verbose_name_plural = u"Etapes annuelles des étudiants"
        app_label = 'django_apogee'


class IndBac(models.Model):
    """
    abréviation: IBA
    Libellé: Baccalauréats ou équivalences obtenus par chaque individu
    Clé primaire:
        colonne
        -------
        cod_ind
        cod_bac
    Clé(s) étrangère(s)
        colonne     table de référence      colonne de référence
        -------     ------------------      --------------------
        cod_bac     BAC_OUX_EQU             cod_bac
        cod_dep     DEPARTEMENT             cod_dep
        cod_etb     ETABLISSEMENT           cod_etb
        cod_ind     INDIVIDU                cod_ind
        cod_mnb     MENTION_NIV_BAC         cod_mnb
        cod_tpe     TYP_ETB                 cod_tpe
    """

    cod_ind = models.CharField(u"code etudiant au sein de l'établissement", max_length=8,
                               db_column="COD_IND", primary_key=True)
    cod_bac = models.CharField(u"code_baccalaureat ou equivalence", max_length=4, null=True, db_column="COD_BAC")
    cod_etb = models.CharField(u"code national de l'etablissement de preparation du bac", max_length=8,
                               null=True, db_column="COD_ETB")
    cod_tpe = models.CharField(u"code type etablissement", max_length=2, null=True, db_column="COD_TPE")
    cod_dep = models.CharField(u"code departement de preparation du bac", max_length=3, null=True, db_column="COD_DEP")
    cod_mnb = models.CharField(u"code mention niveau bac obtenue", max_length=2, null=True, db_column="COD_MNB")
    daa_obt_bac_iba = models.CharField(u"annee de la date d'obtention du bac", max_length=4, null=True,
                                       db_column="DAA_OBT_BAC_IBA")
    tem_ins_adm = models.CharField(u"temoin bac titre acces a universite", max_length=1, default='O',
                                   db_column="TEM_INS_ADM")
    cod_tpe_opi = models.CharField(u"code opi du type de l'etablissement d'obtention du bac", max_length=2,
                                   null=True, db_column="COD_TPE_OPI")

    class Meta:
        app_label = "django_apogee"
        db_table = 'IND_BAC'
        managed = False
