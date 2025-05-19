
def using_assert():
    try:
        x = int(input("Enter non-zero number: "))
        assert x != 0, "Zero is not allowed."
    except AssertionError as ae:
        print("Assertion Error:", ae)
    else:
        print("Good input:", x)

using_assert()
