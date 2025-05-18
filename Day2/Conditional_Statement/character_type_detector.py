# Read a single character input
char = input().strip()

# Check and classify the character
if 'A' <= char <= 'Z':
    print("Upper")
elif 'a' <= char <= 'z':
    print("Lower")
elif '0' <= char <= '9':
    print("Number")
else:
    print("Symbol")
