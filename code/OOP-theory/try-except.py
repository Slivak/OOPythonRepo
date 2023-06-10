a = int(input())
try:
    print(100 / a)

except ZeroDivisionError:
    print("На ноль делить нельзя")

try:
    x, y = map(float, input().split())

except ValueError:
    print('некорректные данные')

print(x, y)


a = int(input())
try:
    print(100 / a)

# Обрабатывает всё
except Exception:
    print("Ошибка")

# Принято сначала прописывать основные возможные исключения,
# И только затем общее Exception на все остальные случаи