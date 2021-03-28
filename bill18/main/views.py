from datetime import datetime
from flask import session, flash, current_app
from bill18.utils import send_mail
from . import main


@main.route('/')
@main.route('/index')
def index():
    print("index")
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1  # обновление данных сессии
    else:
        session['visits'] = 1  # запись данных в сессию
    return f"<h1>API - сервис по приборам учёта</h1>Число просмотров: {session['visits']}"


@main.route('/status')
def status():
    print("status")
    dt_now = datetime.now()
    return {
        'status': True,
        'time': dt_now.strftime('%d.%m.%Y %H:%M:%S'),
    }


@main.route('/contact/', methods=['get', 'post'])
def contact():
    name = ''
    email = ''
    send_mail("New Feedback", current_app.config['MAIL_DEFAULT_SENDER'], 'mail/feedback.html',
              name=name, email=email)
    flash("Message Received", "success")
    return True
