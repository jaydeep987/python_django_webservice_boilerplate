from os.path import join

from root.settings.common import *

DEBUG = True

ADMIN_ENABLED = True

ALLOWED_HOSTS = ['*']

# DATABASES = {
#   'default': {
#     'ENGINE': 'django.db.backends.postgresql',
#     'NAME': 'pythondjango',
#     'USER': 'postgres',
#     'PASSWORD': 'PostgreSQL',
#     'HOST': '192.168.11.13',
#     'PORT': '5432',
#     'OPTIONS' : {
#       'options': '-c search_path=pythondjango,public'
#     },
#   }
# }

DATABASES = {
  'default': {
    'ENGINE': 'sql_server.pyodbc',
    'NAME': 'pythondjango',
    'USER': 'sa',
    'PASSWORD': 'MsSQL@987',
    'HOST': '127.0.0.1',
    'PORT': '1433',
    'OPTIONS': {
      'driver': 'ODBC Driver 17 for SQL Server',
    },
  }
}

# APPLICATION CONFIGURATION
INSTALLED_APPS = DEFAULT_APPS
