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


