
arr = [4, 5, 3, 4, 5, 6, 7, 1, 20]
max_length = 0

for i in range(len(arr) - 1):
    temp_length = 1
    for j in range(i + 1, len(arr)):
        if arr[j - 1] < arr[j]:
            temp_length += 1
        else:
            if temp_length > max_length:
                max_length = temp_length
            break

print("Length of longest increasing subarray:", max_length)
