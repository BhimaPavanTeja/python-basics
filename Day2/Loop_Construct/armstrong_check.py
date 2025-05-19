num = 1634
tot = 0
length=len(str(num))
for digit in str(num):
    tot += int(digit) ** length
print("Armstrong" if tot == num else "Not Armstrong")


