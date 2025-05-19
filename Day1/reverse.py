n = int(input("Enter a number: "))
reversed_num = 0

while n > 0:
    digit = n % 10
    reversed_num = reversed_num * 10 + digit
    n //= 10

print("Reversed number is: ",reversed_num)
