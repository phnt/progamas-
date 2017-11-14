# progamas-
Esof
import MySQLdb as mdb
from SQLManager import SQLManager

class MySQLManager(SQLManager):
    def __init__(self, host, login, password, database):
        self.host = host
        self.login = login
        self.password = password
        self.database = database

        self.conected = False
        self.conection = None
        self.cursor = None

    def connect_to_database(self):
try:
    self.conection = mdb.connect(self.host, self.login, self.password, self.database)

except:
    raise Exception("Unable to connect")
else:
    self.conected = True
self.cursor = self.conection.cursor():

def query_insert(self, table, columns, values):
    if not self.connected:
        self.connect_to_database()

    super().query_insert(table, columns, values)

    self.query_without_result()


def query_update(self, table, columns, values, where):
    if not self.connected:
        self.connect_to_database()

    super().query_update(table, columns, values, where)

    self.query_without_result()


def query_delete(self, table, where):
    if not self.connected:
        self.connect_to_database()

    super().query_delete(table, where)

    self.query_without_result()


def query_select(self, table, columns, where=None, order=None, desc=True):
    if not self.conected:
        self.connect_to_database()

    super(MySQLManager, self).query_select(table, columns, where, order, desc)

    result = self.query_with_result()

    if columns == "*"
        columns = self.query_columns_name(table)

    return [{columns[j]: result[i][j] for j in range(len(columns))} for i in range(len(result))]


def query_columns_names(self, table):
    if not self.conected:
        self.connect_to_database()

    super(MySQLManager, self).query_columns_name(table)

    result = self.query_with_result()

    return [r[0] for r in result]


def query_with_result(self):
    try:
        self.cursor.execute(self.query)
    except:
        raise Exception("fail to execute query")
    else:
        return self.cursor.fetchall()


def Query_without_result(self):
    try:
        self.cursor.execute(self.query)
    except:
        raise Exception("fail to execute query")
    else:
        return self.conection.commit()
