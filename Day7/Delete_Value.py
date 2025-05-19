
arr = [1, 1, 2, 3, 5] + [0]*5
n = 5
index = 2

print("Before deletion:", arr[:n])
if 0 <= index < n:
    for i in range(index, n - 1):
        arr[i] = arr[i + 1]
    arr[n - 1] = 0
    n -= 1

print("After deletion:", arr[:n])
