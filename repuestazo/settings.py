# coding=utf-8
"""
Django settings for repuestazo project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b)b_xfu4+@u5no3b-i&p10g!@n$x590k^jqx-)&4g=kj7c0de7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['www.repuestazo.com', 'repuestazo.com']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'grimoire.django.xmail',
    'tinymce',
    'rest_framework',
    'customers',
    'pages',
    'advertisement',
    'stock',
    'blog'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

REST_FRAMEWORK = {
    'UNICODE_JSON': False,
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}

ROOT_URLCONF = 'repuestazo.urls'

WSGI_APPLICATION = 'repuestazo.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'repuestazo',
        'USER': 'repuestazo',
        'PASSWORD': 'mysql:repuestazo$2014',
        'HOST': 'localhost',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es-ec'
TIME_ZONE = 'America/Guayaquil'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'repuestazo', 'locale')
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = 'http://static.repuestazo.com/repuestazo/'
STATIC_ROOT = '/home/rleiva/webapps/static/repuestazo/'
MEDIA_URL = 'http://media.repuestazo.com/repuestazo/'
MEDIA_ROOT = '/home/rleiva/webapps/media/repuestazo/'

# email

EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'atencion'
EMAIL_HOST_PASSWORD = 'mail:repuestazo$2014'
EMAIL_USE_TLS = False
EMAIL_USE_SSL = False
EMAIL_BACKEND = 'grimoire.django.xmail.backends.AsyncEmailBackend'
XMAIL_BRIDGED_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

DEFAULT_FROM_NAME = u'Atención al Cliente <atencion@repuestazo.com>'
DEFAULT_RECIPIENTS = {
    'contact': ['sguevara@autosierra.com.ec', 'quimelia@quimelia.com']
}

try:
    from local_settings import *
except ImportError:
    pass