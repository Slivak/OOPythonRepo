#Это класс
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


#А это объекты

cat1 = Cat('Абиссинская', 'Рыжая', 4)
cat2 = Cat('Британская', 'Серая', 2)

cat1.about()