import time
from datetime import datetime
from app import app
from app.db import config as db
from app.db import query
import utils
SITE = '/bill18/api/v1'


@app.route(SITE + '/')
def home():
    return "<h1>API - сервис по приборам учёта</h1>"


@app.route(SITE + '/status')
def status():
    dt_now = datetime.now()
    return {
        'status': True,
        'time1': time.asctime(),
        'time2': dt_now.strftime('%d.%m.%Y time: %H:%M:%S'),
        'time3': dt_now.isoformat()
    }


@app.route(SITE + '/streets')
def get_streets():
    conn = db.get_connection()
    data = query.get_streets(conn)
    conn.close()
    return data


@app.route(SITE + '/builds/<street_name>')
def get_builds(street_name):
    conn = db.get_connection()
    data = query.get_builds(conn, street_name)
    conn.close()
    return data


@app.route(SITE + '/flats/<street_name>/<nom_dom>')
def get_flats(street_name, nom_dom):
    conn = db.get_connection()
    data = query.get_flats(conn, street_name, nom_dom)
    conn.close()
    return data


@app.route(SITE + '/lics/<street_name>/<nom_dom>/<nom_kvr>')
def get_lics(street_name, nom_dom, nom_kvr):
    conn = db.get_connection()
    data = query.get_lics(conn, street_name, nom_dom, nom_kvr)
    conn.close()
    return data


@app.route(SITE + '/lic/<int:lic>')
def get_occ(lic):
    conn = db.get_connection()
    data = query.get_occ(conn, lic)
    conn.close()
    return data

# TODO сделать добавление ППУ
# TODO сделать удаление ППУ
