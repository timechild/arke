import os


class Config(object):
    DEBUG = True
    SECRET_KEY = 'my key'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SERVER_IP = os.environ['SERVER_NAME']
    PORT = int(os.environ['PORT'])


class TestConfig(Config):
    DEBUG = True
    # to-do: set up test database


class LocalConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
