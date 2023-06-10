"""class Point:
    MAX_COORD = 100
    MIN_CORD = 0"""

# Реализация пользовательского метакласса через функцию
"""
def create_class_point(name, base, attrs):
    # Срабатывает если мы не прописали аттрибуты при вызове
    attrs.update({'MAX_COORD': 100, 'MIN_COORD': 0})
    return type(name, base, attrs)
    
    
class Point(metaclass=create_class_point):
    def get_coords(self):
        return (0, 0)

pt = Point()
print(pt.get_coords())
print(pt.MAX_COORD)
"""

# Реализация Через Класс

class Meta(type):

    def __new__(cls, name, base, attrs):
        attrs.update({'MAX_COORD': 100, 'MIN_COORD': 0})
        return type.__new__(cls, name, base, attrs)

    #def __init__(cls, name, base, attrs):
        #super().__init__(name, base, attrs)
        #cls.MAX_COORD = 100
        #cls.MIN_COORD = 0

class Point(metaclass=Meta):
    def get_coords(self):
        return (0, 0)
pt = Point()
print(pt.get_coords())
print(pt.MAX_COORD)