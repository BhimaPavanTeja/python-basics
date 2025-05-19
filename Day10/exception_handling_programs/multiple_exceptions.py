def multiple_exceptions():
    try:
        lst = [1, 2, 3]
        idx = int(input("Enter index to access: "))
        print(lst[idx])
    except IndexError:
        print("Error: Index out of range.")
    except ValueError:
        print("Error: Invalid input, not a number.")

multiple_exceptions()
