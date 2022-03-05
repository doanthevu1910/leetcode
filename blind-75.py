import re
import numpy as np
s = "A man, a plan, a canal: Panama"

nums = [1, 2, 3, 4]

def prod(nums, i):
    return np.product(nums[:i] + nums[i+1:])

def productExceptSelf(nums):
    result = []
    for i in range(len(nums)):
        result.append(prod(nums, i))
    return result

productExceptSelf(nums)

def isPalindrome(s):
    s = ''.join(ch for ch in s if ch.isalnum()).lower()
    return s == s[::-1]

def countSubstrings(s):

    sub = [s[i: j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]

    count = 0

    for i in range(len(sub)):
        if isPalindrome(sub[i]) == True:
            count += 1

    return count



