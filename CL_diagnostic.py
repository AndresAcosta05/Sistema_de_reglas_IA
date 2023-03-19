class Diagnostic:

    def __init__(self, id_diagnostic=0, id_user=0, id_questions=0, diagnostic=0):
        self._id_diagnostic = id_diagnostic
        self._id_user = id_user
        self._id_questions = id_questions
        self._diagnostic = diagnostic

    # getters
    @property
    def id_diagnostic(self):
        return self._id_diagnostic
    
    @property
    def id_user(self):
        return self._id_user
    
    @property
    def id_questions(self):
        return self._id_questions
    
    @property
    def diagnostic(self):
        return self._diagnostic
    
    # setters
    @id_diagnostic.setter
    def id_diagnostic(self, id_diagnostic):
        self._id_diagnostic = id_diagnostic
    
    @id_user.setter
    def id_user(self, id_user):
        self._id_user = id_user
    
    @id_questions.setter
    def id_questions(self, id_questions):
        self._id_questions = id_questions
    
    @diagnostic.setter
    def diagnostic(self, diagnostic):
        self._diagnostic = diagnostic
    
    def __str__(self):
        return f'IDG{self._id_diagnostic}, US{self._id_user}, QS{self._id_questions}, DG{self._diagnostic}'
