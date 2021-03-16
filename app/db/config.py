"""
Файл с настройками доступа
и создание соединения с SQL Server
"""
import pyodbc
# ===============================================
driver = '{SQL Server}'
server = 'localhost'
db = 'kr1'
user = 'sa'
pw = '123'
connectionString = f"DRIVER={driver};SERVER={server};DATABASE={db};UID={user};PWD={pw}"
# ===============================================


def get_connection():
    """
    Получаем соединение к БД
    """
    try:
        conn = pyodbc.connect(connectionString, timeout=5)
    except Exception as ex:
        print("\nError connection: ", ex)
        print(f"connectionString: {connectionString}")
    return conn
