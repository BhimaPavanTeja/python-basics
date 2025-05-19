
def try_except_else():
    try:
        n = int(input("Enter positive number: "))
        if n < 0:
            raise ValueError("Negative value!")
    except ValueError as e:
        print("Caught exception:", e)
    else:
        print("No exception, number is:", n)

try_except_else()
