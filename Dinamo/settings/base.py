import os
from django.urls import reverse_lazy


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    'django.contrib.sites',
    'crispy_forms',
    'agregator',
    'django_apscheduler',
    'user',
    'forum',
    'contact',
]
CRISPY_TEMPLATE_PACK = 'bootstrap4'
SITE_ID=1
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.BrokenLinkEmailsMiddleware',

]
ROOT_URLCONF = 'Dinamo.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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
WSGI_APPLICATION = 'Dinamo.wsgi.application'
AUTH_USER_MODEL = 'user.User'


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGIN_URL=reverse_lazy('dj-auth:login')
LOGOUT_URL=reverse_lazy('dj-auth:logout')
LOGIN_REDIRECT_URL=reverse_lazy('article_list')


SERVER_EMAIL='contact@dinamonews.ro'
DEFAULT_FROM_EMAIL='no-reply@dinamonews.ro'
EMAIL_SUBJECT_PREFIX='[Dinamo News]'
MANAGERS=[
    ('Us','ourselves@dinamonews.ro'),
]
STATIC_URL = 'static/'
STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'static')
]
STATIC_ROOT='staticfiles'
MEDIA_URL='media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')

