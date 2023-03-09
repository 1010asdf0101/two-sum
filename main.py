def twoSum(nums, target):
    for i, x in enumerate(nums[1:]):
        if nums[i]+nums[i-1]==target: return [i, i+1]

