import os
from datetime import timedelta

import dj_database_url
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://d5a4c307198e4c38a82dbd7593234c5d@o153106.ingest.sentry.io/5240628",
    integrations=[DjangoIntegration()], send_default_pii=True
)

IS_PRODUCTION = 'PRODUCTION' in os.environ
IS_TEST = 'TRAVIS' in os.environ

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = os.getenv('SECRET_KEY') if IS_PRODUCTION else 'ulbhag)%ote-g#kc^e5nmc*o=6#hwqxk!@anb+90dghoai6#ou'
DEBUG = not IS_PRODUCTION
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split() if IS_PRODUCTION else []
INSTALLED_APPS = [
    'nutrition.apps.NutritionConfig',
    'goals.apps.GoalsConfig',
    'sec.apps.SecConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'django_filters'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'lifeknifexpy.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
WSGI_APPLICATION = 'lifeknifexpy.wsgi.application'
if IS_PRODUCTION:
    DATABASES = {
        'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
    }
elif IS_TEST:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'travis_ci_test',
            'USER': 'postgres',
            'PASSWORD': '',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'lifeknifexpy',
            'USER': 'lifeknifexpy',
            'PASSWORD': 'lifeknifexpy',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.SearchFilter',
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated',),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'PAGE_SIZE': 100
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=15),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
}

CSRF_USE_SESSIONS = False
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
SESSION_COOKIE_SAMESITE = None
CORS_ALLOW_CREDENTIALS = True
CSRF_COOKIE_SAMESITE = None

if IS_PRODUCTION:
    CORS_ORIGIN_WHITELIST = (os.getenv('CORS_ORIGIN_WHITELIST'),)
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_DOMAIN = CSRF_COOKIE_DOMAIN = os.getenv('SESSION_COOKIE_DOMAIN')
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 31536000  # one year
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SESSION_COOKIE_SAMESITE = os.getenv('SESSION_COOKIE_SAMESITE')
    CSRF_COOKIE_SAMESITE = os.getenv('CSRF_COOKIE_SAMESITE')
    CSRF_TRUSTED_ORIGINS = (os.getenv('CSRF_TRUSTED_ORIGINS') or '').split()
    # EMAIL_HOST = os.getenv('EMAIL_HOST')
    # EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
    # EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
    # ADMINS = [(os.getenv('ADMIN_NAME'), os.getenv('ADMIN_EMAIL'))]
    # SERVER_EMAIL = os.getenv('SERVER_EMAIL')

else:
    CORS_ORIGIN_WHITELIST = ('http://localhost:3000',)
    # SESSION_COOKIE_DOMAIN = CSRF_COOKIE_DOMAIN = 'http://localhost'

LOGIN_REDIRECT_URL = '/account/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
