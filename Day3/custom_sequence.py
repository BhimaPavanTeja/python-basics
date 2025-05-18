n = int(input("Enter n: "))
seq = [2]
for i in range(1, n):
    seq.append(seq[-1] + 2**i)
print(seq)