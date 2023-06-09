from dataclasses import dataclass, field, InitVar
class Vector3D:
    def __init__(self, x: int, y: int, z: int, calc_len: bool = True):
        self.x = x
        self.y = y
        self.z = z
        self.length = (x**2 + y**2 + z**2) ** 0.5 if calc_len else 0

@dataclass()
class V3D:
    # Не входящее в __repr__ в вывод
    x: int = field(repr=False)
    y: int
    # Не сравниваемое
    z: int = field(compare=False)
    # InitVar отправляет в __post_init__
    calc_len: InitVar[bool] = True

    # А это вообще ловушка пениса.
    # Дело в том, что в датаклассах в метод __repr__
    # Который робит автоматом, передают только свойства, прописанные вот так явно, а не в  __post_init__
    # Но здесь мы прописываем его для вывода, но в функции field мы говорим, что значение своё length получает не в init'е
    length: float = field(init=False, compare=False, default=0)


    # __post_init__ срабатывает последним в классе
    # К этому моменту уже созданы наши локальные свойства
    # И мы можем их использовать
    def __post_init__(self, clac_len: bool):
        if clac_len:
            self.length = (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

v = V3D(1, 2, 3)
print(v)