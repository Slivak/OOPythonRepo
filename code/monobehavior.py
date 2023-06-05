class Smth:
    __instance = {
        'name': 'thread1',
        'id': 3
    }

    def __init__(self):
        self.__dict__ = self.__instance

d1 = Smth()
d2 = Smth()