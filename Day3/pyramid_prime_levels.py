n = int(input("Enter number of levels: "))
primes = []
num = 2
while len(primes) < n*(n+1)//2:
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        primes.append(num)
    num += 1

index = 0
for i in range(1, n+1):
    for j in range(i):
        print(primes[index], end=" ")
        index += 1
    print()