def missing_num(nums):
    res = len(nums)
    for i in range(len(nums)):
        res += i-nums[i]

    return res
print(missing_num([0,1]))

''' nums.sort()

    for index in range(len(nums)):
        if index != nums[index]:
            return index
        else:
            return len(nums)'''

