# -*- coding: utf-8 -*-

LOGIN_URL          = '/socialauth_douban/'
LOGIN_REDIRECT_URL = '/quiz/'
LOGIN_ERROR_URL    = '/login-error/'

SOCIAL_AUTH_COMPLETE_URL_NAME  = 'socialauth_complete'
SOCIAL_AUTH_ASSOCIATE_URL_NAME = 'socialauth_associate_complete'

DOUBAN2_CONSUMER_KEY = "0d43a2695456712d27cae73bfd035387"
DOUBAN2_CONSUMER_SECRET = "79144fd570399fb2"

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.contrib.douban.DoubanBackend2',                       
    'django.contrib.auth.backends.ModelBackend',
)
