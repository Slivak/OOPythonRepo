"""

class Drink:

    # Статичный объём
    _volume = 200

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self._remains = self._volume

    def drink_info(self):
        print(f"Название: {self.name}. Стоимость: {self.price}. Объём: {self._volume}. Осталось: {self._remains}")


    def _is_enough(self, need):
        if self._remains >= need and self._remains > 0:
            return True
        print("Недостаточно напитка")
        return False

    # Метод, чтобы сказать другу сделать глоток.
    def sip(self):
        if self._is_enough(20):
            self._remains -= 20
            print('Друг сделал глоток')

    def small_sip(self):
        if self._is_enough(10):
            self._remains -= 10
            print('Друг сделал маленький глоток')

    def drink_all(self):
        if self._is_enough(0):
            self._remains = 0
            print("ЗАЛПОМ КОМБО")

    def tell_price(self):
        print('Homie говорит цену напитка')
        return self.price

# У методов классов есть модификаторы доступа
# А именно public private protected
# private (__example) доступ только внутри класса (даже вызвать нельзя)
# public ну понятно что везде (методы по умолчанию public)
# protected (_example) доступ так же есть у классов наследников, но не извне (хотя их можно вызвать)

# Возможность игнорировать уровни доступа — нарушение важного для ООП принципа инкапсуляции.
# Поэтому, несмотря на наличие технической возможности, программисты, пишущие на Python, договорились не обращаться к защищённым и приватным методам откуда-то извне.


class Juice(Drink):
    _juice_name = 'Cок'
    def __init__(self, price, taste):
        super().__init__(self._juice_name, price)
        self.taste = taste

    # Переопределяем родительский метод drink_info, чтобы он сообщал нам информацию о вкусе сока.

    def drink_info(self):
        print(f'Вкус сока: {self.taste}. Стоимость: {self.price}. Начальный объём: {self._volume}. Осталось: {self._remains}')



coffe = Drink('Кофе', 300)
coffe.remains = 10
coffe.sip()
coffe.drink_info()

coffe.small_sip()
coffe.drink_info()


# Создаём экземпляр класса Juice.
apple_juice = Juice(250, 'яблочный')

# Пробуем вызвать методы, прописанные в родительском классе Drink.
apple_juice.small_sip() # Говорим другу сделать маленький глоток.
apple_juice.sip() # Говорим другу сделать обычный глоток.
apple_juice.drink_info() # Просим друга сообщить информацию о напитке.


tea = Drink('чай', 500)
print (tea.tell_price()) # Сначала друг объявит стоимость чая.
beetlejuice = Juice(1988, 'жучиный')
print (beetlejuice.tell_price())"""

def sel_sort(arr):
    new_arr = []

    for n in range(len(arr)):
        lowest_index = arr.index(min(arr))
        new_arr.append(arr.popleft(lowest_index))
    return new_arr

print(sel_sort([4, 2, 0, 9]))