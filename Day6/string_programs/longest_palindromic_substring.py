def longestPalindrome(s: str) -> str:
    if not s:
        return ""
    start, end = 0, 0
    def palindrome_Check(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            print(f"Palindrome found: '{s[left:right+1]}'")
            left -= 1
            right += 1
        return right - left - 1
    for i in range(len(s)):
        print(f"\nCenter at index of {i}: '{s[i]}'")
        len1 = palindrome_Check(i, i)
        len2 = palindrome_Check(i, i + 1)
        max_len = max(len1, len2)
        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2
            print(f"Longest palindrome updated to: '{s[start:end+1]}'")
    print(f"\nFinal longest palindrome is: '{s[start:end+1]}'")
    return s[start:end + 1]

print("\nResult:", longestPalindrome("babd"))
