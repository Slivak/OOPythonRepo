class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return  self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @age.deleter
    def age(self):
        del self.__age

p = Person('Dude', 23)
p.age = 35
print(p.age, p.__dict__)

# Удаление через deleter
del p.age
print(p.__dict__)