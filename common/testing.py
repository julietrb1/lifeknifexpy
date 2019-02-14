from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient


class AuthTestCase(TestCase):
    def setUp(self):
        self.c = APIClient()
        self.user = User.objects.create_user(username='test', password='pass')
        self.c.force_authenticate(self.user)
