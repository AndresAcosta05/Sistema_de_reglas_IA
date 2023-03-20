from DB_database import Connection
from CL_diagnostic import Diagnostic


class diagnostic_Crud:

    _connection = Connection()
    _db = _connection.get_connection()

    """ In this file class, it allows the crud or operation to insert, select, update delete, each fetch 
        returns an object of its class to allow a more organized fetch with respect to its class notes:

        * when insert or update you can valid if the funcion returns 1 if it doesn't it's because don't do it
        * the funcions to read the records returns [] when don't find any data
    """

    @classmethod
    def select_DG(cls):
        with cls._db as db:
            with db.cursor() as cursor:
                cursor.execute('SELECT * FROM diagnoses')
                data = cursor.fetchall()
                diagnoses = []

                if data:
                    for diagnostic in data:
                        diagnoses.append(Diagnostic(diagnostic[0], diagnostic[1], diagnostic[2], diagnostic[3]))
                return diagnoses
    
    @classmethod
    def insert_DG(cls, diagnostic):
        with cls._db as db:
            with db.cursor() as cursor:
                sentence = 'INSERT INTO diagnoses(id_user, id_questions, diagnostic) VALUES (%s, %s, %s)'
                values = (diagnostic.id_user, diagnostic.id_questions, diagnostic.diagnostic)
                cursor.execute(sentence, values)
                db.commit()
                return cursor.rowcount
