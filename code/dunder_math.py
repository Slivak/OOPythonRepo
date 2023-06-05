class Clock:
    __DAY = 86400

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть в формате int")

        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f"{self.__get_formatted(h)}: " \
               f"{self.__get_formatted(m)}: " \
               f"{self.__get_formatted(s)}"

    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, "0")

    def __add__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('Прибавляй только int или Clock')
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
        return Clock(self.seconds + sc)

    # На случай если экземпляр класса при увеличении находится справа

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        print("__iadd__")
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError

        if isinstance(other, Clock):
            sc = other.seconds
        self.seconds += sc
        return self


"""
c1 = Clock(900)
c2 = Clock(2000)
print(c1.get_time())
c1 += 100
print(c1.get_time())
c3 = c1 + c2
print(c3.get_time())
c4 = c3 + c2 + c1
print(c4.get_time())
"""

c1 = Clock(100)
print(c1.get_time())
c1 = 100 + c1