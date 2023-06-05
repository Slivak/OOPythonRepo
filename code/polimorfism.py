#Полиморфизмы позволяют применять одни и те же команды к объектам разных классов, даже если они выполняются по-разному

class Cat:
    def sleep(self):
        print("Свернулся клубком и кайфует")

class Parrot:
    def sleep(self):
        print("На жёрдочке")

def home_sleep(animal):
    animal.sleep()

cat = Cat()
parrot = Parrot()
home_sleep(cat) # Свернулся в клубок и сладко спит.
home_sleep(parrot) # Сел на жёрдочку и уснул.

#Это и был тот легендарный полиморфизм..... Мда..
