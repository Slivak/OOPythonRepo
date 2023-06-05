class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y


    # При получении аттрибута
    def __getattribute__(self, item):
        if item == 'x':
            raise ValueError('Acces Denied')
        else:
            print('Вызван __getattribute__')
            # Возвращаем значение аттрибута, к которому мы обращаемся
            return object.__getattribute__(self, item)


    # При создании экземпляров с аттрибутами
    def __setattr__(self, key, value):
        if key == 'z':
            raise ValueError('Какая гойда?')
        else:
            print("Вызван метод__setattr__")
            object.__setattr__(self, key, value)

    # Когда идёт обращение к несуществующему аттрибуту
    def __getattr__(self, item):
        print(f'__getattr__ {item}')

    # Вызывается при удалении аттрибута
    def __delattr__(self, item):
        print(f'__delattr__ {item}')
        object.__delattr__(self, item)

pt = Point(1, 2)
a = pt.y # Вызван __getattribute__
print(a) # 1
print(pt.yy)
del pt.x
print(pt.__dict__)
