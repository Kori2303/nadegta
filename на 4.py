a = int(input("ведите число: "))
b = int(input("ведите число: "))
c = int(input("ведите число: "))
d = b**2-4*a*c
dis = d**0.5
print (dis)
if d<0:
    print("корня нет")
elif d == 0:
    x = -b / (a * 2)
    print (f"число {x}= x ")
    y = a * x ** 2 + b * x + c
    print(f"число {y}= y ")
elif d>0:
    x1 = - b + dis / a * 2
    print(f"число {x1}= x1 ")
    x2 = - b - dis / a * 2
    print(f"число {x2}= x2 ")
    y1 = a * x1 ** 2 + b * x1 + c
    print(f"число {y1}= y1 ")
    y2 = a * x2 ** 2 + b * x2 + c
    print(f"число {y2}= y2 ")

