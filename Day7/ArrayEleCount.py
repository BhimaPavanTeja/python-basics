
array = [1, 2, 2, 3, 3, 3, 4]
visited = [0] * len(array)
flag= -1

print("Occurrences:")
for i in range(len(array)):
    if visited[i] == flag:
        continue
    count = 1
    for j in range(i + 1, len(array)):
        if array[i] == array[j]:
            count += 1
            visited[j] = flag
    print(f"{array[i]} -->  {count}")








"""array = [1, 2, 2, 3, 3, 3, 4]

print("Occurrences:")
for i in range(len(array)):
    is_counted = False
    for k in range(i):
        if array[i] == array[k]:
            is_counted = True
            break
    if is_counted:
        continue

    count = 1
    for j in range(i + 1, len(array)):
        if array[i] == array[j]:
            count += 1

    print(f"{array[i]} --> {count}")
"""