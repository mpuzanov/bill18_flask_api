import logging
from flask import current_app


def get_mail_handler():
    from logging.handlers import SMTPHandler
    mail_handler = SMTPHandler(current_app.config['MAIL_SERVER'],
                               current_app.config['MAIL_DEFAULT_SENDER'],
                               current_app.config['ADMINS'], 'Bill18 Application Failed')
    mail_handler.setLevel(logging.ERROR)

    mail_handler.setFormatter(logging.Formatter('''
    Message type:       %(levelname)s
    Location:           %(pathname)s:%(lineno)d
    Module:             %(module)s
    Function:           %(funcName)s
    Time:               %(asctime)s

    Message:

    %(message)s
    '''))

    return mail_handler


def get_rotating_file_handler():
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler(current_app.config['FILE_LOG'], maxBytes=10000, backupCount=1)
    file_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s '
                                  '[in %(pathname)s:%(lineno)d]')

    file_handler.setFormatter(formatter)
    return file_handler


def get_file_handler():
    from logging import FileHandler
    file_handler = FileHandler(current_app.config['FILE_LOG'])
    file_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s '
                                  '[in %(pathname)s:%(lineno)d]')

    file_handler.setFormatter(formatter)
    return file_handler
