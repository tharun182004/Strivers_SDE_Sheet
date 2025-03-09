matrix = [[1,2,3],[4,5,6],[7,8,9]]
col_len=len(matrix[0])
row_len=len(matrix)

def transporse():
    for i in range(row_len-1):
        for j in range(i+1,row_len):

            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    return matrix

def reverse(transporse):
    mat=transporse
    for row in transporse:
        rev=row.reverse()
    return mat

rev_mat=reverse(transporse())
for row in rev_mat:
    print(row)