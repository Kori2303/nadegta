def bubble (a):
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i]<a[j]:
                a[i], a[j] = a[j], a[i]
    return a
print(bubble([5, 10, 1, 3]))

def quick(a, l, r):
    if len(a) < 2:
        return a
    m = a[0]
    l_a = []
    r_a = []
    for i in range(l, r):
        if m > a[i]:
            l.append(a[i])
        elif m != a[i]:
            r.append(a[i])

    res_l=quick (l_a, 0, len(l_a))
    res_r=quick (r_a, 0, len(r_a))
    res_l.append(m)
    res_l.extend(res_r)
    return res_l
print(quick([5, 10, 1, 3], 0, 4))
