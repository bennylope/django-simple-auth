# encoding: utf-8

from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.test import TestCase
from simple_auth.models import Password


def test_password_url():
    assert reverse('simple_auth_password')


class PasswordInputTests(TestCase):

    def setUp(self):
        Password.objects.create(password="test")

    def test_correct_password(self):
        """Redirects to next URL with correct password"""
        post_response = self.client.post(reverse("simple_auth_password"),
                data={'password': 'test', 'url': '/tester/hello/'})
        self.assertRedirects(post_response, "/tester/hello/")

        # Session is now set
        get_response = self.client.get("/tester/hello/")
        assert get_response.status_code == 200

    def test_incorrect_password(self):
        """Display form errors with incorrect password, no redirect"""
        post_response = self.client.post(reverse("simple_auth_password"),
                data={'password': 'adjktest', 'url': '/tester/hello/'})
        assert post_response.status_code == 200
