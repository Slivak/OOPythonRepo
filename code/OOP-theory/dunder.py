"""
class Cat:
    def __init__(self, name):
        self.name = name

    # Для кодеров в режиме отладки
    def __repr__(self):
        return f"{self.__class__}: {self.name}"

    # Для пользователей при выводе print или str
    def __str__(self):
        return f"{self.name}"

"""

class Point:
    def __init__(self, *args):
        self.__cords = args

    # Просто позволяет нам выводить длину экземпляров класса
    def __len__(self):
        return len(self.__cords)

    # Просто позволяет нам использовать функцию модуля к экзам
    def __abs__(self):
        return list(map(abs, self.__cords))

p = Point(1, -2)
print(len(p)) # 2
print(abs(p)) # [1, 2]

# EZ