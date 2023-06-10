"""
try:
    20 / 5

# z Является ссылкой на класс исключения с заготовленным текстом
# Исключения
except ZeroDivisionError as z:
    print(z)

# Любое другое исключение можно так же записать и вот так
except:
    print('Другая ошибка!')

# Срабатывает если ошибка не произошла
else:
    print('Ошибок не произошло')

finally:
    print('Блок finally срабатывает ваще всегда')
"""

try:
    f = open("file.txt")
    # Мы не можем записать инфу в файл в режиме чтения
    # f.write('Yo')

except FileNotFoundError as x:
    print(x)
except:
    print('Другая ошибка')

else:
    print('Операция с файлом успешно проведена')

finally:
    if f:
        f.close()
        print(f'файл: {f} закрыт')

# В функциях блок finally выполняется до return
# try except может быть так же вложен в try