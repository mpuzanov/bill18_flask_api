from datetime import datetime
from app import app
from flask import g
from FDataBase import FDataBase
import pyodbc
import utils

SITE = app.config['SITE']
app.json_encoder = utils.MyJSONEncoder


def connect_db():
    """Создаем соединение к БД"""
    conn = None
    try:
        conn = pyodbc.connect(app.config['DATABASE_URI'], timeout=5)
    except Exception as ex:
        print("\nError connection: ", ex)
        print(f"DATABASE_URI: {app.config['DATABASE_URI']}")
    return conn


def get_db():
    """Соединение с БД, если оно еще не установлено"""
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.route(SITE + '/')
def home():
    return "<h1>API - сервис по приборам учёта</h1>"


@app.teardown_appcontext
def close_db(error):
    """Закрываем соединение с БД, если оно было установлено"""
    if hasattr(g, 'link_db'):
        g.link_db.close()


@app.route(SITE + '/status')
def status():
    dt_now = datetime.now()
    return {
        'status': True,
        'time': dt_now.strftime('%d.%m.%Y %H:%M:%S'),
    }


@app.route(SITE + '/streets')
def get_streets():
    """Возвращаем список улиц"""
    db = get_db()
    dbase = FDataBase(db)
    return dbase.get_streets()


@app.route(SITE + '/builds/<street_name>')
def get_builds(street_name):
    """Возвращаем список домов по заданной улице"""
    db = get_db()
    dbase = FDataBase(db)
    return dbase.get_builds(street_name)


@app.route(SITE + '/flats/<street_name>/<nom_dom>')
def get_flats(street_name, nom_dom):
    """Возвращаем список помещений по заданному дому"""
    db = get_db()
    dbase = FDataBase(db)
    return dbase.get_flats(street_name, nom_dom)


@app.route(SITE + '/lics/<street_name>/<nom_dom>/<nom_kvr>')
def get_lics(street_name, nom_dom, nom_kvr):
    """Возвращаем список лицевых в помещении"""
    db = get_db()
    dbase = FDataBase(db)
    return dbase.get_lics(street_name, nom_dom, nom_kvr)


@app.route(SITE + '/lic/<int:lic>')
def get_occ(lic):
    """Возвращаем информацию по заданному лицевому счету"""
    db = get_db()
    dbase = FDataBase(db)
    return dbase.get_occ(lic)


@app.route(SITE + '/infoDataCounter/<int:lic>')
def get_pu(lic):
    """Возвращаем список приборов учета по заданному лицевому счету"""
    db = get_db()
    dbase = FDataBase(db)
    return dbase.get_counters(lic)


@app.route(SITE + '/infoDataCounterValue/<int:lic>')
def get_ppu(lic):
    """Возвращаем список показаний приборов учета по заданному лицевому счету"""
    db = get_db()
    dbase = FDataBase(db)
    return dbase.get_counter_values(lic)


@app.route(SITE + '/infoDataValue/<int:lic>')
def get_values(lic):
    """Возвращаем список начислений по заданному лицевому счету"""
    db = get_db()
    dbase = FDataBase(db)
    return dbase.get_values(lic)


@app.route(SITE + '/infoDataPaym/<int:lic>')
def get_payments(lic):
    """Возвращаем список платежей по заданному лицевому счету"""
    db = get_db()
    dbase = FDataBase(db)
    return dbase.get_payments(lic)


@app.route(SITE + '/puAddValue/<int:pu_id>/<float:value>')
def pu_add_value(pu_id, value):
    """Добавление ППУ"""
    db = get_db()
    dbase = FDataBase(db)
    return dbase.pu_add_value(pu_id, value)


@app.route(SITE + '/puDelValue/<int:pu_id>/<int:id_value>')
def pu_del_value(pu_id, id_value):
    """Удаление ППУ"""
    db = get_db()
    dbase = FDataBase(db)
    return dbase.pu_del_value(pu_id, id_value)
