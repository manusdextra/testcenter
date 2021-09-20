import os


class Config(object):
    TESTING = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'placeholder'
