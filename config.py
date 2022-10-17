import os


class Config(object):
    TEST = False
    DEBUG = False


class ProductionConfig(Config):
    DATABASE_URI = os.getenv("DATABASE_URI")
    SQLALCHEMY_DATABASE_URI = DATABASE_URI


class DevelopmentConfig(Config):
    DATABASE_URI = "sqlite:///memory"
    TESTING = True
    DEBUG = True
