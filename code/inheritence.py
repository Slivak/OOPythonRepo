# Наследование аттрибутов и методов классов

# Наш уже известный класс Cat
class Cat():
    def __init__(self, breed, color, age):
        self.breed = breed
        self.color = color
        self.age = age

    def meow(self):
        print("Мяу")

    def purr(self):
        print("Мррррр")

    def about(self):
        print(self.color)
        print(self.breed)
        print(self.age)

class HomeCat(Cat):
    def __init__(self, breed, color, age, owner, name):
        # Заполняет аттрибуты класса родителя
        # Но мы так же передаём
        # Как я понял super() ГРУБО говоря обращается к родителю
        # А здесь конкретно к его __init__'у

        super().__init__(breed, color, age)
        self._owner = owner
        self._name = name

    @property
    def owner(self):
        return self._owner

    @property
    def name(self):
        return self._name

    def getTreat(self):
        print("мяу Мяу Мяу (дай поесть)")

# Та-Дам
home_cat1 = HomeCat('НоуНейм', 'Чёрно-Белый', 7, 'Сявик', 'Люсян')
print(home_cat1.owner)
print(home_cat1.breed)
# Причём даже методы копируются!
home_cat1.getTreat() # Мяу-мяу
home_cat1.purr() # Мрррр
