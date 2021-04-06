from datetime import datetime
from flask import session, current_app
from bill18.mail import send_mail, send_email
from . import main


@main.route('/')
@main.route('/index')
def index():
    current_app.logger.debug('/index')
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1  # обновление данных сессии
    else:
        session['visits'] = 1  # запись данных в сессию
    return f"<h1>API - сервис по приборам учёта</h1>Число просмотров: {session['visits']}"


@main.route('/status')
def status():
    return {
        'status': True,
        'time': datetime.now().strftime('%d.%m.%Y %H:%M:%S'),
    }


@main.route('/contact', methods=['get'])
# @main.route('/contact', methods=['post'])
def contact():
    current_app.logger.debug('/contact')
    recipients = ['puzanovma@yandex.ru']
    # send_email("welcome", recipients=recipients, text_body='Welcome')
    send_mail("welcome", recipients=recipients, text_body='Welcome from API bill18')
    # send_email('[bill18] welcome',
    #            sender=current_app.config['ADMINS'][0],
    #            recipients=[email],
    #            text_body=render_template('email/welcome.txt',
    #                                      username=username),
    #            html_body=render_template('email/welcome.html',
    #                                      username=username))

    # send_mail('[bill18] welcome',
    #           recipient=[email],
    #           template='email/welcome.html',
    #           username=username)

    return {
        'send_mail': True,
        'time': datetime.now().strftime('%d.%m.%Y %H:%M:%S'),
    }
