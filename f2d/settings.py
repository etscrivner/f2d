"""
Django settings for f2d project.

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
SECRET_KEY = 'pu5%og8i2v4bjoi1v6q_#qqmahf(3)ii+fdo&m&3koiowar8ht'

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
    'django_nose',
    'f2d',
    'follow',
    'tracks',
    'users'
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

ROOT_URLCONF = 'f2d.urls'

WSGI_APPLICATION = 'f2d.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

# Unit-testing
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# Logging
# https://docs.djangoproject.com/en/1.7/topics/logging/
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        }
    },
    'loggers': {
        'users': {
            'handlers': ['console'],
            'level': 'INFO',
        }
    }
}


# Application environment (dev, prod)
class AppEnvironments(object):
    """Enumeration of application environments"""
    Development = 'dev'
    Production = 'prod'

    DevelopmentEnvironments = [Development]
    ProductionEnvironments = [Production]

    @classmethod
    def is_production(cls, value):
        """Indicates whether or not the given environment is a production
        environment.

        :param value: A string value
        :type value: str
        :rtype: bool
        """
        return value in cls.ProductionEnvironments


APP_ENVIRONMENT = AppEnvironments.Production

# Soundcloud API
# https://github.com/soundcloud/soundcloud-python
SOUNDCLOUD_CLIENT_ID = 'dbfb931676a5e9a01e7b20e5221feef8'
SOUNDCLOUD_CLIENT_SECRET = 'b4322147bbae3e543e5dfb60fbb2a271'
SOUNDCLOUD_REDIRECT_URI = 'http://localhost:8000/users/oauth/callback'

SOUNDCLOUD_FOLLOW_CLIENT_ID = '85ba9d3f1618af2b1fc958c07295a3cd'
SOUNDCLOUD_FOLLOW_CLIENT_SECRET = '97957a3b44badfe1bb9da7cdcdc2c6c0'
SOUNDCLOUD_FOLLOW_REDIRECT_URI = 'http://localhost:8000/d/oauth/callback'

if AppEnvironments.is_production(APP_ENVIRONMENT):
    SOUNDCLOUD_CLIENT_ID = '959cbd7bd3fa1f5b92bd32374a6f30eb'
    SOUNDCLOUD_CLIENT_SECRET = 'bd0a1e89388e9a03320122c17d8f042e'
    SOUNDCLOUD_REDIRECT_URI = 'http://follow2download.com/users/oauth/callback'

    SOUNDCLOUD_FOLLOW_CLIENT_ID = '25f0394a28d37a47807e630a7e826abe'
    SOUNDCLOUD_FOLLOW_CLIENT_SECRET = 'f99aff58c8ec354b781a5b9b9c9b8e27'
    SOUNDCLOUD_FOLLOW_REDIRECT_URI = 'http://follow2download.com/d/oauth/callback'


# follow2download SoundCloud User ID
FOLLOW2DOWNLOAD_SOUNDCLOUD_USER_ID = '138114501'

# File Upload Constants
MAX_TRACK_FILE_SIZE_MB = 15

# File upload configuration
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
