# -*- coding: utf-8 -*-
from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from ..models import UserEmail


class RegisterUserTest(TestCase):
    def setUp(self):
        UserEmail.objects.create(email='i@brasil.gov.br')

    def test_register_user(self):
        data = {
            'email': 'i@brasil.gov.br',
            'password': 'password'
            }
        self.client.post(reverse('register:register'), data)
        self.client.post(reverse('register:register'), data)
        self.assertEqual(User.objects.all().count(), 1)