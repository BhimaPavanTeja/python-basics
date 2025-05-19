
def raise_exception():
    def validate_age(age):
        if age < 18:
            raise Exception("Age must be at least 18.")
        return True

    try:
        age = int(input("Enter your age: "))
        validate_age(age)
    except Exception as e:
        print("Validation Error:", e)
    else:
        print("Age is valid.")

raise_exception()
