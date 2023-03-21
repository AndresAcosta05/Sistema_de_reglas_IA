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
        try:
            cursor = cls._db.cursor()
            cursor.execute('SELECT * FROM questions')
            data = cursor.fetchall()
            questions = []

            if data:
                for question in data:
                    questions.append(Question(question[0], question[1], question[2], question[3], question[4]))
            return questions
        
        except Exception as e:
            print(e)
            return []
    
    @classmethod
    def insert_QU(cls, questions):
        try:
            cursor = cls._db.cursor()
            sentence = 'INSERT INTO questions(persistent_cough, chest_pain, difficulty_breathing, coughing_blood, sneezing) VALUES (%s, %s, %s, %s, %s)'
            values = (questions.persistent_cough, questions.chest_pain, questions.difficulty_breathing, questions.coughing_blood, questions.sneezing)
            cursor.execute(sentence, values)
            cls._db.commit()
            return cursor.lastrowid
        
        except Exception as e:
            print(e)
            return []