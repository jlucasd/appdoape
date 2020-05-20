import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'app-do-ape-senai-donalane'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database/appdoape.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False