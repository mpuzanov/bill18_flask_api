from . import api
from bill18.db import get_dbase
from flask import current_app


@api.route('/streets')
def get_streets():
    """Возвращаем список улиц"""
    current_app.logger.debug('Возвращаем список улиц')
    return get_dbase().get_streets()


@api.route('/builds/<street_name>')
def get_builds(street_name):
    """Возвращаем список домов по заданной улице"""
    return get_dbase().get_builds(street_name)


@api.route('/flats/<street_name>/<nom_dom>')
def get_flats(street_name, nom_dom):
    """Возвращаем список помещений по заданному дому"""
    current_app.logger.debug(f'Возвращаем список помещений по {street_name} {nom_dom}')
    return get_dbase().get_flats(street_name, nom_dom)


@api.route('/lics/<street_name>/<nom_dom>/<nom_kvr>')
def get_lics(street_name, nom_dom, nom_kvr):
    """Возвращаем список лицевых в помещении"""
    current_app.logger.debug(f'Возвращаем список лицевых по {street_name} {nom_dom}-{nom_kvr}')
    return get_dbase().get_lics(street_name, nom_dom, nom_kvr)


@api.route('/lic/<int:lic>')
def get_occ(lic):
    """Возвращаем информацию по заданному лицевому счету"""
    current_app.logger.debug(f'Возвращаем информацию по лицевому счету {lic}')
    return get_dbase().get_occ(lic)


@api.route('/infoDataCounter/<int:lic>')
def get_pu(lic):
    """Возвращаем список приборов учета по заданному лицевому счету"""
    current_app.logger.debug(f'Возвращаем список приборов учета по лицевому счету {lic}')
    return get_dbase().get_counters(lic)


@api.route('/infoDataCounterValue/<int:lic>')
def get_ppu(lic):
    """Возвращаем список показаний приборов учета по заданному лицевому счету"""
    current_app.logger.debug(f'Возвращаем список показаний приборов учета по лицевому счету {lic}')
    return get_dbase().get_counter_values(lic)


@api.route('/infoDataValue/<int:lic>')
def get_values(lic):
    """Возвращаем список начислений по заданному лицевому счету"""
    current_app.logger.debug(f'Возвращаем список начислений по лицевому счету {lic}')
    return get_dbase().get_values(lic)


@api.route('/infoDataPaym/<int:lic>')
def get_payments(lic):
    """Возвращаем список платежей по заданному лицевому счету"""
    current_app.logger.debug(f'Возвращаем список платежей по лицевому счету {lic}')
    return get_dbase().get_payments(lic)


@api.route('/puAddValue/<int:pu_id>/<int:value>')
@api.route('/puAddValue/<int:pu_id>/<float:value>')
def pu_add_value(pu_id, value):
    """Добавление ППУ"""
    current_app.logger.debug(f'Добавление показания (код ПУ: {pu_id} показание: {value})')
    return get_dbase().pu_add_value(pu_id, value)


@api.route('/puDelValue/<int:pu_id>/<int:id_value>')
def pu_del_value(pu_id, id_value):
    """Удаление ППУ"""
    current_app.logger.debug(f'Удаление показания (код ПУ: {pu_id} код ППУ: {id_value})')
    return get_dbase().pu_del_value(pu_id, id_value)
