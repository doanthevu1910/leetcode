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

