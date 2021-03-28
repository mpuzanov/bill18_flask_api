from . import mail
from flask import render_template
from threading import Thread
from bill18 import create_app
from flask_mail import Message


def async_send_mail(app, msg):
    with app.app_context():
        mail.send(msg)


def send_mail(subject, recipient, template, **kwargs):
    msg = Message(subject, sender=create_app.config['MAIL_DEFAULT_SENDER'], recipients=[recipient])
    msg.html = render_template(template, **kwargs)
    thrd = Thread(target=async_send_mail, args=[create_app, msg])
    thrd.start()
    return thrd
