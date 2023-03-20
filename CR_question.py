from DB_database import Connection
from CL_question import Question


class question_Crud:

    _connection = Connection()
    _db = _connection.get_connection()

    """ In this file class, it allows the crud or operation to insert, select, update delete, each fetch 
        returns an object of its class to allow a more organized fetch with respect to its class notes:

        * when insert or update you can valid if the funcion returns 1 if it doesn't it's because don't do it
        * the funcions to read the records returns [] when don't find any data
    """

    @classmethod
    def select_QU(cls):
        with cls._db as db:
            with db.cursor() as cursor:
                cursor.execute('SELECT * FROM questions')
                data = cursor.fetchall()
                questions = []

                if data:
                    for question in data:
                        questions.append(Question(question[0], question[1], question[2], question[3], question[4]))
                return questions
    
    @classmethod
    def insert_QU(cls, questions):
        with cls._db as db:
            with db.cursor() as cursor:
                sentence = 'INSERT INTO questions(persistent_cough, chest_pain, difficulty_breathing, coughing_blood) VALUES (%s, %s, %s, %s)'
                values = (questions.persistent_cough, questions.chest_pain, questions.difficulty_breathing, questions.coughing_blood)
                cursor.execute(sentence, values)
                db.commit()
                return cursor.rowcount

