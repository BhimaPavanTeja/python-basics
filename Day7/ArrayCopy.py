
source = [2, 4, 6, 8]
destination = [0] * len(source)

for i in range(len(source)):
    destination[i] = source[i]

print("Copied Array:", destination)
