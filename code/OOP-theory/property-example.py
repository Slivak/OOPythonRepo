from string import ascii_letters
class Person:
    S_RUS  = 'абвгдеёжзийклмнопрстуфхцчшщъьэюя-'
    S_RUS_UPPER = S_RUS.upper()
    def __init__(self, name, age, ps, weight):
        self.verify_name(name)

        self.__name = name.split()
        self.age = age
        self.ps = ps
        self.weight = weight

    @classmethod
    def verify_name(cls, name):
        if not isinstance(name, str):
            raise TypeError('Леее')
        n = name.split()

        if len(n) != 3:
            raise TypeError('Укажите ФИО')

        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        for l in n:
            if len(l) < 1:
                raise TypeError('Ты дегенерат?')
            if len(l.strip(letters)) != 0:
                raise TypeError('Используйте разрешённые символы')


    @classmethod
    def verify_age(cls, age):
        if not isinstance(age, int) or age > 120 or age < 14:
            raise ValueError('Диапозон неверен')

    @classmethod
    def verify_weight(cls, weight):
        if not isinstance(weight, float) or weight < 20.0:
            raise ValueError('Вес должен бытб флотом > 20.0 кг')

    @classmethod
    def verify_ps(cls, ps):
        if type(ps) != str:
            raise TypeError

        s = ps.split()
        if len(s) != 2 or len(s[0])!= 4 or len(s[1])!= 6:
            raise TypeError
        for p in s:
            if not p.isdigit():
                raise TypeError

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.verify_age(age)
        self.__age = age

    @property
    def weight(self):
        return self.__age

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight

    @property
    def ps(self):
        return self.__ps

    @ps.setter
    def ps(self, ps):
        self.verify_ps(ps)
        self.__ps = ps

p = Person('Белов Вячеслав Валерьевич', 20, '1234 567890', 60.0)
p.age = 100
p.ps = '0123 456789'
p.weight = 70.0
print(p.__dict__)