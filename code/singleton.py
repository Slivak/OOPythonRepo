"""
Принцип SingleTon подразумевает создание только одного объекта
Экземпляра класса. Если же создаются 2 и более объекта, то мы
в них определяем ссылку на уже созданный 1 объект.
Перед созданием объекта мы проверяем их количество
"""
class DataBase:

    # Ссылка на экземпляр класса
    # Чекаем есть объект или нет
    __instance = None

    # Если не создан объект, то даём его создать (только 1)
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __del__(self):
        DataBase.__instance = None

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f'Соединение с бд: {self.user}, {self.psw}, {self.port}')

    def close(self):
        print('Закрытие соединения с БД')

    def read(self):
         return 'Данные из БД'

    def write(self, data):
        print(f'Запись {data} в БД')

db = DataBase('root', '1234', 80)
db2 = DataBase('Groot', '5678', 40)
print(id(db), id(db2))
# id равны, а значит они действительно ссылаются на 1 объект
# EZ ура!
# Но...

db.connect()
db2.connect()

# У нас уже не root, а Groot...
# Это можно пофиксить, но я пока незнайка