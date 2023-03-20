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
        try:
            cursor = cls._db.cursor()
            cursor.execute('SELECT questions.*, users.document, users.name, users.surname, diagnoses.diagnostic from diagnoses, users, questions WHERE users.id = diagnoses.id_user AND questions.id_questions = diagnoses.id_questions')
            data = cursor.fetchall()
            diagnoses = []

            if data:
                for diagnostic in data:
                    diagnoses.append({
                        'id_questions': diagnostic[0],
                        'persistent_cough': 'SI' if diagnostic[1]==1 else 'NO',
                        'chest_pain': 'SI' if diagnostic[2]==1 else 'NO',
                        'difficulty_breathing': 'SI' if diagnostic[3]==1 else 'NO',
                        'coughing_blood': 'SI' if diagnostic[4]==1 else 'NO',
                        'sneezing': 'SI' if diagnostic[5]==1 else 'NO',
                        'document': diagnostic[6],
                        'name': diagnostic[7],
                        'surname': diagnostic[8],
                        'diagnostic': diagnostic[9]
                    })
            return diagnoses
        except Exception as e:
            print(e)
            return []
    
    @classmethod
    def insert_DG(cls, diagnostic):
        try:
            cursor = cls._db.cursor()
            sentence = 'INSERT INTO diagnoses(id_user, id_questions, diagnostic) VALUES (%s, %s, %s)'
            values = (diagnostic.id_user, diagnostic.id_questions, diagnostic.diagnostic)
            cursor.execute(sentence, values)
            cls._db.commit()
            return cursor.rowcount
        
        except Exception as e:
            print(e)
            return []
