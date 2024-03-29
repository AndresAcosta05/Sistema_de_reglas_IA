class Question:

    def __init__(self, id_questions=0, persistent_cough=0, chest_pain=0, difficulty_breathing=0, coughing_blood=0, sneezing=0):
        self._id_questions = id_questions
        self._persistent_cough = persistent_cough
        self._chest_pain = chest_pain
        self._difficulty_breathing = difficulty_breathing
        self._coughing_blood = coughing_blood
        self._sneezing = sneezing
    
    # getters
    @property
    def id_questions(self):
        return self._id_questions

    @property
    def persistent_cough(self):
        return self._persistent_cough
    
    @property
    def chest_pain(self):
        return self._chest_pain
    
    @property
    def difficulty_breathing(self):
        return self._difficulty_breathing
    
    @property
    def coughing_blood(self):
        return self._coughing_blood
    
    @property
    def sneezing(self):
        return self._sneezing
    
    # setters
    @id_questions.setter
    def id_questions(self, id_questions):
        self._id_questions = id_questions

    @persistent_cough.setter
    def persistent_cough(self, persistent_cough):
        self._persistent_cough = persistent_cough
    
    @chest_pain.setter
    def chest_pain(self, chest_pain):
        self._chest_pain = chest_pain
    
    @difficulty_breathing.setter
    def difficulty_breathing(self, difficulty_breathing):
        self._difficulty_breathing = difficulty_breathing
    
    @coughing_blood.setter
    def coughing_blood(self, coughing_blood):
        self._coughing_blood = coughing_blood

    @sneezing.setter
    def sneezing(self, sneezing):
        self._sneezing = sneezing
    
    def __str__(self):
        return f'PC{self._persistent_cough}, CHP{self._chest_pain}, DB{self._difficulty_breathing}, CB{self._coughing_blood}'


if __name__ == '__main__':
    question = Question(1, 0, 1, 0)
    print(question)