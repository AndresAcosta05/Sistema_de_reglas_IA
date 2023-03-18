class User:

    def __init__(self, id, document, name, second_name, surname, second_surname, user, password):
        self._id = id
        self._document = document
        self._name = name
        self._second_name = second_name
        self._surname = surname
        self._second_surname = second_surname
        self._user = user
        self._password = password
        self._created_at = ''
    # getters
    @property
    def id(self):
        return self._id
    
    @property
    def document(self):
        return self._document
    
    @property
    def name(self):
        return self._name
    
    @property
    def second_name(self):
        return self._second_name
    
    @property
    def surname(self):
        return self._surname
    
    @property
    def second_surname(self):
        return self._second_surname
    
    @property
    def user(self):
        return self._user
    
    @property
    def password(self):
        return self._password
    
    # setters
    @id.setter
    def id(self, id):
        self._id = id
    
    @document.setter
    def document(self, document):
        self._document = document
    
    @name.setter
    def name(self, name):
        self._name = name
    
    @second_name.setter
    def second_name(self, second_name):
        self._second_name = second_name
    
    @surname.setter
    def surname(self, surname):
        self._surname = surname
    
    @second_surname.setter
    def second_surname(self, second_surname):
        self._second_surname = second_surname
    
    @user.setter
    def user(self, user):
        self._user = user
    
    @password.setter
    def password(self, password):
        self._password = password
    
    def __str__(self):
        return f'{self._id}, {self._document}, {self._name}, {self._second_name}, {self._surname}, {self._second_surname}, {self._user}, {self._password}'
    

if __name__ == '__main__':
    user1 = User(1, '10028772', 'Juan', '', 'Gonzales', 'Ortega', 'juani', '1345666')
    print(user1)
