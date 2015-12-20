#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Management command entry point for working with migrations
"""

import sys
import django
from django.conf import settings

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.admin",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "simple_auth",
]

settings.configure(
    DEBUG=True,
    USE_TZ=True,
    USE_I18N=True,
    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
        }
    },
    MIDDLEWARE_CLASSES=(),  # Silence Django warnings
    SITE_ID=1,
    INSTALLED_APPS=INSTALLED_APPS,
    ROOT_URLCONF="tests.urls",
)

django.setup()

if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
