"""class FRange:
    def __init__(self, start=0.0, stop=0.0, step=1.0):
        self.start = start
        self.stop = stop
        self.step = step
        self.value = self.start - self.step

    def __iter__(self):
        self.value = self.start - self.step
        return self
    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration

fr = FRange(0, 2, 0.5)

for i in range(4):
    print(next(fr))

print('_____________\n')
# Благодаря __iter__ экз теперь итерируем
for x in fr:
    print(x)





class FRange2D:
    def __init__(self, start=0.0, stop=0.0, step=1.0, rows=5):
        self.rows = rows
        self.fr = FRange(start, stop, step)

    def __iter__(self):
        self.value = 0
        return self

    def __next__(self):
        if self.value < self.rows:
            self.value += 1
            return iter(self.fr)
        else:
            raise StopIteration

print('_____________')
fr2 = FRange2D(0, 2, 0.5, 4)
for row in fr2:
    for x in row:
        print(x, end=' ')
    print()
print('_____________\n')"""

class Nums:
    def __init__(self, y):
        self.y = y
    def __next__(self):
        if self.y < 100:
            self.y += 1
        else:
            raise StopIteration

    def __iter__(self):
        self.y = 0
        return self

n1 = Nums(5)
next(n1)
print(n1.y)

# __iter__ следует условию в __next__ и итерирует объекты
for x in n1:
    print(n1.y)
