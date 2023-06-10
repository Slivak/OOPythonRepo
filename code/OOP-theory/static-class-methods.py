class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    # Может работать только с экземплярами класса
    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y):
        self.x = self.y = 0
        # Экземпляр уже содержит в себе инфо о классе
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y
        # Вызов статикметда внутри метода класса
        print(self.norm2(self.x, self.y))

    # Это самый типичный метод
    def get_coord(self):
        return self.x, self.y
    # Есть ещё @staticmethod и @classmethod

    # Статический метод работает ни с аттрибутами классов
    # Ни с аттрибутами методов
    # Но при этом его можно вызывать в классе и его методах
    @staticmethod
    def norm2(x, y):
        return x**2 + y**2




v = Vector(1000, 4)
print(v.get_coord())

v = Vector(1, 4)
print(v.get_coord())

# Квадрат нормы наш статичный метод
print(Vector.norm2(5, 6))