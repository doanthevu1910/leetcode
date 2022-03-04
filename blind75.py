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