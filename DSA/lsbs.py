n = int(input())
arr = list(map(int, input().split()))
no = int(input())

# Linear Search
found = False
for i in range(n):
    if arr[i] == no:
        found = True
        print("index: ", i)
        break

# Binary Search
l = 0
r = n - 1
found = False
while l <= r:
    mid = (l+r) //2
    if arr[mid] == no:
        found = True
        print("index: ", mid)
        break
    elif arr[mid] < no:
        l = mid + 1
    else:
        r = mid - 1
if not found:
    print("Not Found")