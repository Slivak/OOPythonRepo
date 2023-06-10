from dataclasses import dataclass, field
from pprint import pprint

# Обычный класс
class Thing:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __repr__(self):
        return f'Thing: {self.__dict__}'

# А это тот же класс, только проще и датакласс
@dataclass
class ThingData:
    name: str
    weight: int
    price: float = 0
    # При создании объекта экза ставит dims пустым списком
    dims: list = field(default_factory=list)

    def __eq__(self, other):
        return self.weight == other.weight

#t = Thing('Python', 100, 1024)
#print(t)

td = ThingData('JS', 100, 1024)
# print(td)
#pprint(ThingData.__dict__)
td_2 = ThingData('jhk', 10, 104)
td_3 = ThingData('jhk', 10)

# Сравнивает по аттрибутам
print(td == td_2) # False
print(td_2 == td_3) # True

# Однако сейчас прога робит иначе, т.к прописан __eq__ по весу
# Но по умолчанию всё же сравнивает объекты по всем аттрам

print(td)

td.dims.append(10)
print(td.dims)