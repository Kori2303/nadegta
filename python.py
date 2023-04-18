#5.1 A
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


#5.1 B
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

    def length(self, point):
        d = ((self.x - point.x)**2 + (self.y - point.y)**2)**0.5
        return round(d, 2)

#5.1 C
class RedButton:
    def __init__(self):
        self.c = 0

    def click(self):
        self.c += 1
        print("Тревога!")

    def count(self):
        return self.c

#5.1 D
class Posit:
    Junior = 10
    Middle = 15
    Senior = 20


class Programmer:
    def __init__(self, name, Posit):
        self.name = name
        self.Posit = Posit
        self.sal = Posit.val
        self.money = 0
        self.working = 0

    def work(self, time):
        self.working += time
        self.money += time * self.sal

    def rise(self, Junior, Middle, Senior):
        if self.position == Posit.Junior:
            self.position = Posit.Middle
            self.sal = Posit.Middle.val
        elif self.position == Posit.Middle:
            self.position = Posit.Senior
            self.sal = Posit.Senior.val
        else:
            self.sal += 1

    def info(self):
        return '{} {}ч. {}тгр.'.format(
            self.name,
            self.working,
            self.money)

    def main():
        programmer = Programmer()
        programmer.work(100)
        print(programmer.info())
        programmer.rise()
        programmer.work(100)
        print(programmer.info())
        programmer.rise()
        programmer.work(100)
        print(programmer.info())
        programmer.rise()
        programmer.work(100)
        print(programmer.info())

    print(main())


#5.1 E
    class Rectangle:
        def __init__(self, p1, p2):
            self.x1, self.y1 = p1
            self.x2, self.y2 = p2

        def perimeter(self):
            a = abs(self.x1 - self.x2)
            b = abs(self.y1 - self.y2)
            return round(2 * (a + b), 2)

        def area(self):
            a = abs(self.x1 - self.x2)
            b = abs(self.y1 - self.y2)
            return round(a * b, 2)

#5.2 D

class Rectangle:
    def __init__(self, p1, p2):
        self.x1, self.y1 = p1
        self.x2, self.y2 = p2

    def perimeter(self):
        a = abs(self.x1 - self.x2)
        b = abs(self.y1 - self.y2)
        return round(2 * (a + b), 2)

    def area(self):
        a = abs(self.x1 - self.x2)
        b = abs(self.y1 - self.y2)
        return round(a * b, 2)