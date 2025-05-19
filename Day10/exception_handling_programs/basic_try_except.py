
def basic_try_except():
    try:
        x = int(input("Enter a number: "))
        print(100 / x)
    except ZeroDivisionError:
        print("Error: Division by zero not allowed.")
    except ValueError:
        print("Error: Invalid input, not a number.")
basic_try_except()
