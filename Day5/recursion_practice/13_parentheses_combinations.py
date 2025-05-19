
def generate_parentheses(n: int, left: int = 0, right: int = 0, s: str = '') -> list:
    if left == n and right == n:
        return [s]
    result = []
    if left < n:
        result += generate_parentheses(n, left + 1, right, s + '(')
    if right < left:
        result += generate_parentheses(n, left, right + 1, s + ')')
    return result

print(generate_parentheses(2))  # Output: ['(())', '()()']
