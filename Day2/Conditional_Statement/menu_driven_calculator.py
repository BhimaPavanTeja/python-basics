choice = 1
x, y = 20, 4
if choice == 1:
    print(x + y)
elif choice == 2:
    print(x - y)
elif choice == 3:
    print(x * y)
elif choice == 4:
    print(x / y if y != 0 else "Division by zero")
else:
    print("Invalid Choice")