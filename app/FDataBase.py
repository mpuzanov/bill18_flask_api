
class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_streets(self):
        """
        Получение списка улиц
        Выход: JSON - объект
        """
        data = None
        sql = "EXEC ws_streets"
        try:
            self.__cur.execute(sql)
            rows = self.__cur.fetchall()
            cols = [i[0] for i in self.__cur.description]
            data = {"dataStreets": []}
            for item in rows:
                data["dataStreets"].append(dict(zip(cols, item)))
        except Exception as ex:
            print("Exception:", ex)
        return data

    def get_builds(self, street_name):
        """
        Получение списка домов по заданной улице
        Выход: JSON - объект
        """
        sql = "EXEC ws_builds @street_name1=?"
        params = street_name
        data = None
        try:
            self.__cur.execute(sql, params)
            rows = self.__cur.fetchall()
            cols = [i[0] for i in self.__cur.description]
            data = {"street_name": street_name, "dataBuilds": []}
            for item in rows:
                data["dataBuilds"].append(dict(zip(cols, item)))
        except Exception as ex:
            print("Exception:", ex)
        return data

    def get_flats(self, street_name, nom_dom):
        """
        Получение списка квартир по заданной улице и дому
        Выход: JSON - объект
        """
        sql = "EXEC ws_flats @street_name1=?, @nom_dom1=?"
        params = (street_name, nom_dom)
        data = None
        try:
            self.__cur.execute(sql, params)
            rows = self.__cur.fetchall()
            cols = [i[0] for i in self.__cur.description]
            data = {"street_name": street_name, "nom_dom": nom_dom, "dataKvr": []}
            for item in rows:
                data["dataKvr"].append(dict(zip(cols, item)))
        except Exception as ex:
            print("Exception:", ex)
        return data

    def get_lics(self, street_name, nom_dom, nom_kvr):
        """
        Получение списка лицевых по заданной улице,дому и квартире
        Выход: JSON - объект
        """
        query = "EXEC ws_occ_address @street_name1=?, @nom_dom1=?, @nom_kvr1=?"
        params = (street_name, nom_dom, nom_kvr)
        data = None
        try:
            self.__cur.execute(query, params)
            rows = self.__cur.fetchall()
            cols = [i[0] for i in self.__cur.description]
            data = {"street_name": street_name, "nom_dom": nom_dom, "nom_kvr": nom_kvr, "dataKvrLic": []}
            for item in rows:
                data["dataKvrLic"].append(dict(zip(cols, item)))
        except Exception as ex:
            print("Exception:", ex)
        return data

    def get_occ(self, occ):
        """
        Получение списка лицевых по заданной улице,дому и квартире
        Выход: JSON - объект
        """
        sql = "EXEC ws_show_occ @occ=?"
        params = occ
        data = None
        try:
            self.__cur.execute(sql, params)
            row = self.__cur.fetchone()
            if not row:
                data = {"lic": occ, "dataOcc": {}}
            else:
                cols = [i[0] for i in self.__cur.description]
                data = {
                    "lic": occ,
                    "dataOcc": dict(zip(cols, row)),
                    "dataCounter": self.get_counters(occ),
                    "dataCounterValue": self.get_counter_values(occ)
                }
        except Exception as ex:
            print("Exception:", ex)
        return data

    def get_counter_values(self, occ):
        """
        Получение списка показаний приборов учета по лицевому счету
        Выход: JSON - объект
        """
        sql = "exec ws_show_counters_value @occ=?, @row1=?"
        kolval = 6
        params = (occ, kolval)
        data = {}
        try:
            self.__cur.execute(sql, params)
            rows = self.__cur.fetchall()
            cols = [i[0] for i in self.__cur.description]
            data["dataCounterValue"] = []
            for item in rows:
                data["dataCounterValue"].append(dict(zip(cols, item)))

        except Exception as ex:
            print("Exception:", ex)
        return data

    def get_counters(self, occ):
        """
        Получение списка приборов учета по лицевому счету
        Выход: JSON - объект
        """
        sql = "exec ws_show_counters @occ=?"
        params = occ
        data = {}
        try:
            self.__cur.execute(sql, params)
            rows = self.__cur.fetchall()
            cols = [i[0] for i in self.__cur.description]
            data["dataCounter"] = []
            for item in rows:
                data["dataCounter"].append(dict(zip(cols, item)))

        except Exception as ex:
            print("Exception:", ex)
        return data

    def get_values(self, occ):
        """
        Получение начислений по лицевому счету
        Выход: JSON - объект
        """
        sql = "exec ws_show_values @occ=?"
        params = occ
        data = {}
        try:
            self.__cur.execute(sql, params)
            rows = self.__cur.fetchall()
            cols = [i[0] for i in self.__cur.description]
            data["dataValue"] = []
            for item in rows:
                data["dataValue"].append(dict(zip(cols, item)))

        except Exception as ex:
            print("Exception:", ex)
        return data

    def get_payments(self, occ):
        """
        Получение платежей по лицевому счету
        Выход: JSON - объект
        """
        sql = "exec ws_show_payments @occ=?"
        params = occ
        data = {}
        try:
            self.__cur.execute(sql, params)
            rows = self.__cur.fetchall()
            cols = [i[0] for i in self.__cur.description]
            data["dataPaym"] = []
            for item in rows:
                data["dataPaym"].append(dict(zip(cols, item)))

        except Exception as ex:
            print("Exception:", ex)
        return data
