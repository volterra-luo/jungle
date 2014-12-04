# -*- coding: utf-8 -*-

SOCIAL_AUTH_LOGIN_URL          = '/socialauth_douban/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/quiz/'
SOCIAL_AUTH_LOGIN_ERROR_URL    = '/login-error/'

SOCIAL_AUTH_COMPLETE_URL_NAME  = 'socialauth_complete'
SOCIAL_AUTH_ASSOCIATE_URL_NAME = 'socialauth_associate_complete'



SOCIAL_AUTH_DOUBAN_OAUTH2_KEY = "0d43a2695456712d27cae73bfd035387"
SOCIAL_AUTH_DOUBAN_OAUTH2_SECRET = "79144fd570399fb2"

AUTHENTICATION_BACKENDS = (
    'social.backends.douban.DoubanOAuth2',               
    'django.contrib.auth.backends.ModelBackend',
)
