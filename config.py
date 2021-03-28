import os

app_dir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    DEBUG = False
    TESTING = False
    JSON_AS_ASCII = False
    SITE = ''  # '/bill18/'

    SECRET_KEY = os.environ.get('SECRET_KEY', 'A SECRET KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # настройка Flask-Mail
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME', 'YOU_MAIL@gmail.com')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', 'password')
    MAIL_DEFAULT_SENDER = MAIL_USERNAME

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
