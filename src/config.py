
import os



class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_TEST_URL')
    DEBUG = True
    TESTING = True


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    DEBUG = True
