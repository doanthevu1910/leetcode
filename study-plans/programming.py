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

def canMakeArithmeticProgression(arr):
    arr.sort()
    dif = arr[1] - arr[0]
    for i in range(len(arr) - 1):
        if arr[i + 1] - arr[i] != dif:
            return False
    return True

def isHappy(n):
    s = {n}
    while n != 1:
        tmp = sum([int(c) ** 2 for c in str(n)])
        if tmp in s:
            return False
        s.add(tmp)
        n = tmp
    return True

def areAlmostEqual(self, s1: str, s2: str) -> bool:
    if set(s1) != set(s2):
        return False
    mark = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            mark += 1
        if mark > 2:
            return False
    return True

def nextGreaterElement(nums1, nums2):
    result = []
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if nums1[i] == nums2[j]:
                if j == len(nums2):
                    result.append(-1)
                elif nums2[j] < nums2[j+1]:
                    result.append(nums2[j+1])
    return result

nums1 = [4,1,2]
nums2 = [1,3,4,2]

nextGreaterElement(nums1, nums2)

def checkStraightLine(coordinates):

    for i in range(len(coordinates)):
        a = coordinates[i]
        b = coordinates[i+1]
        c = coordinates[i+2]
        if (b[1]-a[1])/(b[0]-a[0]) == (c[1]-b[1])/(c[0]-b[0]):
            return True
        else:
            return False

coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]

checkStraightLine(coordinates)

arr = [1,4,2,5,3]

arr[0:3]
arr[1:4]
arr[2:5]

sub = []
i = 0
while i <= len(arr) // 2:
    length = 2*i + 1
    j = 0

    while j <= len(arr) - 2:
        sub.append(arr[j:(j+length)])
        j += 1

    i +=1

sub

def sumOddLengthSubarrays(arr):
    total = 0
    for i in range(1, len(arr) + 1, 2):
        for k in range(len(arr)):
            if k + i > len(arr):
                break
            else:
                total += sum(arr[k:k + i])

    return total

accounts = [[1,2,3],[3,2,1]]

def maximumWealth(accounts):
    return max(sum(accounts[i]) for i in range(len(accounts)))

# day 7
mat = [[1,2,3], [4,5,6], [7,8,9]]

def diagonalSum(mat):
    i = 0
    sum1 = 0
    while i <= len(mat)-1:
        sum1 += mat[i][i] + list(reversed(mat[i]))[i]
        i += 1

    if len(mat) % 2 == 1:
        center = len(mat) // 2
        return sum1 - mat[center][center]
    else:
        return sum1

mat = [[1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1]]
diagonalSum(mat)

