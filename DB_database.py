# to use this need execute the command pip install mysql-connector-python
import mysql.connector


class Connection:
    
    _database = 'rules_system'
    _user = 'root'
    _password = ''
    _host = 'localhost'

    def __init__(self):
        self._conecction = mysql.connector.connect(
            host = self._host,
            user = self._user,
            passwd = self._password,
            db = self._database
        )

    def get_connection(self):
        return self._conecction

