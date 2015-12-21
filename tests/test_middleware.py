# encoding: utf-8

from __future__ import unicode_literals

import unittest

try:
    from unittest import mock
except ImportError:
    import mock

from django.contrib.auth.models import User
from django.test import TestCase
from django.test.utils import override_settings

from simple_auth.middleware import allow_user


class GatekeeperTests(unittest.TestCase):

    def setUp(self):
        self.user = mock.MagicMock()
        self.request = mock.MagicMock()
        self.request.session = {}
        self.request.user = self.user

    def test_authenticated_user(self):
        """Normally authenticated users should be allowed"""
        self.request.user.is_authenticated.return_value = True
        assert allow_user(self.request)

    def test_has_session(self):
        """If the user has already entered a good password, allow"""
        self.request.user.is_authenticated.return_value = False
        self.request.session['simple_auth'] = 'kjdk'
        assert allow_user(self.request)

    def test_no_session(self):
        """If user has no session key, redirect"""
        self.request.user.is_authenticated.return_value = False
        self.request.session['simple_auth'] = None
        assert not allow_user(self.request)


class URLTests(TestCase):

    def test_protect_test_url(self):
        self.client.logout()
        response = self.client.get("/tester/hello/")
        self.assertRedirects(response, "/password/?url=%2Ftester%2Fhello%2F")

    def test_default_admin_ignored(self):
        """Admin URLs ignored by default"""
        response = self.client.get("/admin/")
        self.assertRedirects(response, "/admin/login/?next=/admin/")

    @override_settings(SIMPLE_AUTH_IGNORE=[])
    def test_no_ignored(self):
        """Even admin URLs are protected"""
        response = self.client.get("/admin/")
        self.assertRedirects(response, "/password/?url=%2Fadmin%2F")

    @override_settings(SIMPLE_AUTH_IGNORE=[r'^test'])
    def test_test_ignored(self):
        """Ignore specified URLs"""
        response = self.client.get("/tester/hello/")
        self.assertEqual(response.status_code, 200)

    @override_settings(SIMPLE_AUTH_IGNORE=[r'^test'],
                       SIMPLE_AUTH_PROTECT=[r'^test'])
    def test_ignore_protec_conflict(self):
        """Ignore always trumps protect"""
        response = self.client.get("/tester/hello/")
        self.assertEqual(response.status_code, 200)

    @override_settings(SIMPLE_AUTH_PROTECT=[r'^test'])
    def test_only_specified_protected(self):
        response = self.client.get("/tester/hello/")
        self.assertEqual(response.status_code, 302)
        response = self.client.get("/goodbye/world/")
        self.assertEqual(response.status_code, 200)

    def test_allowed_authed_user(self):
        user = User.objects.create(username="bob")
        self.client.force_login(user)
        response = self.client.get("/tester/hello/")
        self.assertEqual(response.status_code, 200)
        self.client.logout()
