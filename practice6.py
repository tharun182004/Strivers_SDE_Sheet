nums=[7,1,5,3,6,4]

n = len(nums)
mini = nums[0]
max_profit = 0
for i in range(1, n):
    profit = nums[i] - mini
    if profit > max_profit:
        max_profit = profit
    mini = min(nums[i], mini)

print(max_profit)

'''
THIS BRUTE FORCE METHOD EXCEEDS TIME LIMIT

n=len(nums)
max_profit=0
for i in range(n-1):
    for j in range(i+1,n):
        if nums[j]>nums[i]:
            profit=nums[j]-nums[i]
            if profit>max_profit:
                max_profit=profit
        else:
            continue
print(max_profit)'''

