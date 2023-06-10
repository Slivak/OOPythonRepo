# Распространение исключений
# Суть в том что ошибки распространяются стэком
# В данном случае в самой функции, во 2 функции и в принте

def func2():
    try:
        return 1 / 0
    except:
        print('func2 err')
def func1():
    try:
        return func2()
    except:
        print('func1 err')
print(func1())