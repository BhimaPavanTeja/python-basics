
array = [1, 2, 3, 4, 5, 6]
even_count = 0
odd_count = 0

for num in array:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even Count:", even_count)
print("Odd Count:", odd_count)
