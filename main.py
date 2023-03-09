def print_task():
    print("task")

def get_the_root(arrayp):
    a = int(input("введите число: "))
    b = int(input("Введите число: "))
    c = int(input("Введите число: "))
    d = b ** 2 - 4 * a * c
    dis = d ** 0.5
    print(dis)
    if d < 0:
        print("корня нет")
    elif d == 0:
        x = -b / (a * 2)
        print(f"число {x}= корень")
    elif d > 0:
        x1= (- b + dis) / (a * 2)
        print(f"число {x1} = 1 корень")
        x2 = (- b - dis) / (a * 2)
        print(f"число {x2}= 2 корень ")
    return(x, x1, x2)

def find_coordinates(*elems):
    x_min = int(input("Min. x:"))
    x_max = int(input("Max. x:"))
    a = int(input("a:"))
    b = int(input("b:"))
    c = int(input("c:"))
    for i in range(x_min, x_max + 1):
        y = a * (i) ** 2 + b * (i) + c
        print("Coordinates x =", i, ",y = ", y)
print(get_the_root)
print(find_coordinates)



