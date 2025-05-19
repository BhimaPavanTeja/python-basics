def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        rotated = s1[i:] + s1[:i]
        if rotated == s2:
            return True
    return False

print(is_rotation("abcd", "cdab"))
