"""
class point2D:
    __slots__ = ('x', 'y', '__length')

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__length = (x**2 + y**2) ** 0.5

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, a):
        self.__length = a
"""

class Point2D:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y
class Point3D(Point2D):
    pass

# бан локальных свойств из __slots__ не унаследовался
pt3 = Point3D(10, 20)
pt3.z = 30 # Всё робит

# __dict__ тоже робит, но выводит только новые свойства не из __slots__
print(pt3.__dict__) # {'z': 30}

# Даже после удаления и создания вновь
del pt3.x
pt3.x = 10

# Всё равно не отображается
print(pt3.__dict__)

# Но если мы сделаем так:

class Point2D:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y
class Point3D(Point2D):
    __slots__ = ()
    # При записи вида __slots__ = 'z', мы добавляем z в возможные локальные свойства
    # Но ещё и наследуем x и y

pt3 = Point3D(10, 20)
# pt3.z = 30
# То уже нихера не робит, ведь мы переопределили __slots__

class Point2D:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y
class Point3D(Point2D):
    __slots__ = 'z',

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

pt3 = Point3D(10, 20, 30) # Робит
