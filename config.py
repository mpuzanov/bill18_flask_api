import os

app_dir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    JSON_AS_ASCII = False
    SITE = ''  # '/bill18/api/v1'
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
    SECRET_KEY = "SUPER SECRET KEY"
    DATABASE_URI = (os.environ.get('DATABASE_URI') or
                    "DRIVER={SQL Server};SERVER=localhost;DATABASE=kr1;UID=sa;PWD=123")


class TestingConfig(BaseConfig):
    DEBUG = True
    DATABASE_URI = (os.environ.get('DATABASE_URI') or
                    'DRIVER={SQL Server};SERVER=localhost;DATABASE=kr1;UID=sa;PWD=123')


class ProductionConfig(BaseConfig):
    DEBUG = False
    DATABASE_URI = (os.environ.get('DATABASE_URI') or
                    'DRIVER={SQL Server};SERVER=localhost;DATABASE=komp;UID=sa;PWD=dnypr1')
