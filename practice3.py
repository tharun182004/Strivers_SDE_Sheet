nums=[3,2,1]

n = len(nums)
ind = -1
for i in range(n - 1, 0, -1):
    if nums[i] > nums[i - 1]:
        ind = i - 1
        break

if ind == -1:
    nums = nums[::-1]
    print("nums", nums)
else:
    print("else part")
    for i in range(n - 1, ind, -1):
        print(i)
        if nums[ind] < nums[i]:
            nums[ind], nums[i] = nums[i], nums[ind]
            nums = nums

            break
        else:
            continue
    # ind=1, n=6
    ind = ind + 1
    n = n - 1
    while ind < n:
        nums[ind], nums[n] = nums[n], nums[ind]
        ind += 1
        n -= 1
    print(nums)
