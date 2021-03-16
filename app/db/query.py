"""
Различные запросы к БД
"""


def get_streets(conn):
    """ 
    Получение списка улиц
    Выход: JSON - объект
    """
    query = "EXEC ws_streets"
    cursor = conn.cursor()
    data = None
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        cols = [i[0] for i in cursor.description]
        data = {"dataStreets": []}
        for item in rows:
            data["dataStreets"].append(dict(zip(cols, item)))
    except Exception as ex:
        print("Exception:", ex)
    finally:
        cursor.close()
    return data


def get_builds(conn, street_name):
    """
    Получение списка домов по заданной улице
    Выход: JSON - объект
    """
    query = "EXEC ws_builds @street_name1=?"
    params = street_name
    cursor = conn.cursor()
    data = None
    try:
        cursor.execute(query, params)
        rows = cursor.fetchall()
        cols = [i[0] for i in cursor.description]
        data = {"street_name": street_name, "dataBuilds": []}
        for item in rows:
            data["dataBuilds"].append(dict(zip(cols, item)))
    except Exception as ex:
        print("Exception:", ex)
    finally:
        cursor.close()
    return data


def get_flats(conn, street_name, nom_dom):
    """
    Получение списка квартир по заданной улице и дому
    Выход: JSON - объект
    """
    query = "EXEC ws_flats @street_name1=?, @nom_dom1=?"
    params = (street_name, nom_dom)
    cursor = conn.cursor()
    data = None
    try:
        cursor.execute(query, params)
        rows = cursor.fetchall()
        cols = [i[0] for i in cursor.description]
        data = {"street_name": street_name, "nom_dom": nom_dom, "dataKvr": []}
        for item in rows:
            data["dataKvr"].append(dict(zip(cols, item)))
    except Exception as ex:
        print("Exception:", ex)
    finally:
        cursor.close()
    return data


def get_lics(conn, street_name, nom_dom, nom_kvr):
    """
    Получение списка лицевых по заданной улице,дому и квартире
    Выход: JSON - объект
    """
    query = "EXEC ws_occ_address @street_name1=?, @nom_dom1=?, @nom_kvr1=?"
    params = (street_name, nom_dom, nom_kvr)
    cursor = conn.cursor()
    data = None
    try:
        cursor.execute(query, params)
        rows = cursor.fetchall()
        cols = [i[0] for i in cursor.description]
        data = {"street_name": street_name, "nom_dom": nom_dom, "nom_kvr": nom_kvr, "dataKvrLic": []}
        for item in rows:
            data["dataKvrLic"].append(dict(zip(cols, item)))
    except Exception as ex:
        print("Exception:", ex)
    finally:
        cursor.close()
    return data


def get_occ(conn, occ):
    """
    Получение списка лицевых по заданной улице,дому и квартире
    Выход: JSON - объект
    """
    query = "EXEC ws_show_occ @occ=?"
    params = occ
    cursor = conn.cursor()
    data = None
    try:
        cursor.execute(query, params)
        row = cursor.fetchone()
        if not row:
            data = {"lic": occ, "dataOcc": {}}
        else:
            cols = [i[0] for i in cursor.description]
            data = {
                "lic": occ,
                "dataOcc": dict(zip(cols, row)),
                "dataCounter": get_counters(conn, occ),
                "dataCounterValue": get_counter_values(conn, occ)
            }
    except Exception as ex:
        print("Exception:", ex)
    finally:
        cursor.close()
    return data


def get_counter_values(conn, occ):
    """
    Получение списка показаний приборов учета по лицевому счету
    Выход: JSON - объект
    """
    query = "exec ws_show_counters_value @occ=?, @row1=?"
    kolval = 6
    params = (occ, kolval)
    cursor = conn.cursor()
    data = {}
    try:
        cursor.execute(query, params)
        rows = cursor.fetchall()
        cols = [i[0] for i in cursor.description]
        data["dataCounterValue"] = []
        for item in rows:
            data["dataCounterValue"].append(dict(zip(cols, item)))

    except Exception as ex:
        print("Exception:", ex)
    finally:
        cursor.close()
    return data


def get_counters(conn, occ):
    """
    Получение списка приборов учета по лицевому счету
    Выход: JSON - объект
    """
    query = "exec ws_show_counters @occ=?"
    params = occ
    cursor = conn.cursor()
    data = {}
    try:
        cursor.execute(query, params)
        rows = cursor.fetchall()
        cols = [i[0] for i in cursor.description]
        data["dataCounter"] = []
        for item in rows:
            data["dataCounter"].append(dict(zip(cols, item)))

    except Exception as ex:
        print("Exception:", ex)
    finally:
        cursor.close()
    return data
