class Clock:
    __DAY = 86400

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Только int")
        self.seconds = seconds % self.__DAY


    @classmethod
    def verify_data(cls, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError("Только int / Clock")

        return other if isinstance(other, int) else other.seconds
    def __eq__(self, other):
        sc = self.verify_data(other)
        return self.seconds == sc

    def __lt__(self, other):
        sc = self.verify_data(other)
        return self.seconds < sc

    def __gt__(self, other):
        sc = self.verify_data(other)
        return self.seconds > sc


c1 = Clock(1000)
c2 = Clock(1000)
# Без маг.методов мы просто тупо сравниваем id
#print(c1 == c2) # False

# С методом __eq__
print(c1 == c2) # True
# неравно тоже робит
print(c1 != c2)

c3 = Clock(900)
c4 = Clock(1000)
print(c3 < c4)
# Больше тоже реверсивно робит и без его прописания
print(c3 > c4)