import os

app_dir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    DEBUG = False
    TESTING = False
    JSON_AS_ASCII = False
    SITE = ''  # '/bill18/'
    API = '/api/v1'
    FILE_LOG = 'bill18.log'

    SECRET_KEY = os.environ.get('SECRET_KEY', 'A SECRET KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # настройка Flask-Mail
    ADMINS = ['puzanovma@yandex.ru']
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = False
    MAIL_USE_SSL = (os.environ.get('MAIL_USE_SSL') or True)
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = MAIL_USERNAME
    MAIL_SUBJECT_PREFIX = ''

    DATABASE_URI = (os.environ.get('DATABASE_URI') or
                    'DRIVER={SQL Server};SERVER=localhost;DATABASE=kr1;UID=sa;PWD=123')


class DevelopementConfig(BaseConfig):
    DEBUG = True
    DATABASE_URI = (os.environ.get('DATABASE_URI') or
                    "DRIVER={SQL Server};SERVER=localhost;DATABASE=kr1;UID=sa;PWD=123")


class TestingConfig(BaseConfig):
    TESTING = True
    DATABASE_URI = (os.environ.get('DATABASE_URI') or
                    "DRIVER={SQL Server};SERVER=localhost;DATABASE=kr1;UID=sa;PWD=123")


class ProductionConfig(BaseConfig):
    DATABASE_URI = (os.environ.get('DATABASE_URI') or
                    'DRIVER={SQL Server};SERVER=localhost;DATABASE=komp;UID=sa;PWD=dnypr1')
