# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_apogee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='individu',
            name='cod_civ',
            field=models.CharField(max_length=1, null=True, verbose_name='Code civilit\xe9', db_column='COD_CIV'),
        ),
        migrations.AddField(
            model_name='individu',
            name='cod_cle_nni_etu',
            field=models.CharField(max_length=2, null=True, verbose_name="cl\xe9 du num\xe9ro INSEE de l'\xe9tudiant", db_column='COD_CLE_NNI_ETU'),
        ),
        migrations.AddField(
            model_name='individu',
            name='cod_dep_pay_nai',
            field=models.CharField(max_length=3, null=True, verbose_name='D\xe9partement ou pays de naissance', db_column='COD_DEP_PAY_NAI'),
        ),
        migrations.AddField(
            model_name='individu',
            name='cod_nni_etu',
            field=models.CharField(max_length=13, null=True, verbose_name="Numero INSEE de l'etudiant", db_column='COD_NNI_ETU'),
        ),
        migrations.AddField(
            model_name='individu',
            name='cod_typ_dep_pay_nai',
            field=models.CharField(max_length=1, null=True, verbose_name='Type D\xe9partement ou pays de naissance', db_column='COD_TYP_DEP_PAY_NAI'),
        ),
        migrations.AddField(
            model_name='individu',
            name='eta_coh_dos_ind',
            field=models.CharField(max_length=4, null=True, verbose_name='Etat de coh\xe9rance du dossier individu', db_column='ETA_COH_DOS_IND', choices=[('CRIA', 'CRIA'), ('CRIP', 'CRIP'), ('MCIA', 'MCIA'), ('MSIA', 'MSIA'), ('VAIA', 'VAIA')]),
        ),
        migrations.AddField(
            model_name='individu',
            name='eta_prs_etu',
            field=models.CharField(db_column='ETA_PRS_ETU', default='O', choices=[('N', 'N'), ('O', 'O')], max_length=1, null=True, verbose_name='Code pr\xe9sence \xe9tudiant'),
        ),
        migrations.AddField(
            model_name='individu',
            name='lib_vil_nai_etu',
            field=models.CharField(max_length=4, null=True, verbose_name='lib', db_column='LIB_VIL_NAI_ETU'),
        ),
        migrations.AddField(
            model_name='individu',
            name='num_brs_etu',
            field=models.CharField(max_length=13, null=True, verbose_name='Numero boursier etudiant', db_column='NUM_BRS_ETU'),
        ),
        migrations.AddField(
            model_name='individu',
            name='tem_crt_sso_etu',
            field=models.CharField(max_length=1, null=True, verbose_name='Temoin possession carte securite sociale', db_column='TEM_CRT_SSO_ETU'),
        ),
        migrations.AddField(
            model_name='insadmanu',
            name='cod_pru',
            field=models.CharField(max_length=2, null=True, verbose_name='Code profil etudiant', db_column='COD_PRU'),
        ),
    ]
