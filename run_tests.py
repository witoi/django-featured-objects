#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'tests_settings'

from django.conf import settings
from django.test.utils import get_runner


def run(verbosity=1, interactive=True, **kwargs):
    TestRunner = get_runner(settings)
    test_runner = TestRunner(verbosity=1, interactive=True, **kwargs)
    failures = test_runner.run_tests(['featured'])
    sys.exit(failures)

if __name__ == '__main__':
    run()
