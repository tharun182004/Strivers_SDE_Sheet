arr=[-2,-3,4,-1,-2,1,5,-3]

max=float('-inf')
sum=0

for i in range(len(arr)):
    if sum==0:
        start=i
    sum+=arr[i]

    if sum>max:
        max=sum
        end=i

    if sum<0:
        sum=0

for j in range(start,end+1):
    print(arr[j])
