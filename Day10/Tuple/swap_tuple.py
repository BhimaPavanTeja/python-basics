def swap_tup(t):
    n = len(t)
    for i in range(n):
        a, b = t[i]
        if a > b:
            t[i] = (b, a)
        else:
            t[i] = (b, a)
    return t

t = [(1, 2), (3, 4)]
r = swap_tup(t)
print(r)
