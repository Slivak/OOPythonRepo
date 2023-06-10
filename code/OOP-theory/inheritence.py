class Geom:
    name = 'Geom'

    def set_coord(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

class Line(Geom):
    def draw(self):
        print('Рисование линии')


class Rect(Geom):
    def draw(self):
        print('Рисование прямоугольника')

g = Geom()
l = Line()
r = Rect()
l.set_coord(1, 1, 2, 2)
r.set_coord(1, 1, 2, 2)

print(l.name)