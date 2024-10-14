def single_num(nums):
    num = set()
    for i in range(len(nums)):
        if nums[i] in num:
            num.remove(nums[i])
        else:
            num.add(nums[i])

    return num.pop()

print(single_num([1,0,1]))