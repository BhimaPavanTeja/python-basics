def maxWeightCell(N, Edge):
    temp = [0] * N

    for i in range(N):
        if Edge[i] != -1:
            temp[Edge[i]] += i

    ans = 0
    max_val = float('-inf')

    for i in range(N):
        if temp[i] >= max_val:
            ans = i
            max_val = temp[i]

    return ans

N = 4
Edge = [2, 0, -1, 2]
print(maxWeightCell(N, Edge))