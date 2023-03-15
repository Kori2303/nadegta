a = int(input("введите начало диапозона: "))
b = int(input('введите конец диапозона: '))
for p in range(a, b+1):
    if p > 1:
        break
for i in range(2, p):
    if (p % i) == 0:
        break
    else:
        print(p)
