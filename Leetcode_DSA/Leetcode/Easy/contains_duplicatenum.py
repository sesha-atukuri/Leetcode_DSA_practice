def contain_duplicate(nums):
    nums_set = set(nums)
    return False if len(nums_set) == len(nums) else True




print(contain_duplicate([1,2,3,4]))