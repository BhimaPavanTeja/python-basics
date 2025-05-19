def anagrams(str1, str2):
    a = str1.lower()
    b = str2.lower()
    if len(a) != len(b):
        return False
    count = [0] * 26
    for i in range(len(a)):
        count[ord(a[i]) - ord('a')] += 1
        count[ord(b[i]) - ord('a')] -= 1
    print(count, end=" ") 
    for i in count:
        if i != 0:
            return False
    return True
print(anagrams("sileN", "sileN"))
