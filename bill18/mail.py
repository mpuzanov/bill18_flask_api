from . import email
from flask import render_template, current_app
from threading import Thread
from flask_mail import Message


def send_async_email(app, msg):
    with app.app_context():
        email.send(msg)


def send_email(subject, recipients, text_body='', html_body=''):
    app = current_app
    print(app.config['MAIL_USERNAME'])
    msg = Message(subject, sender=app.config['MAIL_USERNAME'], recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email, args=[app, msg])


def send_mail(subject, recipients, text_body=''):
    app = current_app
    with app.app_context():
        msg = Message(subject, sender=app.config['MAIL_USERNAME'], recipients=recipients)
        msg.body = text_body
        thrd = Thread(target=email.send(msg), args=[msg])
        return thrd.start()


def send_email_template(to, subject, template, **kwargs):
    app = current_app
    with app.app_context():
        msg = Message(app.config['MAIL_SUBJECT_PREFIX'] + subject, sender=app.config['MAIL_SENDER'], recipients=[to])
        msg.body = render_template(template + '.txt', **kwargs)
        msg.html = render_template(template + '.html', **kwargs)
        Thread(target=email.send(msg)).start()
