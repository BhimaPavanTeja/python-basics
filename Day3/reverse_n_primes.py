n = int(input("Enter n: "))
count = 0
num = 2
primes = []
while count < n:
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        primes.append(num)
        count += 1
    num += 1
for p in reversed(primes):
    print(p, end=" ")