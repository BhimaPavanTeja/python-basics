def count_substrings(s):
    count = 0
    palindromes = []
    for i in range(len(s)):
        l = r = i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            palindromes.append(s[l:r+1])
            count += 1
            l -= 1
            r += 1

        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            palindromes.append(s[l:r+1])
            count += 1
            l -= 1
            r += 1

    print("All palindromic substrings:", palindromes)
    return count
print("Count:", count_substrings("aaa"))
