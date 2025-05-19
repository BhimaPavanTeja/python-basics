# 1. Swap Two Numbers Without Using a Third Variable
def swap_numbers(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

# 2. Check if a Number is Power of Two Without Using Loops or Recursion
def is_power_of_two(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0

# 3. Multiply Two Numbers Without Using *, /, or %
def multiply(x, y):
    result = 0
    positive = y > 0
    y = y if positive else -y
    for _ in range(y):
        result += x
    return result if positive else -result

# 4. Reverse a Number Without Using Strings or Arrays
def reverse_number(n):
    rev = 0
    negative = n < 0
    n = -n if negative else n
    while n > 0:
        rev = rev * 10 + n % 10
        n = n // 10
    return -rev if negative else rev

# 5. Find the Nth Digit in a Continuous Sequence: 123456789101112...
def nth_digit(n):
    digit_length = 1
    count = 9
    start = 1
    while n > digit_length * count:
        n -= digit_length * count
        digit_length += 1
        count *= 10
        start *= 10
    num = start + (n - 1) // digit_length
    digit_index = (n - 1) % digit_length
    for _ in range(digit_length - digit_index - 1):
        num = num // 10
    return num % 10

# 6. Count Total Set Bits in an Integer Without Built-in Functions
def count_set_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

# 7. Find GCD Using Recursion Only
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

# 8. Print All Armstrong Numbers Between 1 to 1000
def is_armstrong(n):
    original = n
    result = 0
    digits = 0
    temp = n
    while temp > 0:
        digits += 1
        temp = temp // 10
    temp = n
    while temp > 0:
        digit = temp % 10
        power = 1
        for _ in range(digits):
            power *= digit
        result += power
        temp = temp // 10
    return result == original

def armstrong_numbers():
    result = []
    for i in range(1, 1001):
        if is_armstrong(i):
            result.append(i)
    return result

# 9. Check If a Number is a Palindrome Without Using Extra Space
def is_palindrome_number(n):
    if n < 0:
        return False
    original = n
    reversed_num = 0
    while n > 0:
        reversed_num = reversed_num * 10 + n % 10
        n //= 10
    return original == reversed_num

# 10. Convert Decimal to Binary as String Without Using Built-ins
def decimal_to_binary(n):
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        binary = chr((n % 2) + ord('0')) + binary
        n = n // 2
    return binary
