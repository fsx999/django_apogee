# -*- coding: utf-8 -*-
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.test import TestCase
from apogee.models import AnneeUni


class CreationTest(TestCase):

    def test_succes_login(self):
        AnneeUni.objects.create(cod_anu=2012, eta_anu_iae="0")
        print AnneeUni.objects.count()
        # de l'url de connection


# class LoginFormTest(TestCase):
#     fixtures = ['user.json']
#
#     def setUp(self):
#         pass
#
#     def tearDown(self):
#         pass
#
#     def testLoginForm(self):
#         form_login = LoginIED(data={'username': "paul", 'password': 'naharisoa'})
#         self.assertTrue(form_login.is_valid())
#         form_login = LoginIED({'username': "toto0", 'password': 'naharisoa'})
#         self.assertFalse(form_login.is_valid())
#
#
# class SignalTest(TestCase):
#     fixtures = ['user.json']
#
#     def testSignal(self):
#         user = User.objects.get(username="paul")
#         user_activated.send(sender=None, user=user, request=None)
#         self.assertEquals(Individu.objects.count(), 1)
