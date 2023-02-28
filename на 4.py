x_min = int(input("Min. x:"))
#вводим минимальный х
x_max = int(input("Max. x:"))
#вводим максимальный х
a = int(input("a:")) #вводим а
b = int(input("b:")) #вводим b
c = int(input("c:")) #вводим с
for i in range (x_min, x_max + 1):
    y = a*(i) **2 + b*(i) + c
    #I кол-во повторений
    print("Coordinates x =", i, ",y = ", y)
    #координаты х, у


