class Goods:
    def __init__(self, name, weight, price):
        # Обращение к MixinLog
        super().__init__()
        print("Init Goods")
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f'{self.name}, {self.weight} kg, {self.price}$')

class MixinLog:
    ID = 0

    def __init__(self):
        super().__init__()
        print("init MixinLog")
        MixinLog.ID += 1
        self.id = MixinLog.ID
    def print_info(self):
        print(f"{self.id}: был продан в 3:00")

class MixinLog2:
    ID = 0

    def __init__(self):
        print("init MixinLog")
        MixinLog.ID += 1
        self.id = MixinLog.ID

class Laptop(Goods, MixinLog, MixinLog2):
    pass

l = Laptop("Thinkpad", 1.5, 220)
l.print_info() # Вызов из первого цикла в цепочке наследования
MixinLog.print_info(l) # Вызов из произвольного класса
# Здесь идёт цепочка обхода классов
print(Laptop.__mro__)
# В таком ужасе лучше прописывать все классы, вызванные через super
# Без параметров, т.к туповатый кодер может напутать цепочку наследования
# В самом первом классе по вызову Laptop