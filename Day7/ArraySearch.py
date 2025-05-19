
array = [3, 5, 7, 9, 11]
target = int(input("Enter the element to search: "))
found = False

for num in array:
    if num == target:
        found = True
        break

print("Element found:", found)
