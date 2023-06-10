# OCP (Open Closed Principle) - принцип заключается в том
# Что бы новые методы/классы/функции не конфликтовали с ранеепрописанными

# Неправильно

class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def give_discount(self):
        return self.price * 0.2

    def give_discount(self):
        if self.customer == 'VIP':
            return self.price * 0.4

# Проблема вышепоказанного кода в том, что он
# Переопределяет метод give_discount сам в себе
# Из-за этого старый код уже не робит


# Правильно
class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def give_discount(self):
        return self.price * 0.2

class VIPDiscount(Discount):
    def give_discount(self):
        super().give_discount() * 2

# А тут мы ваще красавцы