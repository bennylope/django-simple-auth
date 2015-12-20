# encoding: utf-8

from __future__ import unicode_literals
from django.test import TestCase
from simple_auth.models import Password


class ModelTests(TestCase):

    def test_save_object(self):
        Password.objects.create(
            name="My test",
            password="ajdkjkjakdj",
        )
