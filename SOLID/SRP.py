# Принцип SRP (Single Responsibility) подразумевает под собой
# То, что каждая конкретная задача должна выполняться конкретной
# Функцией или классом. Не должно быть такого, что все задачи выполняются в одной функции или в одном классе

# Неправильно:

class User:
    def __init__(self, db_conn, name, surname):
        self.db = db_conn
        self.name = name
        self.surname = surname
    def get_name(self):
        return self.name

    def save_in_db(self):
        pass

# Здесь мы в одном классе создаём юзера, выводим его имя, и заносим в БД
# Что за ужас тут творится


# Правильно

class User:
    def __init__(self, name, surname):
        self.name = name
        self.surname= surname

    def get_name(self):
        return self.name

class UserModelDB:
    def get_username_from_db(self, user_id):
        pass

    def save_in_db(self):
        pass

# Мы каждую конкретную операцию поручили конкретному классу
