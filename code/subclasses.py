class Women:
    title = 'title'
    photo = 'photo'
    ordering = 'ordering'

    def __init__(self, user, psw):
        self._user = user
        self._psw = psw
        # Передаём аргумент(access) в класс Meta
        self.meta = self.Meta(user + '@' + psw)

    # Во вложенном классе своё пространство имён
    class Meta:
        ordering = ['id']

        # Но мы не можем обращаться к основному классу, т.к он не создан
        # Women.title (NameError: name 'Women' is not defined.)
        def __init__(self, access):
            self._access = access

w = Women('root', '1234')
print(w.ordering)
print(w.Meta.ordering)

# Не одно и тоже!
print(w.__dict__) # свойства экза
print(Women.__dict__) # Свойства класса


print(w.meta.__dict__)

# Логику надо прописывать так, что бы
# Внутренний класс не юзал вложенный
# А ровно наооборот