import os


class Config(object):
    TEST = True


class ProductionConfig(Config):
    DATABASE_URI = os.getenv("DATABASE_URI")


class DevelopmentConfig(Config):
    DATABASE_URI = "sql:///memory"
    TESTING = True