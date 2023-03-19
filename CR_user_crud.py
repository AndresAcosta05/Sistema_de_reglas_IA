from DB_database import Connection
from CL_user import User

class user_Crud:

    _connection = Connection()
    _db = _connection.get_connection()

    @classmethod
    def select_US(cls):
        with cls._db as db:
            with db.cursor() as cursor:
                cursor.execute('SELECT * FROM users')
                data = cursor.fetchall()
                users = []
                if data:
                    for user in data:
                        users.append(User(user[0], user[1], user[2], user[3], user[4], user[5], user[6], user[7]))
                return users
    
    @classmethod
    def login_US(cls, user):
        with cls._db as db:
            with db.cursor() as cursor:
                cursor.execute(f'SELECT * from users WHERE user="{user.user}" AND password="{user.password}"')
                data = cursor.fetchone()
                if data:
                    user = User(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7])
                else:
                    user = []
                return user
    
    @classmethod
    def insert_US(cls, user):
        with cls._db as db:
            with db.cursor() as cursor:
                sentence = 'INSERT INTO users(document, name, second_name, surname, second_surname, user, password, created_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
                values = (user.document, user.name, user.second_name, user.surname, user.second_surname, user.user, user.password, "")
                cursor.execute(sentence, values)
                return cursor.rowcount
            

crud = user_Crud()
user = User(user="Samir",password="123")
print(crud.insert_US(user))