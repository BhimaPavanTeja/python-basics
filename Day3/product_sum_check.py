n = int(input("Enter n: "))
count = 0
for i in range(1, n+1):
    num = i
    sum_d = 0
    prod_d = 1
    while num > 0:
        d = num % 10
        sum_d += d
        prod_d *= d
        num //= 10
    if sum_d != 0 and prod_d % sum_d == 0:
        count += 1
print(count)