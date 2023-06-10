"""
class Counter:
    def __init__(self):
        self.__counter = 0

    def __call__(self, step=1, *args, **kwargs):
        print('__call__')
        self.__counter += step
        return self.__counter
c = Counter()
# c - функтор (экз. класса, которы можно вызывать как функцию
# Всё это благодаря магическому методу __call__
c()

for i in range(60):
    c()
res = c(2, 4543, c=3)
print(res)
"""

class RemoveChars:
    def __init__(self, chars):
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise TypeError('Must be a string')
        self.__chars = self.__chars.lower()
        return args[0].lower().strip(self.__chars)

a = RemoveChars('v')
res = a('  Venchislav')
print(res)