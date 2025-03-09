mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
#       0, 1, 2, 3,   4, 5, 6, 7,   8, 9,  10, 11
row_len=len(mat)
col_len=len(mat[0])

n=row_len*col_len
low,high=0,n

target=10

while low<=high:
    mid=(low+high)//2
    row=mid//col_len
    col=mid%col_len

    if mat[row][col]==target:
        print(True)
        #print(f"row is {row},col is {col}")
        break
    elif target<=mat[row][col]:
        high=mid-1
    else:
        low+=1

else:
    print("Target not found")


