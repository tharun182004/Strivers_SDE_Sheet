from typing import *


def numberOfInversions(a: List[int], n: int) -> int:
    # Write your code here.
    low = 0
    high = n - 1

    def merge_sort(a, low, high):

        if low >= high:
            return 0

        mid = (low + high) // 2
        left_count = merge_sort(a, low, mid)
        right_count = merge_sort(a, mid + 1, high)

        merge_count = merge(a, low, mid, high)

        return merge_count

    def merge(a, low, mid, high):
        temp = []
        left = low
        right = mid + 1
        count = 0

        while left <= mid and right <= high:
            if a[left] <= a[right]:
                temp.append(a[left])
                left += 1
            else:
                temp.append(a[right])
                right += 1
                count += (mid - left + 1)

        while left <= mid:
            temp.append(a[left])
            left += 1

        while right <= high:
            temp.append(a[right])
            right += 1

        for i in range(len(temp)):
            a[low + i] = temp[i]

        return count

    return merge_sort(a, low, high)



