class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Если нет __bool__, то при вызове функции bool() мы
    # Заюзаем __len__
    def __len__(self):
        print("__len__")
        return self.x **2 + self.y**2

    # Но в приоритете всё же __bool__
    def __bool__(self):
        print("__bool__")
        return self.x == self.y
    # Маг. метод __bool__ не возвращает числовых значений
p = Point(10, 10)
print(bool(p))

# Вот отрабатывает __bool__, проверяющий в данном случае
# равенство координат
if p:
    print("True")
else:
    print("False")