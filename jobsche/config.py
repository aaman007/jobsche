import os


ENV = os.environ.get('ENV', 'development')
SECRET_KEY = os.environ.get('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')

if not SECRET_KEY:
    raise ValueError('No SECRET_KEY set for Flask application')
if not SQLALCHEMY_DATABASE_URI:
    raise ValueError('No SQLALCHEMY_DATABASE_URI set for Flask application')


class Environment:
    DEVELOPMENT = 'development'
    PRODUCTION = 'production'
    TESTING = 'testing'


class Config:
    SECRET_KEY = SECRET_KEY
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask Smorest Configs
    API_TITLE = 'JobSche API'
    API_VERSION = 'v1'
    OPENAPI_VERSION = '3.0.2'

    @property
    def DEBUG(self):
        return ENV != Environment.PRODUCTION

    @property
    def TESTING(self):
        return ENV != Environment.PRODUCTION
