class Point:
    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        if isinstance(x, (int, float)) and isinstance(y, (int, float)):
            self.__x = x
            self.__y = y

    def set_coord(self, x, y):
        if isinstance(x, (int, float)) and isinstance(y, (int, float)):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Должны быть числа")

    def get_coords(self):
        return self.__x, self.__y

pt = Point(1, 2)
print(pt.get_coords())
pt.set_coord(10, 20)
print(pt.get_coords())