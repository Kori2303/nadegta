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
 #5.1 I   
    
    class Queue: 
    def __init__(self): 
        self.items = [] 
         
    def push(self, item): 
        self.items.append(item) 
         
    def pop(self): 
        return self.items.pop(0) 
     
    def is_empty(self): 
        return len(self.items) == 0

 #5.2 A

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move (self, dx, dy):
        self.x += dx
        self.y += dy

    def length(self, point):
        distance = ((self.x - point.x)** 2 + (self.y - point.y)**2) **0.5
        return round(distance, 2)

class PatchedPoint(Point):
    def __init__(self, *args):
        if len(args) == 0:
            super().__init__(0, 0)
        elif len(args) == 1:
            super().__init__(args[0][0], args[0][1])
        elif len(args) == 2:
            super().__init__(*args)
            
#5.1 J

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0
    
#5.2 b

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move (self, dx, dy):
        self.x += dx
        self.y += dy

    def length(self, point):
        distance = ((self.x - point.x)** 2 + (self.y - point.y)**2)
        return round(distance, 2)

class PatchedPoint(Point):
    def __init__(self, *args):
        if len(args) == 0:
            super().__init__(0, 0)
        elif len(args) == 1:
            super().__init__(args[0][0], args[0][1])
        elif len(args) == 2:
            super().__init__(*args)

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'PatchedPoint({self.x}, {self.y})'
    
#5.2 F

class Fraction:
    def __init__(self, numerator, denominator=1):
        if type(numerator) == str:
            numerator, denominator = map(int, numerator.split('/'))
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator
        gcd = self._gcd(abs(numerator), abs(denominator))
        self._numerator = numerator // gcd
        self._denominator = denominator // gcd

    def _gcd(self, a, b):
        if b == 0:
            return a
        return self._gcd(b, a % b)

    def numerator(self, number=None):
        if number is None:
            return self._numerator
        if number < 0:
            self._numerator = -abs(number)
        else:
            self._numerator = abs(number)
        gcd = self._gcd(self._numerator, self._denominator)
        self._numerator = self._numerator // gcd
        self._denominator = self._denominator // gcd
        return self._numerator

    def denominator(self, number=None):
        if number is None:
            return self._denominator
        if number == 0:
            raise ValueError("Denominator can't be equal to zero.")
        if number < 0:
            self._denominator = -abs(number)
        else:
            self._denominator = abs(number)
        gcd = self._gcd(self._numerator, self._denominator)
        self._numerator = self._numerator // gcd
        self._denominator = self._denominator // gcd
        return self._denominator

    def __str__(self):
        if self._denominator == 1:
            return f"{self._numerator}"
        else:
            return f"{self._numerator}/{self._denominator}"

    def __repr__(self):
        return f"Fraction({self._numerator}, {self._denominator})"

    def __neg__(self):
        return Fraction(-self._numerator, self._denominator)

    def __add__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        elif not isinstance(other, Fraction):
            raise TypeError("Unsupported operand type(s) for +: 'Fraction' and '{}'".format(type(other).__name__))
        new_numerator = self._numerator * other._denominator + self._denominator * other._numerator
        new_denominator = self._denominator * other._denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        elif not isinstance(other, Fraction):
            raise TypeError("Unsupported operand type(s) for -: 'Fraction' and '{}'".format(type(other).__name__))
        new_numerator = self._numerator * other._denominator - self._denominator * other._numerator
        new_denominator = self._denominator * other._denominator
        return Fraction(new_numerator, new_denominator)

    def __iadd__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        elif not isinstance(other, Fraction):
            raise TypeError("Unsupported operand type(s) for +=: 'Fraction' and '{}'".format(type(other).__name__))
        new_numerator = self._numerator * other._denominator + self._denominator * other._numerator
        new_denominator = self._denominator * other._denominator
        gcd = self._gcd(abs(new_numerator), abs(new_denominator))
        self._numerator = new_numerator // gcd
        self._denominator = new_denominator // gcd
        return self

    def __isub__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        elif not isinstance(other, Fraction):
            raise TypeError("Unsupported operand type(s) for -=: 'Fraction' and '{}'".format(type(other).__name__))
        new_numerator = self._numerator * other._denominator - self._denominator * other._numerator
        new_denominator = self._denominator * other._denominator
        gcd = self._gcd(abs(new_numerator), abs(new_denominator))
        self._numerator = new_numerator // gcd
        self._denominator = new_denominator // gcd
        return self
