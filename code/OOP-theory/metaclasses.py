# Классы в python это тоже своего рода объекты
# И они как раз создаются метаклассами


class Point:
    MAX_COORD = 100
    MIN_COORD = 0

# type это метакласс. 1-Имя класса, 2-кортеж базовых классов, 3-аттрибуты
A = type('Point', (), {'MAX_COORD': 100, 'MIN_COORD': 0})

pt = A()
print(pt.MAX_COORD)


class B1: pass
class B2: pass

A = type('Point', (B1, B2), {'MAX_COORD': 100, 'MIN_COORD': 0})
# Теперь цепочка идёт с учётом наследований
print(A.__mro__)


def method1(self):
    print(self.__dict__)


A = type('Point', (), {'MAX_COORD': 100, 'method1': method1})
pt = A()
pt.method1()

A = type('Point', (), {'MAX_COORD': 100, 'method1': lambda self: self.MAX_COORD})
pt = A()
print(pt.method1())