# LSP (Liskov substitution Principle)
# Дочерний класс не должен ломать родительский и переопределять его
# он должен расширять его функционал

# Неправильно

class Vehicle:
    def __init__(self, name: str, speed: float):
        self.name = name
        self.speed = speed

    def get_name(self) -> str:
        return f"The vehicle name {self.name}"

    def get_speed(self) -> str:
        return f"The vehicle speed {self.speed}"

    def engine(self):
        pass

    def start_engine(self):
        self.engine()

class Car(Vehicle):
    def start_engine(self):
        pass

class Bicycle(Vehicle):
    def start_engine(self):
        pass

# Всё что здесь сделали дочерние классы
# Так это просто переопределили под себя методы родителя
# для таких задач рекомендуется не использовать наследование

# Правильно
class Vehicle:
    def __init__(self, name: str, speed: float):
        self.name = name
        self.speed = speed

    def get_name(self) -> str:
        return f"The vehicle name {self.name}"

    def get_speed(self) -> str:
        return f"The vehicle speed {self.speed}"
class VehicleWithoutEngine(Vehicle):
    def start_moving(self):
        print("Покатился")

class VehicleWithEngine(Vehicle):
    def engine(self):
        pass

    def start_engine(self):
        self.engine()

class Car(VehicleWithEngine):
    def start_engine(self):
        pass

class Bicycle(VehicleWithoutEngine):
    def start_moving(self):
        pass