from .base import *   #NOQA


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'typeidea_db',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        # 'CONN_MAX_AGE': 5 * 60,
        # 'OPTIONS': {'charset': 'utf8mb64'}
    },
}

INSTALLED_APPS += [
    # 'debug_toolbar',
    # 'pympler',
    # 'debug_toolbar_line_profiler',
    'silk',
]

MIDDLEWARE += [
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
    # 'debug_toolbar_line_profiler.panel.ProfilingPanel',
    'silk.middleware.SilkyMiddleware',
]

INTERNAL_IPS = ["127.0.0.1"]

# DEBUG_TOOLBAR_CONFIG = {
#     'JQUERY_URL': 'https://cdn.bootcss.com/jquery/3.3.1/jquery.min.js',
#
# }


DEBUG_TOOLBAR_PANELS = [
    # 'djdt_flamegraph.FlamegraphPanel',
    'pympler.panels.MemoryPanel',
]
