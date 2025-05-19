
def try_except_finally():
    try:
        f = open("non_existent_file.txt")
        print(f.read())
    except FileNotFoundError:
        print("File not found.")
    finally:
        print("Execution completed, closing file if open.")

try_except_finally()
