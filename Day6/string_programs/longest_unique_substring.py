input_str = "abcabcbbcccc"
def longest_len(input_str):
    longest = ""
    for i in range(len(input_str)):
        current = ""
        for j in range(i, len(input_str)):
            if input_str[j] not in current:
                current += input_str[j] 
            else:
                break
        if len(current) > len(longest):
            longest = current
    return longest
print(longest_len(input_str))
