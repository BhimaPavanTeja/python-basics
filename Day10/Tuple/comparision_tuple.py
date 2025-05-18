def cmp_tup(t1, t2):
    a = (min(t1[0], t2[0]), min(t1[1], t2[1]))
    b = (max(t1[0], t2[0]), max(t1[1], t2[1]))
    return a, b
t1 = (1, 5)
t2 = (3, 4)
r1, r2 = cmp_tup(t1, t2)
print(r1, r2)
