def firstBadVersion(n):
    left = 1
    right = n
    while right >= left:
        mid = (left + right) // 2
        if not isBadVersion(mid):
            left = mid + 1
        else:
            right = mid - 1

    return left

def searchInsert(nums, target):
    for i in range(len(nums)):
        if target > nums[i]:
            i+=1
        else:
            return i
    return i