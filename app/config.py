import os

app_dir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    # SITE = '/bill18/api/v1'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'A SECRET KEY'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # настройка Flask-Mail
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'YOU_MAIL@gmail.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'password'
    MAIL_DEFAULT_SENDER = MAIL_USERNAME


class DevelopementConfig(BaseConfig):
    DEBUG = True
    DATABASE_URI = os.environ.get('DEVELOPMENT_DATABASE_URI') or 'sqlserver://sa:123@localhost:1433?database=kr1'


class TestingConfig(BaseConfig):
    DEBUG = True
    DATABASE_URI = os.environ.get('TESTING_DATABASE_URI') or 'sqlserver://sa:123@localhost:1433?database=kr1'


class ProductionConfig(BaseConfig):
    DEBUG = False
    DATABASE_URI = os.environ.get('PRODUCTION_DATABASE_URI') or 'sqlserver://sa:dnypr1@192.168.5.111:1433?database=komp'
