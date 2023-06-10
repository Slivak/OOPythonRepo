class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):
        if 0 <= item < len(self.marks):
            return self.marks[item]
        else:
            raise IndexError('Out of range dude!')

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0:
            raise KeyError('Wrong key type dude!')

        if key > len(self.marks):
            off = key + 1 - len(self.marks)
            self.marks.extend([0]*off)

        self.marks[key] = value

    def __delitem__(self, key):
        if not isinstance(key, int) or key < 0:
            raise KeyError('Wrong key dude!')

        del self.marks[key]

s1 = Student('Лёха', [2, 2, 3, 2 , 2])

# __getitem__
print(s1[2])

# __setitem__
s1[99] = 2
print(s1[99])
print(s1.marks)

# __delitem__
del s1[99]
print(s1.marks)