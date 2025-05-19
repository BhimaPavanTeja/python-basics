
class CustomError(Exception):
    pass

def custom_exception_example():
    try:
        x = int(input("Enter positive number: "))
        if x <= 0:
            raise CustomError("Only positive numbers allowed.")
    except CustomError as e:
        print("Custom Error:", e)
    else:
        print("Valid input:", x)

custom_exception_example()
