import math


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

num = [1, 2, 3]

def sortedSquares(nums):
    result = []
    for i in range(len(nums)):
        result.append(nums[i]**2)
    return sorted(result)

sortedSquares([-4,-1,0,3,10])

num = [-4,-1,0,3,10]

# a = num[-3:]
#
# num = a + num[0:2]

def rotate(nums, k):
    for i in range(k):
        nums.insert(0, nums[-1])
        nums.pop()

prices = [7,1,5,3,6,4]

def maxProfit(prices):
    test = []

    for i in range(len(prices)):
        last = prices[-i]
        for j in range(i):
            test.append(last - prices[j])

    return max(test)

maxProfit(prices)


def moveZeroes(nums):
    for i in range(len(nums)):
        x = nums[i]
        if x == 0:
            nums.insert(len(nums), x)
            nums.pop(i)

nums = [0,0,1]
moveZeroes(nums)
nums

def reverseString(s):
    for i in range(len(s)):
        s.insert(0, s[-1])
        s.pop()

s = ["h","e","l","l","o"]
a = reverseString(s)

s = "Let's take LeetCode contest"

def reverseWords(s):
    split = s.split(' ')
    words = []
    for i in range(len(split)):
        words.append(split[i][::-1])

    return ' '.join(words)

reverseWords(s)

mat = [[1,2],[3,4]]

import numpy as np

def matrixReshape(mat, r, c):
    if len(mat)*len(mat[0]) != r*c:
        return mat
    else:
        return np.reshape(mat, (r, c))

matrixReshape(mat, 1, 4)

def generate(numRows):
    pt = []
    for row_num in range(numRows):
        row = [1] * (row_num + 1)
        for index in range(1, len(row) - 1):
            row[index] = pt[row_num - 1][index - 1] + pt[row_num - 1][index]
        pt.append(row)
    return pt

generate(5)

n = [1, 2, 3, 4, 5, 6]


def middleNode(head):
    return n[len(n) // 2]

# day 6

s = "abcabcbb"

list(s)

# def lengthOfLongestSubstring(s):
#     result = []
#
#     for i in list(s):
#         if i not in result:
#             result.append(i)
#
#     return len(result)

s = "pwwkew"

all_sub = [s[i: j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]

all_sub.remove(s)

all_sub

sub1 = all_sub[0]

def lengthOfLongestSubstring(s):
    all_sub = [s[i: j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]

    all_sub = all_sub.remove(s)

    def count_unique(a):
        result = []
        for i in list(a):
            if i not in result:
                result.append(i)
        return len(result)

    count = []

    for i in range(len(all_sub)):
        count.append(count_unique(all_sub[i]))

    return max(count)

#day 7

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2

def floodFill(image, sr, sc, newColor):
    if sr >= 1 and sc >=1:
        image[sr - 1][sc - 1] = newColor
        image[sr - 1][sc] = newColor
        image[sr - 1][sc + 1] = newColor
        image[sr][sc - 1] = newColor
        image[sr][sc] = newColor
        image[sr + 1][sc - 1] = newColor

    elif sr >= 1:
        image[sr - 1][sc] = newColor
        image[sr - 1][sc + 1] = newColor
        image[sr][sc] = newColor

    else:
        image[sr][sc - 1] = newColor
        image[sr][sc] = newColor
        image[sr + 1][sc - 1] = newColor

    return image



floodFill([[0,0,0],[0,0,0]], 0, 0, 2)

#day 14

from collections import Counter

nums = [2,2,3]

def singleNumber(nums):
    return min(Counter(nums), key=Counter(nums).get)

singleNumber(nums)

round(math.log(536870912, 2), 5).is_integer()

aa = dict(zip([range(1, 27), "abcdefghijklmnopqrstuvwxyz"))

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        output = [[]]
        
        for num in nums:
            output += [curr + [num] for curr in output]
        
        res = []
        for x in output:
            if x not in res:
                res.append(x)
        
        return res
