a = int(input("введите число: "))
b = int(input("Введите число: "))
c = int(input("Введите число: "))
d = b**2-4*a*c
dis = d**0.5
print (dis)
if d<0:
    print("корня нет")
elif d == 0:
    x = -b / (a * 2)
    print(f"число {x}= корень")
elif d>0:
    x1 = - b + dis / a * 2
    print(f"число {x1} = 1 корень")
    x2 = - b - dis / a * 2
    print(f"число {x2}= 2 корень ")



