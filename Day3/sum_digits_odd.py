n = int(input("Enter n: "))
total = 0
for i in range(1, n+1, 2):
    num = i
    sum_digits = 0
    while num > 0:
        sum_digits += num % 10
        num //= 10
    total += sum_digits
print(total)