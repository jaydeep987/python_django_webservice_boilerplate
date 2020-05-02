from os.path import join

from root.settings.common import *

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'pythondjango',
    'USER': 'postgres',
    'PASSWORD': 'PostgreSQL',
    'HOST': '192.168.11.13',
    'PORT': '5432',
    'OPTIONS' : {
      'options': '-c search_path=pythondjango,public'
    },
  }
}

# APPLICATION CONFIGURATION
INSTALLED_APPS = DEFAULT_APPS
