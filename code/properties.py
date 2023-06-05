#Здесь идёт речь про инкапсуляцию
#Закрытие некоторых методов класса для чтения


class Cat():
    def __init__(self, breed, color, age):
        # _ сделал наши аттрибуты закрытыми
        # И доступными только внутри класса

        self._breed = breed
        self._color = color
        self._age = age

    # @property даёт доступ к аттрибутам для методов
    # Которые возвращают их значения

    @property
    def breed(self):
        return self._breed

    @property
    def color(self):
        return self._color

    @property
    def age(self):
        return self._age

    # @age.setter даёт нам возможность изменять пользователю
    # возраст, но только при условии, что возраст увеличивается
    @age.setter
    def age(self, new_age):
        if new_age > self._age:
            self._age = new_age
        return  self._age

cat = Cat('Абиссинская', 'Рыжая', 4)

print(cat.breed) # Абиссинская
print(cat.color) # Рыжая
print(cat.age) # 4

cat.age = 2 # Не изменится
print(cat.age) # 4
cat.age = 6 #Изменится
print(cat.age) # 6


try:
    cat.breed = "Люсьеновская"
    print(cat.breed) # А это вообще не сработает

except:
    print("Не робит т.к аттрибут breed доступен только для чтения")
