n = 5
mat = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(0)
    mat.append(row)
for row in mat:
    for col in row:
        print(col,end=" ")
    print()
    
    
     
val = 1
top=0
bottom=n-1
left=0
right = n-1
while val <= n*n:
    for i in range(left, right+1):
        mat[top][i] = val
        val += 1
    top += 1
    for i in range(top, bottom+1):
        mat[i][right] = val
        val += 1
    right -= 1
    for i in range(right, left-1, -1):
        mat[bottom][i] = val
        val += 1
    bottom -= 1
    for i in range(bottom, top-1, -1):
        mat[i][left] = val
        val += 1
    left += 1
for row in mat:
    for col in row:
        print(col,end=" ")
    print()