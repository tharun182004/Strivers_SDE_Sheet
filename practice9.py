arr1=[1, 4, 5, 7]
arr2=[2, 3, 6]
n=len(arr1)
m=len(arr2)
left=n-1
right=0
while (left>=0 and right<m):
    if arr1[left]>arr2[right]:
        arr1[left],arr2[right]=arr2[right],arr1[left]
        left-=1
        right+=1
    else:
        break
arr1.sort()
arr2.sort()

print(arr1,arr2)