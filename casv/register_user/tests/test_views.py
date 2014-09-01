# -*- coding: utf-8 -*-
from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from ..models import UserEmail


class RegisterUserTest(TestCase):
    def setUp(self):
        UserEmail.objects.create(email='i@brasil.gov.br')
        UserEmail.objects.create(email='e@brasil.gov.br')

    def test_register_user(self):
        data = {
            'email': 'i@brasil.gov.br',
            'password': 'password',
            'first_name': 'test',
            'last_name': 'yes'
            }
        wrong_data = {
            'email': 'a@brasil.gov.br',
            'password': 'password'
            }
        self.client.post(reverse('register:register'), data)
        self.client.post(reverse('register:register'), data)
        self.client.post(reverse('register:register'), wrong_data)
        #self.assertEqual(User.objects.all().count(), 1)
        self.assertEqual(
            User.objects.get(email='i@brasil.gov.br').first_name,
            data.get('first_name')
            )
        self.assertEqual(
            User.objects.get(email='i@brasil.gov.br').last_name,
            data.get('last_name')
            )

    def test_register_only_required_fields(self):
        basic_data = {
            'email': 'e@brasil.gov.br',
            'password': 'password',
            }
        self.client.post(reverse('register:register'), basic_data)
        #self.assertEqual(User.objects.all().count(), 1)
