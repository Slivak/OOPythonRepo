from dataclasses import dataclass, field
from typing import Any


class GoodsMethodsFactory:
    @staticmethod

    def get_init_measure():
        return [0, 0, 0]

@dataclass
class Goods:
    # Без указания типа данных он не будет отображаться в
    # Init'е и __repr__
    current_uid = 0

    uid: int = field(init=False)

    price: Any = None
    weight: Any = None

    def __post_init__(self):
        print("Goods: post_init")
        Goods.current_uid += 1
        self.uid = Goods.current_uid

@dataclass
class Book(Goods):
    title: str = ""
    author: str = ""
    # Переопределяем аттрибуты
    price: float = 0
    weight: int | float = 0
    measure: list = field(default_factory=GoodsMethodsFactory.get_init_measure)

    def __post_init__(self):
        super().__post_init__()
        print('Book')

b = Book(1000, 100, 'OOP', 'Chichis')
print(b)