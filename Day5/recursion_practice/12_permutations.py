
def permutations(s: str) -> list:
    if len(s) == 1:
        return [s]
    perm_list = []
    for i, char in enumerate(s):
        for perm in permutations(s[:i] + s[i+1:]):
            perm_list.append(char + perm)
    return perm_list

print(permutations("abc"))  # Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
