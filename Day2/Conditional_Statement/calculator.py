a, b, op = 10, 5, '*'
if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    print(a / b if b != 0 else "Division by zero")
else:
    print("Invalid operation")