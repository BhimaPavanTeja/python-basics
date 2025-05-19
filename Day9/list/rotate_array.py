matrix = [[1,2,3],[4,5,6],[7,8,9]]
def rotate_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i+1, n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
    print("After transpose : ",matrix)
    for i in range(n):
        start = 0
        end = n - 1
        while start < end:
            temp = matrix[i][start]
            matrix[i][start] = matrix[i][end]
            matrix[i][end] = temp
            start += 1
            end -= 1
    print("after reverse part: ",end=" ")
    return matrix

rotate_matrix(matrix)
print(matrix)
