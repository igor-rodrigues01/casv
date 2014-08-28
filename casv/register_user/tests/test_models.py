from django.test import TestCase
from django.core import mail

from ..models import UserEmail


class TestUserEmail(TestCase):
    def setUp(self):
        self.email = 'a@e.gov.br'
        self.useremail = UserEmail.objects.create(email=self.email)

    def test_useremail_creation(self):
        self.assertIsInstance(self.useremail, UserEmail)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(self.useremail.__str__(), '%s' % self.email)