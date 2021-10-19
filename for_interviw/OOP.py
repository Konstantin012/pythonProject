#https://younglinux.info/oopython/inheritance
#1------------------------------------------------------------------------------------
class Table:
    def __init__(self, l, w, h):
        self.length = l
        self.width = w
        self.height = h


class DeskTable(Table):
    def square(self):
        return self.width * self.length

t1 = Table(1.5, 1.8, 0.75)
t2 = DeskTable(1, 2, 3)
# print(t2.square())

#2------------------------------------------------------------------------------------
class Table:
    def __init__(self, l, w, h):
        self.length = l
        self.width = w
        self.height = h
        print(str(int(self.length) + int(self.width) + int(self.height)))



class KitchenTable(Table):
    def __init__(self, l, w, h, p):
        Table.__init__(self, l, w, h)
        self.places = p
        print(str(int(self.length) + int(self.width) + int(self.height) + int(self.places)))


t4 = KitchenTable(1, 2, 3, 4)

#3------------------------------------------------------------------------------------
class KitchenTable(Table):
    def __init__(self, l, w, h, p):
        super().__init__(l, w, h)
        self.places = p

