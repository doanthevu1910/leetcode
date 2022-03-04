nums = [2,2,1,1,1,2,2]

from collections import Counter

if Counter(nums)[nums[0]] > len(nums)/2:
    print(nums[0])

