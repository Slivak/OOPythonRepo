# ISP (Interface Segregation Principle) - Принцип разделения интерфейса

# Неправильно
class Shape:
    def draw_circle(self):
        print("O")

    def draw_square(self):
        print("[]")

class Circle(Shape):
    pass
# Т.К Circle наследует все методы класса Shape, то он и наследует метод draw_square
# А он ему не нужен!

# Правильно

class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("O")

class Square(Shape):
    def draw(self):
        print("[]")
