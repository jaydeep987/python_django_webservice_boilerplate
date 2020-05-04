from os.path import abspath, basename, dirname, join
from django.utils.translation import gettext_lazy as _
from root.settings.get_env import isDevelopmentOrStaging

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = dirname(dirname(abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'injc!k1b8znh8$t6&&#ggyzw5bg#rqo+dh9x)52$7cu$-naa-r'

SECURE_BROWSER_XSS_FILTER = True

# Project root
PROJECT_ROOT = dirname(BASE_DIR)

# Static files
STATIC_ROOT = join(PROJECT_ROOT, 'static')

# Collect media files
MEDIA_ROOT = join(PROJECT_ROOT, 'media')

# The URL for static files
STATIC_URL = '/static/'

# These are the apps
DEFAULT_APPS = [
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'rest_framework',
  'polls.apps.PollsConfig'
]

rest_rendere_classes = [
  'rest_framework.renderers.JSONRenderer'
]

if isDevelopmentOrStaging():
  rest_rendere_classes.append('rest_framework.renderers.BrowsableAPIRenderer')

# Rest framework settings
REST_FRAMEWORK = {
  'DEFAULT_RENDERER_CLASSES': rest_rendere_classes,
  'DEFAULT_PARSER_CLASSES': [
    'rest_framework.parsers.FormParser',
    'rest_framework.parsers.JSONParser',
    'rest_framework.parsers.MultiPartParser'
  ],
  'DEFAULT_AUTHENTICATION_CLASSES': [
    'rest_framework.authentication.TokenAuthentication'
  ]
}

# Middlewares
MIDDLEWARE = [
  'django.middleware.security.SecurityMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Templates
TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [ join(PROJECT_ROOT, 'templates') ],
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

# Only allow access to specified hosts
ALLOWED_HOSTS = []

ROOT_URLCONF = 'root.urls'

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

LANGUAGES = (
  ('hi', _('Hindi')),
  ('gu', _('Gujarati')),
  ('en', _('English')),
)

TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LOCALE_PATHS = [
  join(abspath(BASE_DIR), 'locale')
]

# these persons receive error notification
ADMINS = (
    ('Jaydeep', 'jaydeep253a@gmail.com'),
)
MANAGERS = ADMINS
