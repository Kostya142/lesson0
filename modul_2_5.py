def  get_matrix (n,m, value):
    matrix = [[None] * n]*m
    for j in range(m):
        for i in range(n):
            matrix[j][i]=value
    return matrix

print(get_matrix(2,3,40))













