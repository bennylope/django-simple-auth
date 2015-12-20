# encoding: utf-8

from __future__ import unicode_literals
from simple_auth.forms import PasswordAdminForm, PasswordForm


def test_admin_name_not_required():
    form = PasswordAdminForm(data={
        'password': 'jakdjkj',
    })
    assert form.is_valid()


def test_admin_password_required():
    form = PasswordAdminForm(data={
        'name': 'jakdjkj',
    })
    assert not form.is_valid()


def test_pass_missing_next():
    form = PasswordForm(data={
        'password': 'jakdjkj',
    })
    assert form.is_valid()


def test_password_required():
    form = PasswordForm(data={
        'url': 'jakdjkj',
    })
    assert not form.is_valid()
