num = 456
s = 0
while num:
    s += num % 10
    num //= 10
print("Sum of digits:", s)