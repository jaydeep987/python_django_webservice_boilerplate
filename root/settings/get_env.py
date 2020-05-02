import environ

env = environ.Env(
  APP_ENV = (str, 'development')
)

environment = env('APP_ENV')

if environment == 'prod':
  environment = 'production'
elif environment == 'stg':
  environment = 'staging'
else:
  environment = 'development'

def isProduction():
  return environment == 'production'

def isDevelopment():
  return environment == 'development'

def isStaging():
  return environment == 'staging'

def isDevelopmentOrStaging():
  return isDevelopment() or isStaging()
