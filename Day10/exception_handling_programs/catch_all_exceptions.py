
def catch_all_exceptions():
    try:
        x = 10 / 0
    except Exception as e:
        print("Caught an exception:", e)

catch_all_exceptions()
