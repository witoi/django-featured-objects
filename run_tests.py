#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import Command


def run_tests():
    from django.conf import settings
    from django.core.management import call_command
    settings.configure(
        INSTALLED_APPS=(
            'django.contrib.contenttypes',
            'django.contrib.auth',
            'featured',
        ),
        DATABASE_ENGINE='sqlite3',
        DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3'}},
        ROOT_URLCONF = 'tests_urls',
    )

    # Fire off the tests
    call_command('test', 'featured')


class TestCommand(Command):
    description = 'Run (Django) tests for django-featured-objects app.'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        run_tests()


if __name__ == '__main__':
    run_tests()
