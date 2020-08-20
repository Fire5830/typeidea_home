from .base import *

DEBUG = False

ALLOWED_HOSTS =['thefire5.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'typeidea_db',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        # 'CONN_MAX_AGE': 5 * 60,
        'OPTIONS': {'charset': 'utf8mb64'}
    },
}