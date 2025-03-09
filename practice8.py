#arr=[[1,3],[2,4],[3,5],[6,7]]
#arr=[[1,2],[1,3],[1,6],[3,4],[4,4],[5,5],[6,6],[6,6]]
arr=[[2,2],[2,3],[2,5],[3,6],[4,4],[4,5],[6,6]]
n=len(arr)
i=0
while i<n-1:
    if arr[i][0]<=arr[i+1][0] and arr[i+1][0]<=arr[i][1]:
        if arr[i][1]<=arr[i+1][1]:
            max=arr[i+1][1]
            arr[i][1]=max
            del arr[i+1]
            n=len(arr)
        else:
            del arr[i+1]
            n=len(arr)
    else:
        i+=1
        n=len(arr)

print(arr)