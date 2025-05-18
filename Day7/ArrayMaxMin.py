
array = [10, 20, 5, 8, 25, 3]
max_val = array[0]
min_val = array[0]

for num in array:
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num

print("Maximum:", max_val)
print("Minimum:", min_val)
