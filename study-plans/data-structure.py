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

# day 11

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root:
            queue = [(1, root)]
            temp = []
            result = {1: []}

            while queue:
                i, node = queue.pop(0)

                if node.left:
                    queue.append((i + 1, node.left))
                    result[i + 1] = []

                if node.right:
                    queue.append((i + 1, node.right))
                    result[i + 1] = []

                result[i] += [node.val]
                print(result)

            return list(result.values())

def combinations(nums):
        result = []

        def backtracking(n, k, index, nums):
            nums = nums or []

            if len(nums) == k:
                result.append(nums[:])
                return

            for i in range(index, n):
                nums.append(i + 1)
                backtracking(n, k, i + 1, nums)
                nums.pop()

        backtracking(n, k, 0, None)

        return result



