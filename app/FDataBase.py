
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
                }
                data.update(self.get_counters(occ))  # добавляем в словарь другой словарь
                data.update(self.get_counter_values(occ))

        except Exception as ex:
            print("Exception:", ex)
        return data

    def get_counter_values(self, occ, kolval=6):
        """
        Получение списка показаний приборов учета по лицевому счету
        Выход: JSON - объект
        """
        sql = "exec ws_show_counters_value @occ=?, @row1=?"
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
        sql = "exec ws_show_values_occ @occ=?"
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
        sql = "exec ws_show_payings @occ=?"
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

    def pu_add_value(self, pu_id, value):
        """
        Добавление показания ПУ
        :param pu_id:
        :param value:
        :return:
        """
        sql = """declare @result_add BIT, @strerror VARCHAR(4000), @id_new INT;
        exec k_counter_value_add2 @counter_id1=?, @inspector_value1=?, 
            @result_add=@result_add OUTPUT, @strerror=@strerror OUTPUT, @id_new=@id_new OUTPUT;
        select @result_add, @strerror, @id_new;"""
        params = (pu_id, value)
        result = {'result': False, 'strerror': '', 'id_new': 0}
        try:
            self.__cur.execute(sql, params)
            rows = self.__cur.fetchone()
            result['result'] = bool(rows[0])
            result['strerror'] = rows[1]
            result['id_new'] = int(rows[2])
            self.__db.commit()
        except Exception as ex:
            print("Exception:", ex)
        return result

    def pu_del_value(self, pu_id, id_value):
        """
        Удаление показания ПУ
        :param pu_id:
        :param id_value:
        :return:
        """
        sql = """declare @result_add BIT, @strerror VARCHAR(4000);
        exec k_counter_value_del @counter_id1=?, @id1=?,
            @result_add=@result_add OUTPUT, @strerror=@strerror OUTPUT;
        select @result_add, @strerror;"""
        params = (pu_id, id_value)
        result = {'result': False, 'strerror': ''}
        try:
            self.__cur.execute(sql, params)
            rows = self.__cur.fetchone()
            result['result'] = bool(rows[0])
            result['strerror'] = rows[1]
            self.__db.commit()
        except Exception as ex:
            print("Exception:", ex)
        return result
