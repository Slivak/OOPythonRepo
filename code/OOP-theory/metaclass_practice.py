class Meta(type):
    # Это инициализатор класса Women(см. линию 11)
    def create_local_attrs(self, *args, **kwargs):
        # Тут мы просто создаём локальные аттрибуты объекта
        # Путём добавления в его коллекцию __dict__
        # Аттрибутов метакласса
        for key, value in self.class_attrs.items():
            self.__dict__[key] = value
    def __init__(cls, name, bases, attrs):
        cls.class_attrs = attrs
        cls.__init__ = Meta.create_local_attrs
class Women(metaclass=Meta):
    title = 'title'
    content = 'content'
    photo = 'photo'

w = Women()
print(w.__dict__)


# С помощью метакласса наш класс выглядит в коде вот так

""""
class Women:
    class_atrs = {'title': 'title', 'content': 'content', 'photo': 'photo'}
    title = 'title'
    content = 'content'
    photo = 'photo'

    def __init__(self, *args, **kwargs):
        for key, value in self.class_attrs.items():
            self.__dict__[key] = value
"""

# Таким образом метакласс упростил нам работу
# Но это тольуо в Django (и слава богу)
# И вообще метаклассы большинству нахер не нужны
# То есть я зря писал всё это. Это полный rofls!