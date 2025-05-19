def Strip_Function():
    Sample = "   Sankar "
    start = 0
    end = len(Sample) - 1
    while start <= end and (Sample[start] == ' ' or Sample[end] == ' '):
        if Sample[start] == ' ':
            start += 1
        if Sample[end] == ' ':
            end -= 1
    if start <= end:
        result = ""
        for i in range(start, end + 1):
            result += Sample[i]
    else:
        result = ""
    return result
print(Strip_Function())
