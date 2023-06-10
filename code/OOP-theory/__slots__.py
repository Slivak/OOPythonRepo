class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Point2D:
    # Доступные имена свойств
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(2, 3)
p.z = 4

p2 = Point2D(2, 3)
# p2.z = 4 - выдаст ошибку, т.к в 2Д у нас нет 3 измерения
# Для этого мы и  прописали __slots__
# p2.__dict__ - к слову коллекция __dict__ у таких классов и их экзов не формируется


