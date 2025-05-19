
def exception_chaining():
    try:
        try:
            x = int("Sankar")
        except ValueError as ve:
            raise RuntimeError("Failed to convert string to int") from ve
    except RuntimeError as re:
        print("Runtime Error:", re)
        print("Original cause:", re.__cause__)

exception_chaining()
