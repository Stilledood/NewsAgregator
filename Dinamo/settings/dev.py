
from .base import *

SECRET_KEY = 'django-insecure-8sj&*+kce%^)1wt+d4-o%ug%aghembn-zd+hn+kzyh^v#)6sab'
DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR,'db.sqlite3')
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
CACHE_MIDDLEWARE_ALIAS = 'default'
EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'

