def majorityElement(nums):
    dict = {}

    for i in range(len(nums)):
        if nums[i] not in dict:
            dict[nums[i]] = 1
        else:
            dict[nums[i]] += 1

    for key, value in dict.items():
        if value > (len(nums) // 2):
            return key


print(majorityElement([3,2,3]))