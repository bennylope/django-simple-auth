# encoding: utf-8

from __future__ import unicode_literals

import pytest
from simple_auth.forms import PasswordAdminForm, PasswordForm
from simple_auth.models import Password


def test_admin_name_not_required():
    form = PasswordAdminForm(data={
        "password": "jakdjkj",
    })
    assert form.is_valid()


def test_admin_password_required():
    form = PasswordAdminForm(data={
        "name": "jakdjkj",
    })
    assert not form.is_valid()


def test_password_required():
    form = PasswordForm(data={
        "url": "jakdjkj",
    })
    assert not form.is_valid()


@pytest.mark.django_db
def test_pass_missing_next():
    Password.objects.create(password="test")
    form = PasswordForm(data={
        "password": "test",
    })
    assert form.is_valid()


@pytest.mark.django_db
def test_wrong_password():
    Password.objects.create(password="test")
    form = PasswordForm(data={
        "password": "test",
    })
    assert form.is_valid()


@pytest.mark.django_db
def test_multiple_matches():
    Password.objects.create(password="test")
    Password.objects.create(password="test")
    form = PasswordForm(data={
        "password": "test",
    })
    assert form.is_valid()
