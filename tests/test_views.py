# encoding: utf-8

from __future__ import unicode_literals
from django.core.urlresolvers import reverse


def test_password_url():
    assert reverse('simple_auth_password')


def test_correct_password():
    """Redirects to next URL with correct password"""


def test_incorrect_password():
    """Display form errors with incorrect password"""
