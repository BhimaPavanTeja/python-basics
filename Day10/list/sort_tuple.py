def sort_tup(t):
    n = len(t)
    for i in range(n):
        for j in range(0, n - i - 1):
            if t[j][1] > t[j + 1][1]:
                temp = t[j]
                t[j] = t[j + 1]
                t[j + 1] = temp
        print(*t)
    return t

t = [(1, 2), (3, 1), (5, 0)]
r = sort_tup(t)
print(r)
