"""
class Soda:
    def __init__(self, addon):
        # Грубо говря если addon string
        if isinstance(addon, str):
            self.addon = addon
        else:
            self.addon = None

    def show_my_drink(self):
        if self.addon != None:
            return f'Газировка и {self.addon}'
        else:
            return 'Обычная газировка'


cola = Soda(5)
print(cola.show_my_drink())

cola = Soda("малинка стар")
print(cola.show_my_drink())
"""


"""
class TriangleChecker:
    def __init__(self, triangle_sides):
        self.sides = triangle_sides

    def is_triangle(self):
        if all(isinstance(i, (int, float)) for i in self.sides):
            if all(i > 0 for i in self.sides):
                sorted_sides = sorted(self.sides)
                if sorted_sides[0] + sorted_sides[1] > sorted_sides[2]:
                    return 'Можно построить треугольник'
                return 'Нельзя построить'
            return 'числа должны быть положительные'
        return 'стороны должны быть числами!'

# Тесты
triangle1 = TriangleChecker([2, 3, 4])
print(triangle1.is_triangle())
triangle2 = TriangleChecker([77, 3, 4])
print(triangle2.is_triangle())
triangle3 = TriangleChecker([77, 3, 'Сторона3'])
print(triangle3.is_triangle())
triangle4 = TriangleChecker([77, -3, 4])
print(triangle4.is_triangle())
"""

"""
class KgToPounds:
    def __init__(self, kg):
        self.__kg = kg

    def to_pounds(self):
        return self.__kg * 2.205

    @property
    def kg(self):
        return self.__kg

    @kg.setter
    def kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            # Вызываем ошибочку со своим комментарием
            raise ValueError('Значение должно быть числом')

weight = KgToPounds(12)
print(weight.to_pounds())
print(weight.kg)
weight.kg = 41
print(weight.kg)

weight.kg = 'десять'
print(weight.kg)
"""

class Slavrentiy:
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        if name.lower() == 'славяныч':
            self.name = name
        else:
            self.name =  f'Я не {name} я Славяныч!'
        self.age = age

slava = Slavrentiy('Славяныч', 14)
print(slava.name)
