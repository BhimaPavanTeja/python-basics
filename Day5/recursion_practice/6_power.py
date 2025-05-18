
def power(a: int, b: int) -> int:
    if b == 0:
        return 1
    return a * power(a, b - 1)
print(power(2, 3))  
