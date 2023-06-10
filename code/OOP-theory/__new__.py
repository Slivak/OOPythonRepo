class Point:
    #Аргументы так же передаются и в арги и кварги автоматически
    def __new__(cls, *args, **kwargs):
        print(f"Вызов метода __new__ для класса {str(cls)}")
        #Вызываем __new__ для получения адреса объекта
        #__new__ из общего для всех классов базового класса
        #Без ссылки на объект не сработал бы __init__
        return super().__new__(cls)

    def __init__(self, x=0, y=0):
        print(f'Вызов __init__ для класса {str(self)}')
        self.x = x
        self.y = y

pt = Point(1, 2)
print(pt)