import os

import pytest
from rest_framework.test import APIClient

pytest_plugins = ["tests.fixtures"]


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture(scope='session', autouse=True)
def set_django_settings_module():
    os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'
