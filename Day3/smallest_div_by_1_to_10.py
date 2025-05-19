import math
def lcm(x, y):
    return x * y // math.gcd(x, y)

n = int(input("Enter n: "))
i = n + 1
lcm_10 = 1
for i in range(1, 11):
    lcm_10 = lcm(lcm_10, i)
while True:
    if i % lcm_10 == 0:
        print(i)
        break
    i += 1