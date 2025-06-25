n = int(input())
arr = [5 * i for i in range(1,n+1)]
no = int(input())

print("Array: ", arr)

l = 0
r = n - 1
count = 0
found = False
while l <= r:
    count += 1
    mid = (l + r) // 2
    if arr[mid] == no:
        found = True
        break
    elif arr[mid] < no:
        l = mid + 1
    else:
        r = mid - 1
if found:
    print("index: ", mid)
else:
    print("Not Found")
    
print("search count:", count)