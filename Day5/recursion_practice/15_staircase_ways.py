
def ways_to_climb(n: int) -> int:
    if n < 0:
        return 0
    if n == 0:
        return 1
    return ways_to_climb(n - 1) + ways_to_climb(n - 2) + ways_to_climb(n - 3)

print(ways_to_climb(4)) 
