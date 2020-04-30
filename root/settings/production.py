from root.settings.common import *
import environ

env = environ.Env(
  DEBUG = (bool, False)
)

# redirects all requests to https
# SECURE_SSL_REDIRECT = True
# session cookies will only be set, if https is used
# SESSION_COOKIE_SECURE = True
# how long is a session cookie valid?
# SESSION_COOKIE_AGE = 1209600

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': env('DB_NAME'),
    'USER': env('DB_USER'),
    'PASSWORD': env('DB_PASSWORD'),
    'HOST': env.db(),
    'PORT': env('DB_PORT'),
    'OPTIONS' : {
      'options': '-c search_path=%s,public' % env('DB_SCHEMA_NAME')
    },
  }
}

# APPLICATION CONFIGURATION
INSTALLED_APPS = DEFAULT_APPS
