def maxSubArray(nums):
    max_ending_here = 0
    max_so_far = -100000
    for i in range(len(nums)):
        max_ending_here = max_ending_here + nums[i]
        if max_ending_here < nums[i]:
            max_ending_here = nums[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
    return max_so_far

def merge(nums1, m, nums2, n):
    nums1[m:] = nums2[:n]
    for i in range(len(nums1)):
        for i in range(len(nums1) - 1):
            if nums1[i] > nums1[i + 1]:
                nums1[i], nums1[i + 1] = nums1[i + 1], nums1[i]
    return nums1


import numpy as np

def intersect(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []

        for i in range(len(nums1)):
            if nums1[i] in nums2:
                result.append(nums1[i])

        return result

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]

import numpy as np

def searchMatrix(matrix, target):
    reshaped = np.reshape(matrix, (1, len(matrix) * len(matrix[0])))
    reshaped = reshaped[0]
    return any(element == target for element in reshaped)

searchMatrix(matrix, 3)

def checkValid(matrix):
    newmat = matrix + list(zip(*matrix))

    return all(len(set(nums)) == len(nums) for nums in newmat)

matrix = [[1,2,3],[3,1,2],[2,3,1]]

# matrix = [[1,2,3],[4,5,6],[7,8,9]]

nums = (matrix + list(zip(*matrix)))[0]

len(nums)

#day 6
s = "loveleetcode"

c = Counter(s)

c[s[2]]

s[2]
from collections import Counter

def firstUniqChar(s):
    c = Counter(s)
    for i in range(len(s)):
        if c[s[i]] == 1:
            return i
    return -1

ransomNote = "aa"
magazine = "aab"

def canConstruct(ransomNote, magazine):
    c1 = Counter(ransomNote)
    c2 = Counter(magazine)

    sum = 0

    for i in range(len(ransomNote)):
        if c1[ransomNote[i]] <= c2[ransomNote[i]]:
            sum += 1

    return sum == len(ransomNote)

canConstruct('a', 'b')

s = "anagram"
t = "nagaram"

def isAnagram(s, t):
    return Counter(s) == Counter(t)

isAnagram(s, t)

# day 7