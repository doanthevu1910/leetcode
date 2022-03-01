import numpy as np

def average(salary):
    salary.remove(max(salary))
    salary.remove(min(salary))

    return np.mean(salary)

salary = [4, 3, 1, 2]

average(salary)

def hammingweight(n):
    c = 0
    while n:
        c += 1
        n &= n - 1

    return c

def subtractProductAndSum(n):
    sum = 0
    product = 1
    i = 0
    while i <= len(str(n))-1:
        sum = sum + int(str(n)[i])
        product = product * int(str(n)[i])
        i += 1

    return product - sum

subtractProductAndSum(234)

def largestPerimeter(nums):
    nums = sorted(nums, reverse=True)
    for i in range(2, len(nums)):
        if nums[i-2] < nums[i-1] + nums[i]:
            return nums[i-2] + nums[i-1] + nums[i]
        else:
            return 0
largestPerimeter([3, 6, 2, 3])


def nearestValidPoint(x, y, points):
    init_d = float('inf')
    ans = 1
    for i in range(len(points)):
        a, b = points[i]
        if a == x or b == y:
            d = abs(a - x) + abs(b - y)
            if d < init_d:
                init_d, ans = d, i
    return ans

def arraySign(nums):
    prod = np.product(nums)
    if prod < 0:
        return -1
    if prod == 0:
        return 0
    if prod > 0:
        return 1

arraySign([9,72,34,29,-49,-22,-77,-17,-66,-75,-44,-30,-24])

np.product([9,72,34,29,-49,-22,-77,-17,-66,-75,-44,-30,-24])

def arraySign(nums):
    sign = 1
    for num in nums:
      if num == 0:
        return 0
      if num < 0:
        sign = -sign

    return sign

