# to use this need execute the command pip install mysql-connector-python
import mysql.connector


class Connection:
    
    _database = 'rules_system'
    _user = 'root'
    _password = ''
    _host = 'localhost'

    _conecction = mysql.connector.connect(
        host=_host,
        user=_user,
        passwd=_password,
        db=_database
    )

    def get_connection(self):
        return self._conecction

