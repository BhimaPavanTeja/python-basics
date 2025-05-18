def tail_recursion(n, result=1):
    if n == 0:
        print(f'Tail Recursion Result: {result}')
        return
    tail_recursion(n - 1, result * n)
print(tail_recursion(5))


def head_recursion(n):
    if n == 0:
        return n
    print(head_recursion(n-1))
    print(f'Head Recursion: {n}')
print(head_recursion(5))

def tree_recursion(n):
    if n == 0:
        return n
    elif n==1:
        return n
    return tree_recursion(n - 1) + tree_recursion(n - 2)
print(tree_recursion(6))


def indirect_recursion_a(n):
    if n <= 0:
        return
    print(f'Indirect Recursion A: {n}')
    indirect_recursion_b(n - 1)
def indirect_recursion_b(n):
    if n <= 0:
        return
    print(f'Indirect Recursion B: {n}')
    indirect_recursion_a(n - 2)
print(indirect_recursion_a(5))

def nested_recursion(n):
    if n > 100:
        return n - 10
    return nested_recursion(nested_recursion(n + 11))
print(nested_recursion(95))