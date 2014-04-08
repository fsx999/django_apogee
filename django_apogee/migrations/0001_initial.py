# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AnneeUni'
        db.create_table(u'ANNEE_UNI', (
            ('cod_anu', self.gf('django.db.models.fields.CharField')(max_length=4, primary_key=True, db_column=u'COD_ANU')),
            ('eta_anu_iae', self.gf('django.db.models.fields.CharField')(default=u'I', max_length=1, db_column=u'ETA_ANU_IAE')),
        ))
        db.send_create_signal(u'django_apogee', ['AnneeUni'])

        # Adding model 'Pays'
        db.create_table(u'PAYS', (
            ('cod_pay', self.gf('django.db.models.fields.CharField')(max_length=3, primary_key=True, db_column=u'COD_PAY')),
            ('cod_sis_pay', self.gf('django.db.models.fields.CharField')(max_length=3, db_column=u'COD_SIS_PAY')),
            ('lib_pay', self.gf('django.db.models.fields.CharField')(max_length=50, db_column=u'LIB_PAY')),
            ('lic_pay', self.gf('django.db.models.fields.CharField')(max_length=20, db_column=u'LIC_PAY')),
            ('lib_nat', self.gf('django.db.models.fields.CharField')(max_length=50, db_column=u'LIB_NAT')),
            ('tem_ouv_drt_sso_pay', self.gf('django.db.models.fields.CharField')(max_length=1, db_column=u'TEM_OUV_DRT_SSO_PAY')),
            ('tem_en_sve_pay', self.gf('django.db.models.fields.CharField')(max_length=1, db_column=u'TEM_EN_SVE_PAY')),
            ('tem_del', self.gf('django.db.models.fields.CharField')(max_length=1, db_column=u'TEM_DEL')),
            ('tem_afl_dec_ind_pay', self.gf('django.db.models.fields.CharField')(max_length=1, db_column=u'TEM_AFL_DEC_IND_PAY')),
        ))
        db.send_create_signal(u'django_apogee', ['Pays'])

        # Adding model 'Departement'
        db.create_table(u'DEPARTEMENT', (
            ('cod_dep', self.gf('django.db.models.fields.CharField')(max_length=3, primary_key=True, db_column=u'COD_DEP')),
            ('cod_acd', self.gf('django.db.models.fields.IntegerField')(db_column=u'COD_ACD')),
            ('lib_dep', self.gf('django.db.models.fields.CharField')(max_length=60, db_column=u'LIB_DEP')),
            ('lic_dep', self.gf('django.db.models.fields.CharField')(max_length=20, db_column=u'LIC_DEP')),
            ('tem_en_sve_dep', self.gf('django.db.models.fields.CharField')(max_length=1, db_column=u'TEM_EN_SVE_DEP')),
        ))
        db.send_create_signal(u'django_apogee', ['Departement'])

        # Adding model 'SitFam'
        db.create_table(u'SIT_FAM', (
            ('cod_fam', self.gf('django.db.models.fields.CharField')(max_length=1, primary_key=True, db_column=u'COD_FAM')),
            ('cod_sis_fam', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, db_column=u'COD_SIS_FAM', blank=True)),
            ('lib_fam', self.gf('django.db.models.fields.CharField')(max_length=40, db_column=u'LIB_FAM')),
            ('lic_fam', self.gf('django.db.models.fields.CharField')(max_length=10, db_column=u'LIC_FAM')),
            ('tem_en_sve_fam', self.gf('django.db.models.fields.CharField')(default=u'O', max_length=1, db_column=u'TEM_EN_SVE_FAM')),
        ))
        db.send_create_signal(u'django_apogee', ['SitFam'])

        # Adding model 'TypHandicap'
        db.create_table(u'TYP_HANDICAP', (
            ('cod_thp', self.gf('django.db.models.fields.CharField')(max_length=2, primary_key=True, db_column=u'COD_THP')),
            ('lib_thp', self.gf('django.db.models.fields.CharField')(max_length=50, db_column=u'LIB_THP')),
            ('lic_thp', self.gf('django.db.models.fields.CharField')(max_length=20, db_column=u'LIC_THP')),
            ('tem_tie_tps', self.gf('django.db.models.fields.CharField')(default=u'O', max_length=1, db_column=u'TEM_TIE_TPS')),
            ('tem_en_sve_thp', self.gf('django.db.models.fields.CharField')(default=u'O', max_length=1, db_column=u'TEM_EN_SVE_THP')),
        ))
        db.send_create_signal(u'django_apogee', ['TypHandicap'])

        # Adding model 'SitMil'
        db.create_table(u'SIT_MIL', (
            ('cod_sim', self.gf('django.db.models.fields.CharField')(max_length=1, primary_key=True, db_column=u'COD_SIM')),
            ('lib_sim', self.gf('django.db.models.fields.CharField')(max_length=50, db_column=u'LIB_SIM')),
            ('lic_sim', self.gf('django.db.models.fields.CharField')(max_length=20, db_column=u'LIC_SIM')),
            ('tem_sai_dmm_lbt', self.gf('django.db.models.fields.CharField')(default=u'O', max_length=1, db_column=u'TEM_SAI_DMM_LBT')),
            ('tem_en_sve_sim', self.gf('django.db.models.fields.CharField')(default=u'O', max_length=1, db_column=u'TEM_EN_SVE_SIM')),
            ('tem_del_dip', self.gf('django.db.models.fields.CharField')(default=u'N', max_length=1, db_column=u'TEM_DEL_DIP')),
        ))
        db.send_create_signal(u'django_apogee', ['SitMil'])

        # Adding model 'ComBdi'
        db.create_table(u'COM_BDI_COPY', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=13, primary_key=True)),
            ('cod_bdi', self.gf('django.db.models.fields.CharField')(max_length=6, db_column=u'COD_BDI')),
            ('cod_com', self.gf('django.db.models.fields.CharField')(max_length=6, db_column=u'COD_COM')),
            ('lib_ach', self.gf('django.db.models.fields.CharField')(max_length=26, db_column=u'LIB_ACH')),
            ('eta_ptc_loc', self.gf('django.db.models.fields.CharField')(max_length=3, db_column=u'ETA_PTC_LOC')),
            ('eta_ptc_ach', self.gf('django.db.models.fields.CharField')(max_length=3, db_column=u'ETA_PTC_ACH')),
            ('tem_en_sve_cbd', self.gf('django.db.models.fields.CharField')(max_length=3, db_column=u'TEM_EN_SVE_CBD')),
            ('cod_fic_cbd', self.gf('django.db.models.fields.CharField')(max_length=3, db_column=u'COD_FIC_CBD')),
        ))
        db.send_create_signal(u'django_apogee', ['ComBdi'])

        # Adding model 'TypHebergement'
        db.create_table(u'TYP_HEBERGEMENT', (
            ('cod_thb', self.gf('django.db.models.fields.CharField')(max_length=1, primary_key=True, db_column=u'COD_THB')),
            ('lib_thb', self.gf('django.db.models.fields.CharField')(max_length=60, db_column=u'LIB_THB')),
            ('tem_en_sve_thb', self.gf('django.db.models.fields.CharField')(default=u'O', max_length=1, db_column=u'TEM_EN_SVE_THB')),
        ))
        db.send_create_signal(u'django_apogee', ['TypHebergement'])

        # Adding model 'BacOuxEqu'
        db.create_table(u'BAC_OUX_EQU', (
            ('cod_bac', self.gf('django.db.models.fields.CharField')(max_length=4, primary_key=True, db_column=u'COD_BAC')),
            ('cod_sis_bac', self.gf('django.db.models.fields.CharField')(max_length=4, db_column=u'COD_SIS_BAC')),
            ('lib_bac', self.gf('django.db.models.fields.CharField')(max_length=80, db_column=u'LIB_BAC')),
            ('lic_bac', self.gf('django.db.models.fields.CharField')(max_length=20, db_column=u'LIC_BAC')),
            ('tem_etb', self.gf('django.db.models.fields.CharField')(default=u'O', max_length=1, db_column=u'TEM_ETB')),
            ('tem_mnb', self.gf('django.db.models.fields.CharField')(default=u'O', max_length=1, db_column=u'TEM_MNB')),
            ('tem_nat_bac', self.gf('django.db.models.fields.CharField')(default=u'O', max_length=1, db_column=u'TEM_NAT_BAC')),
            ('tem_obt_tit_etb_sec', self.gf('django.db.models.fields.CharField')(default=u'O', max_length=1, db_column=u'TEM_OBT_TIT_ETB_SEC')),
            ('tem_en_sve_bac', self.gf('django.db.models.fields.CharField')(default=u'O', max_length=1, db_column=u'TEM_EN_SVE_BAC')),
            ('tem_deb', self.gf('django.db.models.fields.CharField')(default=u'O', max_length=1, db_column=u'TEM_DEB')),
            ('tem_del', self.gf('django.db.models.fields.CharField')(default=u'O', max_length=1, db_column=u'TEM_DEL')),
            ('daa_deb_vld_bac', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, db_column=u'DAA_DEB_VLD_BAC')),
            ('daa_fin_vld_bac', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, db_column=u'DAA_FIN_VLD_BAC')),
            ('tem_type_equi', self.gf('django.db.models.fields.CharField')(default=u'N', max_length=1, db_column=u'TEM_TYPE_EQUI')),
            ('cod_sis', self.gf('django.db.models.fields.related.ForeignKey')(max_length=1, to=orm['django_apogee.SituationSise'], null=True, db_column=u'COD_SIS')),
            ('cod_tds', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, db_column=u'COD_TDS')),
        ))
        db.send_create_signal(u'django_apogee', ['BacOuxEqu'])

        # Adding model 'MentionBac'
        db.create_table(u'MENTION_NIV_BAC', (
            ('cod_mnb', self.gf('django.db.models.fields.CharField')(max_length=2, primary_key=True, db_column=u'COD_MNB')),
            ('lib_mnb', self.gf('django.db.models.fields.CharField')(max_length=50, db_column=u'LIB_MNB')),
            ('lic_mnb', self.gf('django.db.models.fields.CharField')(max_length=20, db_column=u'LIC_MNB')),
            ('tem_en_sve_mnb', self.gf('django.db.models.fields.CharField')(default=u'O', max_length=1, db_column=u'TEM_EN_SVE_MNB')),
        ))
        db.send_create_signal(u'django_apogee', ['MentionBac'])

        # Adding model 'TypEtb'
        db.create_table(u'TYP_ETB', (
            ('cod_tpe', self.gf('django.db.models.fields.CharField')(max_length=2, primary_key=True, db_column=u'COD_TPE')),
            ('cod_sis_tpe', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, db_column=u'COD_SIS_TPE')),
            ('lib_tpe', self.gf('django.db.models.fields.CharField')(max_length=50, db_column=u'LIB_TPE')),
            ('lic_tpe', self.gf('django.db.models.fields.CharField')(max_length=20, db_column=u'LIC_TPE')),
            ('tem_det_tpe', self.gf('django.db.models.fields.CharField')(default=u'O', max_length=1, db_column=u'TEM_DET_TPE')),
            ('tem_en_sve_tpe', self.gf('django.db.models.fields.CharField')(default=u'O', max_length=1, db_column=u'TEM_EN_SVE_TPE')),
            ('tem_ges_trf_tpe', self.gf('django.db.models.fields.CharField')(default=u'O', max_length=1, db_column=u'TEM_GES_TRF_TPE')),
            ('tem_prop_autre_etb', self.gf('django.db.models.fields.CharField')(default=u'N', max_length=1, db_column=u'TEM_PROP_AUTRE_ETB')),
        ))
        db.send_create_signal(u'django_apogee', ['TypEtb'])

        # Adding model 'Etablissement'
        db.create_table(u'ETABLISSEMENT', (
            ('cod_etb', self.gf('django.db.models.fields.CharField')(max_length=8, primary_key=True, db_column=u'COD_ETB')),
            ('cod_tpe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_apogee.TypEtb'], db_column=u'COD_TPE')),
            ('cod_dep', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_apogee.Departement'], db_column=u'COD_DEP')),
            ('lib_etb', self.gf('django.db.models.fields.CharField')(max_length=50, db_column=u'LIB_ETB')),
            ('cod_pos_adr_etb', self.gf('django.db.models.fields.CharField')(default=None, max_length=20, null=True, db_column=u'COD_POS_ADR_ETB')),
            ('tem_en_sve_etb', self.gf('django.db.models.fields.CharField')(default=u'O', max_length=1, db_column=u'TEM_EN_SVE_ETB')),
            ('tem_aut_sis_etb', self.gf('django.db.models.fields.CharField')(default=u'O', max_length=1, db_column=u'TEM_AUT_SIS_ETB')),
            ('cod_aff_dep_etb', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, db_column=u'COD_AFF_DEP_ETB')),
            ('cod_aff_etb', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, db_column=u'COD_AFF_ETB')),
            ('lib_off_etb', self.gf('django.db.models.fields.CharField')(max_length=60, db_column=u'LIB_OFF_ETB')),
            ('lib_art_off_etb', self.gf('django.db.models.fields.CharField')(max_length=5, db_column=u'LIB_ART_OFF_ETB')),
            ('cod_pay_adr_etb', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_apogee.Pays'], null=True, db_column=u'COD_PAY_ADR_ETB')),
        ))
        db.send_create_signal(u'django_apogee', ['Etablissement'])

        # Adding model 'CatSocPfl'
        db.create_table(u'CAT_SOC_PFL', (
            ('cod_pcs', self.gf('django.db.models.fields.CharField')(max_length=2, primary_key=True, db_column=u'COD_PCS')),
            ('lib_pcs', self.gf('django.db.models.fields.CharField')(max_length=50, db_column=u'LIB_PCS')),
            ('tem_en_sve_pcs', self.gf('django.db.models.fields.CharField')(default=u'O', max_length=1, db_column=u'TEM_EN_SVE_PCS')),
            ('lib_web_pcs', self.gf('django.db.models.fields.CharField')(max_length=120, db_column=u'LIB_WEB_PCS')),
            ('tem_sai_qtr', self.gf('django.db.models.fields.CharField')(default=u'O', max_length=1, db_column=u'TEM_SAI_QTR')),
        ))
        db.send_create_signal(u'django_apogee', ['CatSocPfl'])

        # Adding model 'QuotiteTra'
        db.create_table(u'QUOTITE_TRA', (
            ('cod_qtr', self.gf('django.db.models.fields.CharField')(max_length=1, primary_key=True, db_column=u'COD_QTR')),
            ('lib_qtr', self.gf('django.db.models.fields.CharField')(max_length=50, db_column=u'LIB_QTR')),
            ('lic_qtr', self.gf('django.db.models.fields.CharField')(max_length=50, db_column=u'LIC_QTR')),
            ('lim1_qtr', self.gf('django.db.models.fields.CharField')(max_length=50, db_column=u'LIM1_QTR')),
            ('lib_web_qtr', self.gf('django.db.models.fields.CharField')(max_length=120, db_column=u'LIB_WEB_QTR')),
            ('tem_en_sve_qtr', self.gf('django.db.models.fields.CharField')(default=u'O', max_length=1, db_column=u'TEM_EN_SVE_QTR')),
            ('tem_cou_aut_reg_qtr', self.gf('django.db.models.fields.CharField')(default=u'O', max_length=1, db_column=u'TEM_COU_AUT_REG_QTR')),
        ))
        db.send_create_signal(u'django_apogee', ['QuotiteTra'])

        # Adding model 'DomaineActPfl'
        db.create_table(u'DOMAINE_ACT_PFL', (
            ('cod_dap', self.gf('django.db.models.fields.CharField')(max_length=2, primary_key=True, db_column=u'COD_DAP')),
            ('lib_web_dap', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, db_column=u'LIB_WEB_DAP')),
        ))
        db.send_create_signal(u'django_apogee', ['DomaineActPfl'])

        # Adding model 'SituationSise'
        db.create_table(u'SITUATION_SISE', (
            ('cod_sis', self.gf('django.db.models.fields.CharField')(max_length=1, primary_key=True, db_column=u'COD_SIS')),
            ('lib_sis', self.gf('django.db.models.fields.CharField')(max_length=130, db_column=u'LIB_SIS')),
            ('tem_en_sve_sis', self.gf('django.db.models.fields.CharField')(default=u'O', max_length=1, db_column=u'TEM_EN_SVE_SIS')),
        ))
        db.send_create_signal(u'django_apogee', ['SituationSise'])

        # Adding model 'TypeDiplomeExt'
        db.create_table(u'TYP_DIPLOME_EXT', (
            ('cod_tde', self.gf('django.db.models.fields.CharField')(max_length=3, primary_key=True, db_column=u'COD_TDE')),
            ('lib_web_tde', self.gf('django.db.models.fields.CharField')(max_length=130, db_column=u'LIB_WEB_TDE')),
            ('lib_tde', self.gf('django.db.models.fields.CharField')(max_length=130, db_column=u'LIB_TDE')),
            ('tem_en_sve_tde', self.gf('django.db.models.fields.CharField')(default=u'O', max_length=1, db_column=u'TEM_EN_SVE_TDE')),
        ))
        db.send_create_signal(u'django_apogee', ['TypeDiplomeExt'])

        # Adding model 'RegimeParent'
        db.create_table(u'REGIME_PARENT', (
            ('cod_rgp', self.gf('django.db.models.fields.CharField')(max_length=2, primary_key=True, db_column=u'COD_RGP')),
            ('lib_rgp', self.gf('django.db.models.fields.CharField')(max_length=280, db_column=u'LIB_RGP')),
            ('ordre_tri_rgp', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, db_column=u'ORDRE_TRI_RGP')),
        ))
        db.send_create_signal(u'django_apogee', ['RegimeParent'])

        # Adding model 'MtfNonAflSso'
        db.create_table(u'MTF_NON_AFL_SSO', (
            ('cod_mns', self.gf('django.db.models.fields.CharField')(max_length=1, primary_key=True, db_column=u'COD_MNS')),
            ('lib_mns', self.gf('django.db.models.fields.CharField')(max_length=40, db_column=u'LIB_MNS')),
            ('lic_mns', self.gf('django.db.models.fields.CharField')(max_length=10, db_column=u'LIC_MNS')),
            ('tem_en_sve_mns', self.gf('django.db.models.fields.CharField')(default=u'O', max_length=1, db_column=u'TEM_EN_SVE_MNS')),
            ('tem_del', self.gf('django.db.models.fields.CharField')(default=u'O', max_length=1, db_column=u'TEM_DEL')),
        ))
        db.send_create_signal(u'django_apogee', ['MtfNonAflSso'])

        # Adding model 'SitSociale'
        db.create_table(u'SIT_SOCIALE', (
            ('cod_soc', self.gf('django.db.models.fields.CharField')(max_length=2, primary_key=True, db_column=u'COD_SOC')),
            ('lib_soc', self.gf('django.db.models.fields.CharField')(max_length=35, db_column=u'LIM1_SOC')),
            ('lic_soc', self.gf('django.db.models.fields.CharField')(max_length=35, db_column=u'LIB_SOC')),
            ('tem_en_sve_soc', self.gf('django.db.models.fields.CharField')(max_length=1, db_column=u'TEM_EN_SVE_SOC')),
            ('tem_del', self.gf('django.db.models.fields.CharField')(max_length=1, db_column=u'TEM_DEL')),
        ))
        db.send_create_signal(u'django_apogee', ['SitSociale'])

        # Adding model 'Bourse'
        db.create_table(u'BOURSE', (
            ('cod_brs', self.gf('django.db.models.fields.CharField')(max_length=2, primary_key=True, db_column=u'COD_BRS')),
            ('cod_soc', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_apogee.SitSociale'], null=True, db_column=u'COD_SOC')),
            ('lim1_brs', self.gf('django.db.models.fields.CharField')(max_length=35, db_column=u'LIM1_BRS')),
        ))
        db.send_create_signal(u'django_apogee', ['Bourse'])

        # Adding model 'Composante'
        db.create_table(u'COMPOSANTE', (
            ('cod_cmp', self.gf('django.db.models.fields.CharField')(max_length=3, primary_key=True, db_column=u'COD_CMP')),
            ('cod_tpc', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, db_column=u'COD_TPC')),
            ('lib_cmp', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, db_column=u'LIB_CMP')),
        ))
        db.send_create_signal(u'django_apogee', ['Composante'])

        # Adding model 'CentreGestion'
        db.create_table(u'CENTRE_GESTION', (
            ('cod_cge', self.gf('django.db.models.fields.CharField')(max_length=3, primary_key=True, db_column=u'COD_CGE')),
            ('lib_cge', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, db_column=u'LIB_CGE')),
        ))
        db.send_create_signal(u'django_apogee', ['CentreGestion'])

        # Adding model 'Etape'
        db.create_table(u'ETAPE', (
            ('cod_etp', self.gf('django.db.models.fields.CharField')(max_length=6, primary_key=True, db_column=u'COD_ETP')),
            ('cod_cyc', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, db_column=u'COD_CYC')),
            ('cod_cur', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, db_column=u'COD_CUR')),
            ('lib_etp', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, db_column=u'LIB_ETP')),
        ))
        db.send_create_signal(u'django_apogee', ['Etape'])

        # Adding model 'EtpGererCge'
        db.create_table(u'ETP_GERER_CGE', (
            ('cod_etp', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_apogee.Etape'], primary_key=True, db_column=u'COD_ETP')),
            ('cod_cge', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'etape_centre_gestion', db_column=u'COD_CGE', to=orm['django_apogee.CentreGestion'])),
            ('cod_cmp', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_apogee.Composante'], db_column=u'COD_CMP')),
        ))
        db.send_create_signal(u'django_apogee', ['EtpGererCge'])

        # Adding model 'Elp'
        db.create_table(u'ELEMENT_PEDAGOGI', (
            ('cod_elp', self.gf('django.db.models.fields.CharField')(max_length=8, primary_key=True, db_column=u'COD_ELP')),
            ('cod_cmp', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'centre_gestion_elp', db_column=u'COD_CMP', to=orm['django_apogee.Composante'])),
            ('lib_elp', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('eta_elp', self.gf('django.db.models.fields.CharField')(max_length=1, db_column=u'ETA_ELP')),
        ))
        db.send_create_signal(u'django_apogee', ['Elp'])

        # Adding model 'ElpLibelleInitial'
        db.create_table(u'ELP_LIBELLE', (
            ('cod_elp', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_apogee.Elp'], primary_key=True, db_column=u'COD_ELP')),
            ('cod_lng', self.gf('django.db.models.fields.CharField')(max_length=4, db_column=u'COD_LNG')),
            ('lib_elp_lng', self.gf('django.db.models.fields.CharField')(max_length=4000, null=True, db_column=u'LIB_ELP_LNG')),
        ))
        db.send_create_signal(u'django_apogee', ['ElpLibelleInitial'])

        # Adding model 'ElpLibelle'
        db.create_table(u'ELP_LIBELLE_COPY', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=13, primary_key=True)),
            ('cod_elp', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_apogee.Elp'], db_column=u'COD_ELP')),
            ('cod_lng', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, db_column=u'COD_LNG')),
            ('lib_elp_lng', self.gf('django.db.models.fields.CharField')(max_length=4000, null=True, db_column=u'LIB_ELP_LNG')),
        ))
        db.send_create_signal(u'django_apogee', ['ElpLibelle'])

        # Adding model 'Diplome'
        db.create_table(u'DIPLOME', (
            ('cod_dip', self.gf('django.db.models.fields.CharField')(max_length=7, primary_key=True, db_column=u'COD_DIP')),
            ('lib_dip', self.gf('django.db.models.fields.CharField')(max_length=60, db_column=u'LIB_DIP')),
        ))
        db.send_create_signal(u'django_apogee', ['Diplome'])

        # Adding model 'CmpHabiliterVdi'
        db.create_table(u'CMP_HABILITER_COPY', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=17, primary_key=True)),
            ('cod_cmp', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_apogee.Composante'], db_column=u'COD_CMP')),
            ('cod_dip', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_apogee.Diplome'], db_column=u'COD_DIP')),
            ('cod_vrs_vdi', self.gf('django.db.models.fields.CharField')(max_length=3, db_column=u'COD_VRS_VDI')),
            ('tem_en_sve_cvd', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, db_column=u'TEM_EN_SVE_CVD')),
        ))
        db.send_create_signal(u'django_apogee', ['CmpHabiliterVdi'])

        # Adding model 'SpecialiteVdi'
        db.create_table(u'SPECIALITE_VDI', (
            ('cod_svd', self.gf('django.db.models.fields.CharField')(max_length=6, primary_key=True, db_column=u'COD_SVD')),
            ('lib_svd', self.gf('django.db.models.fields.CharField')(max_length=400, db_column=u'LIB_SVD')),
            ('tem_en_sve_svd', self.gf('django.db.models.fields.CharField')(max_length=1, db_column=u'TEM_EN_SVE_SVD')),
        ))
        db.send_create_signal(u'django_apogee', ['SpecialiteVdi'])

        # Adding model 'VersionDiplome'
        db.create_table(u'VERSION_DIPLOME_COPY', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=11, primary_key=True)),
            ('cod_dip', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_apogee.Diplome'], max_length=7, db_column=u'COD_DIP')),
            ('cod_vrs_vdi', self.gf('django.db.models.fields.CharField')(max_length=3, db_column=u'COD_VRS_VDI')),
            ('lic_vdi', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, db_column=u'LIC_VDI')),
            ('cod_svd', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_apogee.SpecialiteVdi'], null=True, db_column=u'COD_SVD')),
        ))
        db.send_create_signal(u'django_apogee', ['VersionDiplome'])

        # Adding model 'VersionEtape'
        db.create_table(u'VERSION_ETAPE_COPY', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=10, primary_key=True)),
            ('cod_etp', self.gf('django.db.models.fields.CharField')(max_length=6, db_column=u'COD_ETP')),
            ('cod_vrs_vet', self.gf('django.db.models.fields.CharField')(max_length=3, db_column=u'COD_VRS_VET')),
        ))
        db.send_create_signal(u'django_apogee', ['VersionEtape'])

        # Adding model 'VdiFractionnerVet'
        db.create_table(u'VDI_FRACTIONNER_VET_COPY', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=22, primary_key=True)),
            ('cod_etp', self.gf('django.db.models.fields.CharField')(max_length=6, db_column=u'COD_ETP')),
            ('cod_vrs_vet', self.gf('django.db.models.fields.CharField')(max_length=3, db_column=u'COD_VRS_VET')),
            ('cod_dip', self.gf('django.db.models.fields.CharField')(max_length=7, db_column=u'COD_DIP')),
            ('cod_vrs_vdi', self.gf('django.db.models.fields.CharField')(max_length=3, db_column=u'COD_VRS_VDI')),
            ('cod_sis_daa_min', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, db_column=u'COD_SIS_DAA_MIN')),
        ))
        db.send_create_signal(u'django_apogee', ['VdiFractionnerVet'])

        # Adding model 'Individu'
        db.create_table(u'INDIVIDU', (
            ('cod_ind', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'COD_IND')),
            ('cod_ind_opi', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'COD_IND_OPI')),
            ('dat_cre_ind', self.gf('django.db.models.fields.DateTimeField')(null=True, db_column=u'DAT_CRE_IND')),
            ('dat_mod_ind', self.gf('django.db.models.fields.DateTimeField')(null=True, db_column=u'DAT_MOD_IND')),
            ('date_nai_ind', self.gf('django.db.models.fields.DateTimeField')(null=True, db_column=u'DATE_NAI_IND')),
            ('lib_nom_pat_ind', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, db_column=u'LIB_NOM_PAT_IND')),
            ('lib_nom_usu_ind', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, db_column=u'LIB_NOM_USU_IND')),
            ('lib_pr1_ind', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, db_column=u'LIB_PR1_IND')),
            ('lib_pr2_ind', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, db_column=u'LIB_PR2_IND')),
            ('lib_pr3_ind', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, db_column=u'LIB_PR3_IND')),
            ('cod_etu', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'COD_ETU')),
            ('cod_sex_etu', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, db_column=u'COD_SEX_ETU')),
            ('cod_fam', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, db_column=u'COD_FAM')),
            ('cod_nne_ind', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, db_column=u'COD_NNE_IND')),
            ('cod_cle_nne_ind', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, db_column=u'COD_CLE_NNE_IND')),
        ))
        db.send_create_signal(u'django_apogee', ['Individu'])

        # Adding model 'Adresse'
        db.create_table(u'ADRESSE', (
            ('cod_adr', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'COD_ADR')),
            ('cod_ind', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'adresse_fixe', null=True, db_column=u'COD_IND', to=orm['django_apogee.Individu'])),
            ('cod_anu_ina', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, db_column=u'COD_ANU_INA')),
            ('cod_ind_ina', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'adresse_annuelle', null=True, db_column=u'COD_IND_INA', to=orm['django_apogee.Individu'])),
            ('cod_pay', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_apogee.Pays'], null=True, db_column=u'COD_PAY')),
            ('cod_bdi', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, db_column=u'COD_BDI')),
            ('cod_com', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, db_column=u'COD_COM')),
            ('lib_ad1', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, db_column=u'LIB_AD1')),
            ('lib_ad2', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, db_column=u'LIB_AD2')),
            ('lib_ad3', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, db_column=u'LIB_AD3')),
            ('lib_ade', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, db_column=u'LIB_ADE')),
            ('num_tel', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, db_column=u'NUM_TEL')),
            ('num_tel_port', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, db_column=u'NUM_TEL_PORT')),
            ('adr_mail', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, db_column=u'ADR_MAIL')),
        ))
        db.send_create_signal(u'django_apogee', ['Adresse'])

        # Adding model 'InsAdmEtp'
        db.create_table(u'INS_ADM_ETP_COPY', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=30, primary_key=True)),
            ('cod_anu', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_apogee.AnneeUni'])),
            ('cod_ind', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'etapes_ied', db_column=u'COD_IND', to=orm['django_apogee.Individu'])),
            ('cod_etp', self.gf('django.db.models.fields.CharField')(max_length=8, null=True, db_column=u'COD_ETP')),
            ('cod_vrs_vet', self.gf('django.db.models.fields.CharField')(max_length=3, db_column=u'COD_VRS_VET')),
            ('num_occ_iae', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, db_column=u'NUM_OCC_IAE')),
            ('cod_dip', self.gf('django.db.models.fields.CharField')(max_length=7, null=True, db_column=u'COD_DIP')),
            ('cod_cge', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, db_column=u'COD_CGE')),
            ('dat_cre_iae', self.gf('django.db.models.fields.DateTimeField')(null=True, db_column=u'DAT_CRE_IAE')),
            ('dat_mod_iae', self.gf('django.db.models.fields.DateTimeField')(null=True, db_column=u'DAT_MOD_IAE')),
            ('nbr_ins_cyc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NBR_INS_CYC')),
            ('nbr_ins_etp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NBR_INS_ETP')),
            ('dat_annul_res_iae', self.gf('django.db.models.fields.DateTimeField')(null=True, db_column=u'DAT_ANNUL_RES_IAE')),
            ('tem_iae_prm', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, db_column=u'TEM_IAE_PRM')),
            ('nbr_ins_dip', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NBR_INS_DIP')),
            ('eta_iae', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, db_column=u'ETA_IAE')),
            ('eta_pmt_iae', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, db_column=u'ETA_PMT_IAE')),
            ('cod_pru', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, db_column=u'COD_PRU')),
        ))
        db.send_create_signal(u'django_apogee', ['InsAdmEtp'])


    def backwards(self, orm):
        # Deleting model 'AnneeUni'
        db.delete_table(u'ANNEE_UNI')

        # Deleting model 'Pays'
        db.delete_table(u'PAYS')

        # Deleting model 'Departement'
        db.delete_table(u'DEPARTEMENT')

        # Deleting model 'SitFam'
        db.delete_table(u'SIT_FAM')

        # Deleting model 'TypHandicap'
        db.delete_table(u'TYP_HANDICAP')

        # Deleting model 'SitMil'
        db.delete_table(u'SIT_MIL')

        # Deleting model 'ComBdi'
        db.delete_table(u'COM_BDI_COPY')

        # Deleting model 'TypHebergement'
        db.delete_table(u'TYP_HEBERGEMENT')

        # Deleting model 'BacOuxEqu'
        db.delete_table(u'BAC_OUX_EQU')

        # Deleting model 'MentionBac'
        db.delete_table(u'MENTION_NIV_BAC')

        # Deleting model 'TypEtb'
        db.delete_table(u'TYP_ETB')

        # Deleting model 'Etablissement'
        db.delete_table(u'ETABLISSEMENT')

        # Deleting model 'CatSocPfl'
        db.delete_table(u'CAT_SOC_PFL')

        # Deleting model 'QuotiteTra'
        db.delete_table(u'QUOTITE_TRA')

        # Deleting model 'DomaineActPfl'
        db.delete_table(u'DOMAINE_ACT_PFL')

        # Deleting model 'SituationSise'
        db.delete_table(u'SITUATION_SISE')

        # Deleting model 'TypeDiplomeExt'
        db.delete_table(u'TYP_DIPLOME_EXT')

        # Deleting model 'RegimeParent'
        db.delete_table(u'REGIME_PARENT')

        # Deleting model 'MtfNonAflSso'
        db.delete_table(u'MTF_NON_AFL_SSO')

        # Deleting model 'SitSociale'
        db.delete_table(u'SIT_SOCIALE')

        # Deleting model 'Bourse'
        db.delete_table(u'BOURSE')

        # Deleting model 'Composante'
        db.delete_table(u'COMPOSANTE')

        # Deleting model 'CentreGestion'
        db.delete_table(u'CENTRE_GESTION')

        # Deleting model 'Etape'
        db.delete_table(u'ETAPE')

        # Deleting model 'EtpGererCge'
        db.delete_table(u'ETP_GERER_CGE')

        # Deleting model 'Elp'
        db.delete_table(u'ELEMENT_PEDAGOGI')

        # Deleting model 'ElpLibelleInitial'
        db.delete_table(u'ELP_LIBELLE')

        # Deleting model 'ElpLibelle'
        db.delete_table(u'ELP_LIBELLE_COPY')

        # Deleting model 'Diplome'
        db.delete_table(u'DIPLOME')

        # Deleting model 'CmpHabiliterVdi'
        db.delete_table(u'CMP_HABILITER_COPY')

        # Deleting model 'SpecialiteVdi'
        db.delete_table(u'SPECIALITE_VDI')

        # Deleting model 'VersionDiplome'
        db.delete_table(u'VERSION_DIPLOME_COPY')

        # Deleting model 'VersionEtape'
        db.delete_table(u'VERSION_ETAPE_COPY')

        # Deleting model 'VdiFractionnerVet'
        db.delete_table(u'VDI_FRACTIONNER_VET_COPY')

        # Deleting model 'Individu'
        db.delete_table(u'INDIVIDU')

        # Deleting model 'Adresse'
        db.delete_table(u'ADRESSE')

        # Deleting model 'InsAdmEtp'
        db.delete_table(u'INS_ADM_ETP_COPY')


    models = {
        u'django_apogee.adresse': {
            'Meta': {'object_name': 'Adresse', 'db_table': "u'ADRESSE'"},
            'adr_mail': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'db_column': "u'ADR_MAIL'"}),
            'cod_adr': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'COD_ADR'"}),
            'cod_anu_ina': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'db_column': "u'COD_ANU_INA'"}),
            'cod_bdi': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'db_column': "u'COD_BDI'"}),
            'cod_com': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'db_column': "u'COD_COM'"}),
            'cod_ind': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'adresse_fixe'", 'null': 'True', 'db_column': "u'COD_IND'", 'to': u"orm['django_apogee.Individu']"}),
            'cod_ind_ina': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'adresse_annuelle'", 'null': 'True', 'db_column': "u'COD_IND_INA'", 'to': u"orm['django_apogee.Individu']"}),
            'cod_pay': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_apogee.Pays']", 'null': 'True', 'db_column': "u'COD_PAY'"}),
            'lib_ad1': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'db_column': "u'LIB_AD1'"}),
            'lib_ad2': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'db_column': "u'LIB_AD2'"}),
            'lib_ad3': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'db_column': "u'LIB_AD3'"}),
            'lib_ade': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'db_column': "u'LIB_ADE'"}),
            'num_tel': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'db_column': "u'NUM_TEL'"}),
            'num_tel_port': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'db_column': "u'NUM_TEL_PORT'"})
        },
        u'django_apogee.adresseopi': {
            'Meta': {'object_name': 'AdresseOpi', 'db_table': "u'ADRESSE_OPI'", 'managed': 'False'},
            'cod_bdi': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'db_column': "u'COD_BDI'"}),
            'cod_com': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'db_column': "u'COD_COM'"}),
            'cod_ind_opi': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'COD_IND_OPI'"}),
            'cod_pay': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'db_column': "u'COD_PAY'"}),
            'cod_typ_adr_opi': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'db_column': "u'COD_TYP_ADR_OPI'"}),
            'lib_ad1': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'db_column': "u'LIB_AD1'"}),
            'lib_ad2': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'db_column': "u'LIB_AD2'"}),
            'lib_ad3': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'db_column': "u'LIB_AD3'"}),
            'lib_ade': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'db_column': "u'LIB_ADE'"})
        },
        u'django_apogee.anneeuni': {
            'Meta': {'ordering': "[u'-cod_anu']", 'object_name': 'AnneeUni', 'db_table': "u'ANNEE_UNI'"},
            'cod_anu': ('django.db.models.fields.CharField', [], {'max_length': '4', 'primary_key': 'True', 'db_column': "u'COD_ANU'"}),
            'eta_anu_iae': ('django.db.models.fields.CharField', [], {'default': "u'I'", 'max_length': '1', 'db_column': "u'ETA_ANU_IAE'"})
        },
        u'django_apogee.bacouxequ': {
            'Meta': {'object_name': 'BacOuxEqu', 'db_table': "u'BAC_OUX_EQU'"},
            'cod_bac': ('django.db.models.fields.CharField', [], {'max_length': '4', 'primary_key': 'True', 'db_column': "u'COD_BAC'"}),
            'cod_sis': ('django.db.models.fields.related.ForeignKey', [], {'max_length': '1', 'to': u"orm['django_apogee.SituationSise']", 'null': 'True', 'db_column': "u'COD_SIS'"}),
            'cod_sis_bac': ('django.db.models.fields.CharField', [], {'max_length': '4', 'db_column': "u'COD_SIS_BAC'"}),
            'cod_tds': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'db_column': "u'COD_TDS'"}),
            'daa_deb_vld_bac': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'db_column': "u'DAA_DEB_VLD_BAC'"}),
            'daa_fin_vld_bac': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'db_column': "u'DAA_FIN_VLD_BAC'"}),
            'lib_bac': ('django.db.models.fields.CharField', [], {'max_length': '80', 'db_column': "u'LIB_BAC'"}),
            'lic_bac': ('django.db.models.fields.CharField', [], {'max_length': '20', 'db_column': "u'LIC_BAC'"}),
            'tem_deb': ('django.db.models.fields.CharField', [], {'default': "u'O'", 'max_length': '1', 'db_column': "u'TEM_DEB'"}),
            'tem_del': ('django.db.models.fields.CharField', [], {'default': "u'O'", 'max_length': '1', 'db_column': "u'TEM_DEL'"}),
            'tem_en_sve_bac': ('django.db.models.fields.CharField', [], {'default': "u'O'", 'max_length': '1', 'db_column': "u'TEM_EN_SVE_BAC'"}),
            'tem_etb': ('django.db.models.fields.CharField', [], {'default': "u'O'", 'max_length': '1', 'db_column': "u'TEM_ETB'"}),
            'tem_mnb': ('django.db.models.fields.CharField', [], {'default': "u'O'", 'max_length': '1', 'db_column': "u'TEM_MNB'"}),
            'tem_nat_bac': ('django.db.models.fields.CharField', [], {'default': "u'O'", 'max_length': '1', 'db_column': "u'TEM_NAT_BAC'"}),
            'tem_obt_tit_etb_sec': ('django.db.models.fields.CharField', [], {'default': "u'O'", 'max_length': '1', 'db_column': "u'TEM_OBT_TIT_ETB_SEC'"}),
            'tem_type_equi': ('django.db.models.fields.CharField', [], {'default': "u'N'", 'max_length': '1', 'db_column': "u'TEM_TYPE_EQUI'"})
        },
        u'django_apogee.bourse': {
            'Meta': {'object_name': 'Bourse', 'db_table': "u'BOURSE'"},
            'cod_brs': ('django.db.models.fields.CharField', [], {'max_length': '2', 'primary_key': 'True', 'db_column': "u'COD_BRS'"}),
            'cod_soc': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_apogee.SitSociale']", 'null': 'True', 'db_column': "u'COD_SOC'"}),
            'lim1_brs': ('django.db.models.fields.CharField', [], {'max_length': '35', 'db_column': "u'LIM1_BRS'"})
        },
        u'django_apogee.catsocpfl': {
            'Meta': {'object_name': 'CatSocPfl', 'db_table': "u'CAT_SOC_PFL'"},
            'cod_pcs': ('django.db.models.fields.CharField', [], {'max_length': '2', 'primary_key': 'True', 'db_column': "u'COD_PCS'"}),
            'lib_pcs': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "u'LIB_PCS'"}),
            'lib_web_pcs': ('django.db.models.fields.CharField', [], {'max_length': '120', 'db_column': "u'LIB_WEB_PCS'"}),
            'tem_en_sve_pcs': ('django.db.models.fields.CharField', [], {'default': "u'O'", 'max_length': '1', 'db_column': "u'TEM_EN_SVE_PCS'"}),
            'tem_sai_qtr': ('django.db.models.fields.CharField', [], {'default': "u'O'", 'max_length': '1', 'db_column': "u'TEM_SAI_QTR'"})
        },
        u'django_apogee.centregestion': {
            'Meta': {'object_name': 'CentreGestion', 'db_table': "u'CENTRE_GESTION'"},
            'cod_cge': ('django.db.models.fields.CharField', [], {'max_length': '3', 'primary_key': 'True', 'db_column': "u'COD_CGE'"}),
            'lib_cge': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'db_column': "u'LIB_CGE'"})
        },
        u'django_apogee.cmphabilitervdi': {
            'Meta': {'object_name': 'CmpHabiliterVdi', 'db_table': "u'CMP_HABILITER_COPY'"},
            'cod_cmp': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_apogee.Composante']", 'db_column': "u'COD_CMP'"}),
            'cod_dip': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_apogee.Diplome']", 'db_column': "u'COD_DIP'"}),
            'cod_vrs_vdi': ('django.db.models.fields.CharField', [], {'max_length': '3', 'db_column': "u'COD_VRS_VDI'"}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '17', 'primary_key': 'True'}),
            'tem_en_sve_cvd': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'db_column': "u'TEM_EN_SVE_CVD'"})
        },
        u'django_apogee.cmphabilitervdiinitial': {
            'Meta': {'object_name': 'CmpHabiliterVdiInitial', 'db_table': "u'CMP_HABILITER_VDI'", 'managed': 'False'},
            'cod_cmp': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_apogee.Composante']", 'primary_key': 'True', 'db_column': "u'COD_CMP'"}),
            'cod_dip': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_apogee.Diplome']", 'db_column': "u'COD_DIP'"}),
            'cod_vrs_vdi': ('django.db.models.fields.CharField', [], {'max_length': '3', 'db_column': "u'COD_VRS_VDI'"}),
            'tem_en_sve_cvd': ('django.db.models.fields.CharField', [], {'max_length': '1', 'db_column': "u'TEM_EN_SVE_CVD'"})
        },
        u'django_apogee.combdi': {
            'Meta': {'ordering': "[u'lib_ach']", 'object_name': 'ComBdi', 'db_table': "u'COM_BDI_COPY'"},
            'cod_bdi': ('django.db.models.fields.CharField', [], {'max_length': '6', 'db_column': "u'COD_BDI'"}),
            'cod_com': ('django.db.models.fields.CharField', [], {'max_length': '6', 'db_column': "u'COD_COM'"}),
            'cod_fic_cbd': ('django.db.models.fields.CharField', [], {'max_length': '3', 'db_column': "u'COD_FIC_CBD'"}),
            'eta_ptc_ach': ('django.db.models.fields.CharField', [], {'max_length': '3', 'db_column': "u'ETA_PTC_ACH'"}),
            'eta_ptc_loc': ('django.db.models.fields.CharField', [], {'max_length': '3', 'db_column': "u'ETA_PTC_LOC'"}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '13', 'primary_key': 'True'}),
            'lib_ach': ('django.db.models.fields.CharField', [], {'max_length': '26', 'db_column': "u'LIB_ACH'"}),
            'tem_en_sve_cbd': ('django.db.models.fields.CharField', [], {'max_length': '3', 'db_column': "u'TEM_EN_SVE_CBD'"})
        },
        u'django_apogee.combdiinitial': {
            'Meta': {'ordering': "[u'lib_ach']", 'object_name': 'ComBdiInitial', 'db_table': "u'COM_BDI'", 'managed': 'False'},
            'cod_bdi': ('django.db.models.fields.CharField', [], {'max_length': '6', 'primary_key': 'True', 'db_column': "u'COD_BDI'"}),
            'cod_com': ('django.db.models.fields.CharField', [], {'max_length': '6', 'db_column': "u'COD_COM'"}),
            'cod_fic_cbd': ('django.db.models.fields.CharField', [], {'max_length': '3', 'db_column': "u'COD_FIC_CBD'"}),
            'eta_ptc_ach': ('django.db.models.fields.CharField', [], {'max_length': '3', 'db_column': "u'ETA_PTC_ACH'"}),
            'eta_ptc_loc': ('django.db.models.fields.CharField', [], {'max_length': '3', 'db_column': "u'ETA_PTC_LOC'"}),
            'lib_ach': ('django.db.models.fields.CharField', [], {'max_length': '26', 'db_column': "u'LIB_ACH'"}),
            'tem_en_sve_cbd': ('django.db.models.fields.CharField', [], {'max_length': '3', 'db_column': "u'TEM_EN_SVE_CBD'"})
        },
        u'django_apogee.composante': {
            'Meta': {'object_name': 'Composante', 'db_table': "u'COMPOSANTE'"},
            'cod_cmp': ('django.db.models.fields.CharField', [], {'max_length': '3', 'primary_key': 'True', 'db_column': "u'COD_CMP'"}),
            'cod_tpc': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'db_column': "u'COD_TPC'"}),
            'lib_cmp': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'db_column': "u'LIB_CMP'"})
        },
        u'django_apogee.departement': {
            'Meta': {'ordering': "[u'lib_dep']", 'object_name': 'Departement', 'db_table': "u'DEPARTEMENT'"},
            'cod_acd': ('django.db.models.fields.IntegerField', [], {'db_column': "u'COD_ACD'"}),
            'cod_dep': ('django.db.models.fields.CharField', [], {'max_length': '3', 'primary_key': 'True', 'db_column': "u'COD_DEP'"}),
            'lib_dep': ('django.db.models.fields.CharField', [], {'max_length': '60', 'db_column': "u'LIB_DEP'"}),
            'lic_dep': ('django.db.models.fields.CharField', [], {'max_length': '20', 'db_column': "u'LIC_DEP'"}),
            'tem_en_sve_dep': ('django.db.models.fields.CharField', [], {'max_length': '1', 'db_column': "u'TEM_EN_SVE_DEP'"})
        },
        u'django_apogee.diplome': {
            'Meta': {'object_name': 'Diplome', 'db_table': "u'DIPLOME'"},
            'cod_dip': ('django.db.models.fields.CharField', [], {'max_length': '7', 'primary_key': 'True', 'db_column': "u'COD_DIP'"}),
            'lib_dip': ('django.db.models.fields.CharField', [], {'max_length': '60', 'db_column': "u'LIB_DIP'"})
        },
        u'django_apogee.domaineactpfl': {
            'Meta': {'object_name': 'DomaineActPfl', 'db_table': "u'DOMAINE_ACT_PFL'"},
            'cod_dap': ('django.db.models.fields.CharField', [], {'max_length': '2', 'primary_key': 'True', 'db_column': "u'COD_DAP'"}),
            'lib_web_dap': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'db_column': "u'LIB_WEB_DAP'"})
        },
        u'django_apogee.elp': {
            'Meta': {'object_name': 'Elp', 'db_table': "u'ELEMENT_PEDAGOGI'"},
            'cod_cmp': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'centre_gestion_elp'", 'db_column': "u'COD_CMP'", 'to': u"orm['django_apogee.Composante']"}),
            'cod_elp': ('django.db.models.fields.CharField', [], {'max_length': '8', 'primary_key': 'True', 'db_column': "u'COD_ELP'"}),
            'eta_elp': ('django.db.models.fields.CharField', [], {'max_length': '1', 'db_column': "u'ETA_ELP'"}),
            'lib_elp': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        },
        u'django_apogee.elplibelle': {
            'Meta': {'object_name': 'ElpLibelle', 'db_table': "u'ELP_LIBELLE_COPY'"},
            'cod_elp': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_apogee.Elp']", 'db_column': "u'COD_ELP'"}),
            'cod_lng': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'db_column': "u'COD_LNG'"}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '13', 'primary_key': 'True'}),
            'lib_elp_lng': ('django.db.models.fields.CharField', [], {'max_length': '4000', 'null': 'True', 'db_column': "u'LIB_ELP_LNG'"})
        },
        u'django_apogee.elplibelleinitial': {
            'Meta': {'object_name': 'ElpLibelleInitial', 'db_table': "u'ELP_LIBELLE'"},
            'cod_elp': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_apogee.Elp']", 'primary_key': 'True', 'db_column': "u'COD_ELP'"}),
            'cod_lng': ('django.db.models.fields.CharField', [], {'max_length': '4', 'db_column': "u'COD_LNG'"}),
            'lib_elp_lng': ('django.db.models.fields.CharField', [], {'max_length': '4000', 'null': 'True', 'db_column': "u'LIB_ELP_LNG'"})
        },
        u'django_apogee.etablissement': {
            'Meta': {'ordering': "[u'lib_etb']", 'object_name': 'Etablissement', 'db_table': "u'ETABLISSEMENT'"},
            'cod_aff_dep_etb': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'db_column': "u'COD_AFF_DEP_ETB'"}),
            'cod_aff_etb': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'db_column': "u'COD_AFF_ETB'"}),
            'cod_dep': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_apogee.Departement']", 'db_column': "u'COD_DEP'"}),
            'cod_etb': ('django.db.models.fields.CharField', [], {'max_length': '8', 'primary_key': 'True', 'db_column': "u'COD_ETB'"}),
            'cod_pay_adr_etb': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_apogee.Pays']", 'null': 'True', 'db_column': "u'COD_PAY_ADR_ETB'"}),
            'cod_pos_adr_etb': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '20', 'null': 'True', 'db_column': "u'COD_POS_ADR_ETB'"}),
            'cod_tpe': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_apogee.TypEtb']", 'db_column': "u'COD_TPE'"}),
            'lib_art_off_etb': ('django.db.models.fields.CharField', [], {'max_length': '5', 'db_column': "u'LIB_ART_OFF_ETB'"}),
            'lib_etb': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "u'LIB_ETB'"}),
            'lib_off_etb': ('django.db.models.fields.CharField', [], {'max_length': '60', 'db_column': "u'LIB_OFF_ETB'"}),
            'tem_aut_sis_etb': ('django.db.models.fields.CharField', [], {'default': "u'O'", 'max_length': '1', 'db_column': "u'TEM_AUT_SIS_ETB'"}),
            'tem_en_sve_etb': ('django.db.models.fields.CharField', [], {'default': "u'O'", 'max_length': '1', 'db_column': "u'TEM_EN_SVE_ETB'"})
        },
        u'django_apogee.etape': {
            'Meta': {'object_name': 'Etape', 'db_table': "u'ETAPE'"},
            'cod_cur': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'db_column': "u'COD_CUR'"}),
            'cod_cyc': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'db_column': "u'COD_CYC'"}),
            'cod_etp': ('django.db.models.fields.CharField', [], {'max_length': '6', 'primary_key': 'True', 'db_column': "u'COD_ETP'"}),
            'lib_etp': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'db_column': "u'LIB_ETP'"})
        },
        u'django_apogee.etpgerercge': {
            'Meta': {'object_name': 'EtpGererCge', 'db_table': "u'ETP_GERER_CGE'"},
            'cod_cge': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'etape_centre_gestion'", 'db_column': "u'COD_CGE'", 'to': u"orm['django_apogee.CentreGestion']"}),
            'cod_cmp': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_apogee.Composante']", 'db_column': "u'COD_CMP'"}),
            'cod_etp': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_apogee.Etape']", 'primary_key': 'True', 'db_column': "u'COD_ETP'"})
        },
        u'django_apogee.individu': {
            'Meta': {'object_name': 'Individu', 'db_table': "u'INDIVIDU'"},
            'cod_cle_nne_ind': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'db_column': "u'COD_CLE_NNE_IND'"}),
            'cod_etu': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'COD_ETU'"}),
            'cod_fam': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'db_column': "u'COD_FAM'"}),
            'cod_ind': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'COD_IND'"}),
            'cod_ind_opi': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'COD_IND_OPI'"}),
            'cod_nne_ind': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'db_column': "u'COD_NNE_IND'"}),
            'cod_sex_etu': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'db_column': "u'COD_SEX_ETU'"}),
            'dat_cre_ind': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'DAT_CRE_IND'"}),
            'dat_mod_ind': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'DAT_MOD_IND'"}),
            'date_nai_ind': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'DATE_NAI_IND'"}),
            'lib_nom_pat_ind': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'db_column': "u'LIB_NOM_PAT_IND'"}),
            'lib_nom_usu_ind': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'db_column': "u'LIB_NOM_USU_IND'"}),
            'lib_pr1_ind': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'db_column': "u'LIB_PR1_IND'"}),
            'lib_pr2_ind': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'db_column': "u'LIB_PR2_IND'"}),
            'lib_pr3_ind': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'db_column': "u'LIB_PR3_IND'"})
        },
        u'django_apogee.indopi': {
            'Meta': {'object_name': 'IndOpi', 'db_table': "u'IND_OPI'", 'managed': 'False'},
            'adr_mail_opi': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'db_column': "u'ADR_MAIL_OPI'"}),
            'cod_cle_nne_ind_opi': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'db_column': "u'COD_CLE_NNE_IND_OPI'"}),
            'cod_dap': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'db_column': "u'COD_DAP'"}),
            'cod_dep_pay_ann_pre_opi': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'db_column': "u'COD_DEP_PAY_ANN_PRE_OPI'"}),
            'cod_dep_pay_ant_iaa_opi': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'db_column': "u'COD_DEP_PAY_ANT_IAA_OPI'"}),
            'cod_dep_pay_der_dip': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'db_column': "u'COD_DEP_PAY_DER_DIP'"}),
            'cod_dep_pay_nai': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'db_column': "u'COD_DEP_PAY_NAI'"}),
            'cod_etb': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'db_column': "u'COD_ETB'"}),
            'cod_etb_ann_crt': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'db_column': "u'COD_ETB_ANN_CRT'"}),
            'cod_etb_ann_pre_opi': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'db_column': "u'COD_ETB_ANN_PRE_OPI'"}),
            'cod_etb_ant_iaa': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'db_column': "u'COD_ETB_ANT_IAA'"}),
            'cod_etb_der_dip': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'db_column': "u'COD_ETB_DER_DIP'"}),
            'cod_etu_opi': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'cod_fam': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'db_column': "u'COD_FAM'"}),
            'cod_ind': ('django.db.models.fields.IntegerField', [], {'db_column': "u'COD_IND'"}),
            'cod_ind_opi': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'COD_IND_OPI'"}),
            'cod_nne_ind_opi': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'db_column': "u'COD_NNE_IND_OPI'"}),
            'cod_opi_int_epo': ('django.db.models.fields.CharField', [], {'max_length': '10', 'db_column': "u'COD_OPI_INT_EPO'"}),
            'cod_pay_nat': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'db_column': "u'COD_PAY_NAT'"}),
            'cod_pcs': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'db_column': "u'COD_PCS'"}),
            'cod_pcs_ap': ('django.db.models.fields.CharField', [], {'default': "u'99'", 'max_length': '2', 'null': 'True', 'db_column': "u'COD_PCS_AP'"}),
            'cod_sex_etu_opi': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'db_column': "u'COD_SEX_ETU_OPI'"}),
            'cod_sim': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'db_column': "u'COD_SIM'"}),
            'cod_sis_ann_pre_opi': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'db_column': "u'COD_SIS_ANN_PRE_OPI'"}),
            'cod_tde_der_dip': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'db_column': "u'COD_TDE_DER_DIP'"}),
            'cod_tds_opi': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'db_column': "u'COD_TDS_OPI'"}),
            'cod_thb_opi': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'db_column': "u'COD_THB_OPI'"}),
            'cod_thp_opi': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'db_column': "u'COD_THP_OPI'"}),
            'cod_tpe_ann_crt': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'db_column': "u'COD_TPE_ANN_CRT'"}),
            'cod_tpe_ant_iaa': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'db_column': "u'COD_TPE_ANT_IAA'"}),
            'cod_typ_dep_pay_ann_pre_opi': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'db_column': "u'COD_TYP_DEP_PAY_ANN_PRE_OPI'"}),
            'cod_typ_dep_pay_ant_iaa_opi': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'db_column': "u'COD_TYP_DEP_PAY_ANT_IAA_OPI'"}),
            'cod_typ_dep_pay_der_dip': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'db_column': "u'COD_TYP_DEP_PAY_DER_DIP'"}),
            'cod_typ_dep_pay_nai': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'db_column': "u'COD_TYP_DEP_PAY_NAI'"}),
            'daa_ens_sup_opi': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'db_column': "u'DAA_ENS_SUP_OPI'"}),
            'daa_ent_etb_opi': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'db_column': "u'DAA_ENT_ETB_OPI'"}),
            'daa_etb_ant_iaa_opi': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'db_column': "u'DAA_ETB_ANT_IAA_OPI'"}),
            'daa_etb_der_dip': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'db_column': "u'DAA_ETB_DER_DIP'"}),
            'daa_etb_opi': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'db_column': "u'DAA_ETB_OPI'"}),
            'daa_etr_sup': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'db_column': "u'DAA_ETR_SUP'"}),
            'daa_lbt_ind_opi': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'db_column': "u'DAA_LBT_IND_OPI'"}),
            'date_nai_ind_opi': ('django.db.models.fields.DateField', [], {'db_column': "u'DATE_NAI_IND_OPI'"}),
            'dmm_lbt_ind_opi': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'db_column': "u'DMM_LBT_IND_OPI'"}),
            'lib_nom_pat_ind_opi': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_column': "u'LIB_NOM_PAT_IND_OPI'"}),
            'lib_nom_usu_ind_opi': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'db_column': "u'LIB_NOM_USU_IND_OPI'"}),
            'lib_pr1_ind_opi': ('django.db.models.fields.CharField', [], {'max_length': '20', 'db_column': "u'LIB_PR1_IND_OPI'"}),
            'lib_pr2_ind_opi': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'db_column': "u'LIB_PR2_IND_OPI'"}),
            'lib_pr3_ind_opi': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'db_column': "u'LIB_PR3_IND_OPI'"}),
            'lib_vil_nai_etu_opi': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'db_column': "u'LIB_VIL_NAI_ETU_OPI'"}),
            'nb_enf_etu_opi': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NB_ENF_ETU_OPI'"}),
            'num_tel_ind_opi': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'db_column': "u'NUM_TEL_IND_OPI'"}),
            'num_tel_por_opi': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'db_column': "u'NUM_TEL_POR_OPI'"}),
            'tem_date_nai_rel_opi': ('django.db.models.fields.CharField', [], {'default': "u'N'", 'max_length': '1', 'db_column': "u'TEM_DATE_NAI_REL_OPI'"}),
            'tem_mi_tps_epo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TEM_MI_TPS_EPO'"})
        },
        u'django_apogee.insadmetp': {
            'Meta': {'object_name': 'InsAdmEtp', 'db_table': "u'INS_ADM_ETP_COPY'"},
            'cod_anu': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_apogee.AnneeUni']"}),
            'cod_cge': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'db_column': "u'COD_CGE'"}),
            'cod_dip': ('django.db.models.fields.CharField', [], {'max_length': '7', 'null': 'True', 'db_column': "u'COD_DIP'"}),
            'cod_etp': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'db_column': "u'COD_ETP'"}),
            'cod_ind': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'etapes_ied'", 'db_column': "u'COD_IND'", 'to': u"orm['django_apogee.Individu']"}),
            'cod_pru': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'db_column': "u'COD_PRU'"}),
            'cod_vrs_vet': ('django.db.models.fields.CharField', [], {'max_length': '3', 'db_column': "u'COD_VRS_VET'"}),
            'dat_annul_res_iae': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'DAT_ANNUL_RES_IAE'"}),
            'dat_cre_iae': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'DAT_CRE_IAE'"}),
            'dat_mod_iae': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'DAT_MOD_IAE'"}),
            'eta_iae': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'db_column': "u'ETA_IAE'"}),
            'eta_pmt_iae': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'db_column': "u'ETA_PMT_IAE'"}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '30', 'primary_key': 'True'}),
            'nbr_ins_cyc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NBR_INS_CYC'"}),
            'nbr_ins_dip': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NBR_INS_DIP'"}),
            'nbr_ins_etp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NBR_INS_ETP'"}),
            'num_occ_iae': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'db_column': "u'NUM_OCC_IAE'"}),
            'tem_iae_prm': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'db_column': "u'TEM_IAE_PRM'"})
        },
        u'django_apogee.insadmetpinitial': {
            'Meta': {'object_name': 'InsAdmEtpInitial', 'db_table': "u'INS_ADM_ETP'", 'managed': 'False'},
            'cod_anu': ('django.db.models.fields.CharField', [], {'max_length': '4', 'db_column': "u'COD_ANU'"}),
            'cod_cge': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'db_column': "u'COD_CGE'"}),
            'cod_dip': ('django.db.models.fields.CharField', [], {'max_length': '7', 'null': 'True', 'db_column': "u'COD_DIP'"}),
            'cod_etp': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True', 'db_column': "u'COD_ETP'"}),
            'cod_ind': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'etapes'", 'primary_key': 'True', 'db_column': "u'COD_IND'", 'to': u"orm['django_apogee.Individu']"}),
            'cod_pru': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'db_column': "u'COD_PRU'"}),
            'cod_vrs_vet': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'db_column': "u'COD_VRS_VET'"}),
            'dat_annul_res_iae': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'DAT_ANNUL_RES_IAE'"}),
            'dat_cre_iae': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'DAT_CRE_IAE'"}),
            'dat_mod_iae': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'DAT_MOD_IAE'"}),
            'eta_iae': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'db_column': "u'ETA_IAE'"}),
            'eta_pmt_iae': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'db_column': "u'ETA_PMT_IAE'"}),
            'nbr_ins_cyc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NBR_INS_CYC'"}),
            'nbr_ins_dip': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NBR_INS_DIP'"}),
            'nbr_ins_etp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NBR_INS_ETP'"}),
            'num_occ_iae': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'db_column': "u'NUM_OCC_IAE'"}),
            'tem_iae_prm': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'db_column': "u'TEM_IAE_PRM'"})
        },
        u'django_apogee.mentionbac': {
            'Meta': {'object_name': 'MentionBac', 'db_table': "u'MENTION_NIV_BAC'"},
            'cod_mnb': ('django.db.models.fields.CharField', [], {'max_length': '2', 'primary_key': 'True', 'db_column': "u'COD_MNB'"}),
            'lib_mnb': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "u'LIB_MNB'"}),
            'lic_mnb': ('django.db.models.fields.CharField', [], {'max_length': '20', 'db_column': "u'LIC_MNB'"}),
            'tem_en_sve_mnb': ('django.db.models.fields.CharField', [], {'default': "u'O'", 'max_length': '1', 'db_column': "u'TEM_EN_SVE_MNB'"})
        },
        u'django_apogee.mtfnonaflsso': {
            'Meta': {'object_name': 'MtfNonAflSso', 'db_table': "u'MTF_NON_AFL_SSO'"},
            'cod_mns': ('django.db.models.fields.CharField', [], {'max_length': '1', 'primary_key': 'True', 'db_column': "u'COD_MNS'"}),
            'lib_mns': ('django.db.models.fields.CharField', [], {'max_length': '40', 'db_column': "u'LIB_MNS'"}),
            'lic_mns': ('django.db.models.fields.CharField', [], {'max_length': '10', 'db_column': "u'LIC_MNS'"}),
            'tem_del': ('django.db.models.fields.CharField', [], {'default': "u'O'", 'max_length': '1', 'db_column': "u'TEM_DEL'"}),
            'tem_en_sve_mns': ('django.db.models.fields.CharField', [], {'default': "u'O'", 'max_length': '1', 'db_column': "u'TEM_EN_SVE_MNS'"})
        },
        u'django_apogee.opibac': {
            'Meta': {'object_name': 'OpiBac', 'db_table': "u'OPI_BAC'", 'managed': 'False'},
            'cod_bac': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'db_column': "u'COD_BAC'"}),
            'cod_dep': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'db_column': "u'COD_DEP'"}),
            'cod_etb': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'db_column': "u'COD_ETB'"}),
            'cod_ind_opi': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'COD_IND_OPI'"}),
            'cod_mnb': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'db_column': "u'COD_MNB'"}),
            'cod_tpe': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'db_column': "u'COD_TPE'"}),
            'daa_obt_bac_oba': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'db_column': "u'DAA_OBT_BAC_OBA'"})
        },
        u'django_apogee.pays': {
            'Meta': {'ordering': "[u'lic_pay']", 'object_name': 'Pays', 'db_table': "u'PAYS'"},
            'cod_pay': ('django.db.models.fields.CharField', [], {'max_length': '3', 'primary_key': 'True', 'db_column': "u'COD_PAY'"}),
            'cod_sis_pay': ('django.db.models.fields.CharField', [], {'max_length': '3', 'db_column': "u'COD_SIS_PAY'"}),
            'lib_nat': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "u'LIB_NAT'"}),
            'lib_pay': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "u'LIB_PAY'"}),
            'lic_pay': ('django.db.models.fields.CharField', [], {'max_length': '20', 'db_column': "u'LIC_PAY'"}),
            'tem_afl_dec_ind_pay': ('django.db.models.fields.CharField', [], {'max_length': '1', 'db_column': "u'TEM_AFL_DEC_IND_PAY'"}),
            'tem_del': ('django.db.models.fields.CharField', [], {'max_length': '1', 'db_column': "u'TEM_DEL'"}),
            'tem_en_sve_pay': ('django.db.models.fields.CharField', [], {'max_length': '1', 'db_column': "u'TEM_EN_SVE_PAY'"}),
            'tem_ouv_drt_sso_pay': ('django.db.models.fields.CharField', [], {'max_length': '1', 'db_column': "u'TEM_OUV_DRT_SSO_PAY'"})
        },
        u'django_apogee.quotitetra': {
            'Meta': {'object_name': 'QuotiteTra', 'db_table': "u'QUOTITE_TRA'"},
            'cod_qtr': ('django.db.models.fields.CharField', [], {'max_length': '1', 'primary_key': 'True', 'db_column': "u'COD_QTR'"}),
            'lib_qtr': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "u'LIB_QTR'"}),
            'lib_web_qtr': ('django.db.models.fields.CharField', [], {'max_length': '120', 'db_column': "u'LIB_WEB_QTR'"}),
            'lic_qtr': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "u'LIC_QTR'"}),
            'lim1_qtr': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "u'LIM1_QTR'"}),
            'tem_cou_aut_reg_qtr': ('django.db.models.fields.CharField', [], {'default': "u'O'", 'max_length': '1', 'db_column': "u'TEM_COU_AUT_REG_QTR'"}),
            'tem_en_sve_qtr': ('django.db.models.fields.CharField', [], {'default': "u'O'", 'max_length': '1', 'db_column': "u'TEM_EN_SVE_QTR'"})
        },
        u'django_apogee.regimeparent': {
            'Meta': {'object_name': 'RegimeParent', 'db_table': "u'REGIME_PARENT'"},
            'cod_rgp': ('django.db.models.fields.CharField', [], {'max_length': '2', 'primary_key': 'True', 'db_column': "u'COD_RGP'"}),
            'lib_rgp': ('django.db.models.fields.CharField', [], {'max_length': '280', 'db_column': "u'LIB_RGP'"}),
            'ordre_tri_rgp': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'db_column': "u'ORDRE_TRI_RGP'"})
        },
        u'django_apogee.sitfam': {
            'Meta': {'object_name': 'SitFam', 'db_table': "u'SIT_FAM'"},
            'cod_fam': ('django.db.models.fields.CharField', [], {'max_length': '1', 'primary_key': 'True', 'db_column': "u'COD_FAM'"}),
            'cod_sis_fam': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'db_column': "u'COD_SIS_FAM'", 'blank': 'True'}),
            'lib_fam': ('django.db.models.fields.CharField', [], {'max_length': '40', 'db_column': "u'LIB_FAM'"}),
            'lic_fam': ('django.db.models.fields.CharField', [], {'max_length': '10', 'db_column': "u'LIC_FAM'"}),
            'tem_en_sve_fam': ('django.db.models.fields.CharField', [], {'default': "u'O'", 'max_length': '1', 'db_column': "u'TEM_EN_SVE_FAM'"})
        },
        u'django_apogee.sitmil': {
            'Meta': {'object_name': 'SitMil', 'db_table': "u'SIT_MIL'"},
            'cod_sim': ('django.db.models.fields.CharField', [], {'max_length': '1', 'primary_key': 'True', 'db_column': "u'COD_SIM'"}),
            'lib_sim': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "u'LIB_SIM'"}),
            'lic_sim': ('django.db.models.fields.CharField', [], {'max_length': '20', 'db_column': "u'LIC_SIM'"}),
            'tem_del_dip': ('django.db.models.fields.CharField', [], {'default': "u'N'", 'max_length': '1', 'db_column': "u'TEM_DEL_DIP'"}),
            'tem_en_sve_sim': ('django.db.models.fields.CharField', [], {'default': "u'O'", 'max_length': '1', 'db_column': "u'TEM_EN_SVE_SIM'"}),
            'tem_sai_dmm_lbt': ('django.db.models.fields.CharField', [], {'default': "u'O'", 'max_length': '1', 'db_column': "u'TEM_SAI_DMM_LBT'"})
        },
        u'django_apogee.sitsociale': {
            'Meta': {'object_name': 'SitSociale', 'db_table': "u'SIT_SOCIALE'"},
            'cod_soc': ('django.db.models.fields.CharField', [], {'max_length': '2', 'primary_key': 'True', 'db_column': "u'COD_SOC'"}),
            'lib_soc': ('django.db.models.fields.CharField', [], {'max_length': '35', 'db_column': "u'LIM1_SOC'"}),
            'lic_soc': ('django.db.models.fields.CharField', [], {'max_length': '35', 'db_column': "u'LIB_SOC'"}),
            'tem_del': ('django.db.models.fields.CharField', [], {'max_length': '1', 'db_column': "u'TEM_DEL'"}),
            'tem_en_sve_soc': ('django.db.models.fields.CharField', [], {'max_length': '1', 'db_column': "u'TEM_EN_SVE_SOC'"})
        },
        u'django_apogee.situationsise': {
            'Meta': {'object_name': 'SituationSise', 'db_table': "u'SITUATION_SISE'"},
            'cod_sis': ('django.db.models.fields.CharField', [], {'max_length': '1', 'primary_key': 'True', 'db_column': "u'COD_SIS'"}),
            'lib_sis': ('django.db.models.fields.CharField', [], {'max_length': '130', 'db_column': "u'LIB_SIS'"}),
            'tem_en_sve_sis': ('django.db.models.fields.CharField', [], {'default': "u'O'", 'max_length': '1', 'db_column': "u'TEM_EN_SVE_SIS'"})
        },
        u'django_apogee.specialitevdi': {
            'Meta': {'object_name': 'SpecialiteVdi', 'db_table': "u'SPECIALITE_VDI'"},
            'cod_svd': ('django.db.models.fields.CharField', [], {'max_length': '6', 'primary_key': 'True', 'db_column': "u'COD_SVD'"}),
            'lib_svd': ('django.db.models.fields.CharField', [], {'max_length': '400', 'db_column': "u'LIB_SVD'"}),
            'tem_en_sve_svd': ('django.db.models.fields.CharField', [], {'max_length': '1', 'db_column': "u'TEM_EN_SVE_SVD'"})
        },
        u'django_apogee.typediplomeext': {
            'Meta': {'object_name': 'TypeDiplomeExt', 'db_table': "u'TYP_DIPLOME_EXT'"},
            'cod_tde': ('django.db.models.fields.CharField', [], {'max_length': '3', 'primary_key': 'True', 'db_column': "u'COD_TDE'"}),
            'lib_tde': ('django.db.models.fields.CharField', [], {'max_length': '130', 'db_column': "u'LIB_TDE'"}),
            'lib_web_tde': ('django.db.models.fields.CharField', [], {'max_length': '130', 'db_column': "u'LIB_WEB_TDE'"}),
            'tem_en_sve_tde': ('django.db.models.fields.CharField', [], {'default': "u'O'", 'max_length': '1', 'db_column': "u'TEM_EN_SVE_TDE'"})
        },
        u'django_apogee.typetb': {
            'Meta': {'object_name': 'TypEtb', 'db_table': "u'TYP_ETB'"},
            'cod_sis_tpe': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'db_column': "u'COD_SIS_TPE'"}),
            'cod_tpe': ('django.db.models.fields.CharField', [], {'max_length': '2', 'primary_key': 'True', 'db_column': "u'COD_TPE'"}),
            'lib_tpe': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "u'LIB_TPE'"}),
            'lic_tpe': ('django.db.models.fields.CharField', [], {'max_length': '20', 'db_column': "u'LIC_TPE'"}),
            'tem_det_tpe': ('django.db.models.fields.CharField', [], {'default': "u'O'", 'max_length': '1', 'db_column': "u'TEM_DET_TPE'"}),
            'tem_en_sve_tpe': ('django.db.models.fields.CharField', [], {'default': "u'O'", 'max_length': '1', 'db_column': "u'TEM_EN_SVE_TPE'"}),
            'tem_ges_trf_tpe': ('django.db.models.fields.CharField', [], {'default': "u'O'", 'max_length': '1', 'db_column': "u'TEM_GES_TRF_TPE'"}),
            'tem_prop_autre_etb': ('django.db.models.fields.CharField', [], {'default': "u'N'", 'max_length': '1', 'db_column': "u'TEM_PROP_AUTRE_ETB'"})
        },
        u'django_apogee.typhandicap': {
            'Meta': {'object_name': 'TypHandicap', 'db_table': "u'TYP_HANDICAP'"},
            'cod_thp': ('django.db.models.fields.CharField', [], {'max_length': '2', 'primary_key': 'True', 'db_column': "u'COD_THP'"}),
            'lib_thp': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "u'LIB_THP'"}),
            'lic_thp': ('django.db.models.fields.CharField', [], {'max_length': '20', 'db_column': "u'LIC_THP'"}),
            'tem_en_sve_thp': ('django.db.models.fields.CharField', [], {'default': "u'O'", 'max_length': '1', 'db_column': "u'TEM_EN_SVE_THP'"}),
            'tem_tie_tps': ('django.db.models.fields.CharField', [], {'default': "u'O'", 'max_length': '1', 'db_column': "u'TEM_TIE_TPS'"})
        },
        u'django_apogee.typhebergement': {
            'Meta': {'object_name': 'TypHebergement', 'db_table': "u'TYP_HEBERGEMENT'"},
            'cod_thb': ('django.db.models.fields.CharField', [], {'max_length': '1', 'primary_key': 'True', 'db_column': "u'COD_THB'"}),
            'lib_thb': ('django.db.models.fields.CharField', [], {'max_length': '60', 'db_column': "u'LIB_THB'"}),
            'tem_en_sve_thb': ('django.db.models.fields.CharField', [], {'default': "u'O'", 'max_length': '1', 'db_column': "u'TEM_EN_SVE_THB'"})
        },
        u'django_apogee.vdifractionnervet': {
            'Meta': {'object_name': 'VdiFractionnerVet', 'db_table': "u'VDI_FRACTIONNER_VET_COPY'"},
            'cod_dip': ('django.db.models.fields.CharField', [], {'max_length': '7', 'db_column': "u'COD_DIP'"}),
            'cod_etp': ('django.db.models.fields.CharField', [], {'max_length': '6', 'db_column': "u'COD_ETP'"}),
            'cod_sis_daa_min': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'db_column': "u'COD_SIS_DAA_MIN'"}),
            'cod_vrs_vdi': ('django.db.models.fields.CharField', [], {'max_length': '3', 'db_column': "u'COD_VRS_VDI'"}),
            'cod_vrs_vet': ('django.db.models.fields.CharField', [], {'max_length': '3', 'db_column': "u'COD_VRS_VET'"}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '22', 'primary_key': 'True'})
        },
        u'django_apogee.vdifractionnervetinitial': {
            'Meta': {'object_name': 'VdiFractionnerVetInitial', 'db_table': "u'VDI_FRACTIONNER_VET'", 'managed': 'False'},
            'cod_dip': ('django.db.models.fields.CharField', [], {'max_length': '7', 'db_column': "u'COD_DIP'"}),
            'cod_etp': ('django.db.models.fields.CharField', [], {'max_length': '6', 'primary_key': 'True', 'db_column': "u'COD_ETP'"}),
            'cod_sis_daa_min': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'db_column': "u'COD_SIS_DAA_MIN'"}),
            'cod_vrs_vdi': ('django.db.models.fields.CharField', [], {'max_length': '3', 'db_column': "u'COD_VRS_VDI'"}),
            'cod_vrs_vet': ('django.db.models.fields.CharField', [], {'max_length': '3', 'db_column': "u'COD_VRS_VET'"})
        },
        u'django_apogee.versiondiplome': {
            'Meta': {'object_name': 'VersionDiplome', 'db_table': "u'VERSION_DIPLOME_COPY'"},
            'cod_dip': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_apogee.Diplome']", 'max_length': '7', 'db_column': "u'COD_DIP'"}),
            'cod_svd': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_apogee.SpecialiteVdi']", 'null': 'True', 'db_column': "u'COD_SVD'"}),
            'cod_vrs_vdi': ('django.db.models.fields.CharField', [], {'max_length': '3', 'db_column': "u'COD_VRS_VDI'"}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '11', 'primary_key': 'True'}),
            'lic_vdi': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'db_column': "u'LIC_VDI'"})
        },
        u'django_apogee.versiondiplomeinitial': {
            'Meta': {'object_name': 'VersionDiplomeInitial', 'db_table': "u'VERSION_DIPLOME'", 'managed': 'False'},
            'cod_dip': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_apogee.Diplome']", 'max_length': '7', 'primary_key': 'True', 'db_column': "u'COD_DIP'"}),
            'cod_svd': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_apogee.SpecialiteVdi']", 'null': 'True', 'db_column': "u'COD_SVD'"}),
            'cod_vrs_vdi': ('django.db.models.fields.CharField', [], {'max_length': '3', 'db_column': "u'COD_VRS_VDI'"}),
            'lic_vdi': ('django.db.models.fields.CharField', [], {'max_length': '25', 'db_column': "u'LIC_VDI'"})
        },
        u'django_apogee.versionetape': {
            'Meta': {'object_name': 'VersionEtape', 'db_table': "u'VERSION_ETAPE_COPY'"},
            'cod_etp': ('django.db.models.fields.CharField', [], {'max_length': '6', 'db_column': "u'COD_ETP'"}),
            'cod_vrs_vet': ('django.db.models.fields.CharField', [], {'max_length': '3', 'db_column': "u'COD_VRS_VET'"}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '10', 'primary_key': 'True'})
        },
        u'django_apogee.versionetapeinitial': {
            'Meta': {'object_name': 'VersionEtapeInitial', 'db_table': "u'VERSION_ETAPE'", 'managed': 'False'},
            'cod_etp': ('django.db.models.fields.CharField', [], {'max_length': '6', 'primary_key': 'True', 'db_column': "u'COD_ETP'"}),
            'cod_vrs_vet': ('django.db.models.fields.CharField', [], {'max_length': '3', 'db_column': "u'COD_VRS_VET'"})
        }
    }

    complete_apps = ['django_apogee']