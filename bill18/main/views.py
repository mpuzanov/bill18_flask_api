from datetime import datetime
from flask import session
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