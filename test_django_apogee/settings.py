"""
Django settings for test_django_apogee project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '02+eu^m*yk=mty%n&+&zfth49t3e$7=#(mhd%-8*)y9y8%_rcl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'devserver',
    'django_apogee',
    'django_extensions',
    'south',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'test_django_apogee.urls'

WSGI_APPLICATION = 'test_django_apogee.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases


if DEBUG:
    APOGEE_CONNECTION = 'oracle'
else:
    APOGEE_CONNECTION = 'apoprod'


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
try:
    from local_settings import *
except ImportError:
    pass

import sys

if 'test' in sys.argv or 'test_coverage' in sys.argv:  # Covers regular testing and django-coverage

    SOUTH_DATABASE_ADAPTERS = {
        'default': 'south.db.sqlite3',
        'oracle': 'south.db.sqlite3',
    }
    SOUTH_TESTS_MIGRATE = False
    SKIP_SOUTH_TESTS = True
    DATABASES = {
        'default': {
             'ENGINE': 'django.db.backends.sqlite3',
             # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
             'NAME': 'refprod', # Or path to database file if using sqlite3.
             'TEST_NAME': ':memory:'
        },
        'oracle': {
             'ENGINE': 'django.db.backends.sqlite3',
             # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
             'NAME': 'oracle', # Or path to database file if using sqlite3.
             'TEST_NAME': ':memory:'
        },
    }

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
