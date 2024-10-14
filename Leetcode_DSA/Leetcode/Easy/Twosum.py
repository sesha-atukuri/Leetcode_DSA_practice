def twosum(nums, target):

    dict, num = {}, 0
    test = 0
    for i in nums:
        num = target - i
        if num in dict:
            return i,num
        else:
            dict[i] += 1  # trying to assign value as '0,1,2,3..'


print(twosum([2,7,11,15], 9))
