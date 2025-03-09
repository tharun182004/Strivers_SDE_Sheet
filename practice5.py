nums=[2,0,2,1,1,0]
n=len(nums)
for i in range(n-1):
    for j in range(i+1,n):
        if nums[i]>nums[j]:
            nums[i],nums[j]=nums[j],nums[i]
        elif nums[i]==nums[j]:
            nums[i+1],nums[j]=nums[j],nums[i+1]
        continue
print(nums)