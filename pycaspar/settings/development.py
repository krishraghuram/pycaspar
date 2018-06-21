from .base import *

SECRET_KEY = 'Ct3PdFdWLOUZCE2f5o4/V19ucFkOugQ1gtRJTVz5sBM='

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pycaspar',
        'USER': 'cbs',
        'PASSWORD': 'iitg',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}

STATIC_URL = '/static/'