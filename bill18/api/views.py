from . import api
from bill18.db import get_dbase
from flask import current_app, request, jsonify


@api.route('/streets')
def get_streets():
    """Возвращаем список улиц"""
    current_app.logger.debug('Возвращаем список улиц')
    try:
        data = get_dbase().get_streets()
    except Exception as ex:
        current_app.logger.warning(f'{ex}')
        return {"strerror:", str(ex)}, 400
    return jsonify(data)


@api.route('/builds/<street_name>')
def get_builds(street_name):
    """Возвращаем список домов по заданной улице"""
    current_app.logger.debug(f'Возвращаем список домов по {street_name}')
    try:
        data = get_dbase().get_builds(street_name)
    except Exception as ex:
        current_app.logger.warning(f'{ex}')
        return {"strerror:", str(ex)}, 400
    return jsonify(data)


@api.route('/flats/<street_name>/<nom_dom>')
def get_flats(street_name, nom_dom):
    """Возвращаем список помещений по заданному дому"""
    current_app.logger.debug(f'Возвращаем список помещений по {street_name} {nom_dom}')
    try:
        result = get_dbase().get_flats(street_name, nom_dom)
    except Exception as ex:
        current_app.logger.warning(f'{ex}')
        return {"strerror:", str(ex)}, 400
    return result


@api.route('/lics/<street_name>/<nom_dom>/<nom_kvr>')
def get_lics(street_name, nom_dom, nom_kvr):
    """Возвращаем список лицевых в помещении"""
    current_app.logger.debug(f'Возвращаем список лицевых по {street_name} {nom_dom}-{nom_kvr}')
    try:
        result = get_dbase().get_lics(street_name, nom_dom, nom_kvr)
    except Exception as ex:
        current_app.logger.warning(f'{ex}')
        return {"strerror:", str(ex)}, 400
    return result


@api.route('/lic/<int:lic>')
def get_occ(lic):
    """Возвращаем информацию по заданному лицевому счету"""
    current_app.logger.debug(f'Возвращаем информацию по лицевому счету {lic}')
    try:
        result = get_dbase().get_occ(lic)
    except Exception as ex:
        current_app.logger.warning(f'{ex}')
        return {"strerror:", str(ex)}, 400
    return result


@api.route('/infoDataCounter/<int:lic>')
def get_pu(lic):
    """Возвращаем список приборов учета по заданному лицевому счету"""
    current_app.logger.debug(f'Возвращаем список приборов учета по лицевому счету {lic}')
    try:
        result = get_dbase().get_counters(lic)
    except Exception as ex:
        current_app.logger.warning(f'{ex}')
        return {"strerror:", str(ex)}, 400
    return result


@api.route('/infoDataCounterValue/<int:lic>')
def get_ppu(lic):
    """Возвращаем список показаний приборов учета по заданному лицевому счету"""
    current_app.logger.debug(f'Возвращаем список показаний приборов учета по лицевому счету {lic}')
    try:
        result = get_dbase().get_counter_values(lic)
    except Exception as ex:
        current_app.logger.warning(f'{ex}')
        return {"strerror:", str(ex)}, 400
    return result


@api.route('/infoDataValue/<int:lic>')
def get_values(lic):
    """Возвращаем список начислений по заданному лицевому счету"""
    current_app.logger.debug(f'Возвращаем список начислений по лицевому счету {lic}')
    try:
        result = get_dbase().get_values(lic)
    except Exception as ex:
        current_app.logger.warning(f'{ex}')
        return {"strerror:", str(ex)}, 400
    return result


@api.route('/infoDataPaym/<int:lic>')
def get_payments(lic):
    """Возвращаем список платежей по заданному лицевому счету"""
    current_app.logger.debug(f'Возвращаем список платежей по лицевому счету {lic}')
    try:
        result = get_dbase().get_payments(lic)
    except Exception as ex:
        current_app.logger.warning(f'{ex}')
        return {"strerror:", str(ex)}, 400
    return result


@api.route('/puAddValue/<int:pu_id>/<int:value>', methods=['GET'])
@api.route('/puAddValue/<int:pu_id>/<float:value>', methods=['GET'])
def pu_add_value_get(pu_id, value):
    """Добавление ППУ"""
    current_app.logger.debug(f'Добавление показания (код ПУ: {pu_id} показание: {value})')
    try:
        result = get_dbase().pu_add_value(pu_id, value)
    except Exception as ex:
        current_app.logger.warning(f'{ex}')
        return {"strerror:", str(ex)}, 400
    return result


@api.route('/puAddValue', methods=['GET', 'POST'])
def pu_add_value():
    """Добавление ППУ"""
    try:
        if request.method == 'POST':
            pu_id = int(request.json['pu_id'])
            value = float(request.json['value'])
        else:
            pu_id = int(request.args.get('pu_id'))
            value = float(request.args.get('value'))
    except Exception as ex:
        return {"strerror:", str(ex)}, 400
    current_app.logger.debug(f'Добавление показания (код ПУ: {pu_id} показание: {value})')
    try:
        result = get_dbase().pu_add_value(pu_id, value)
    except Exception as ex:
        current_app.logger.warning(f'{ex}')
        return {"strerror:", str(ex)}, 400
    return result


@api.route('/puDelValue/<int:pu_id>/<int:id_value>', methods=['GET', 'POST'])
def pu_del_value(pu_id, id_value):
    """Удаление ППУ"""
    current_app.logger.debug(f'Удаление показания (код ПУ: {pu_id} код ППУ: {id_value})')
    try:
        result = get_dbase().pu_del_value(pu_id, id_value)
    except Exception as ex:
        current_app.logger.warning(f'{ex}')
        return {"strerror:", str(ex)}, 400
    return result
