n = 17
if n <= 1:
    print("Neither")
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print("Composite")
            break
    else:
        print("Prime")