def findmissingranges(nums,lower,upper):
    result = []
    nums = [lower-1]+nums+[upper+1]

    for n in range(len(nums)):
        if n < len(nums)-1 and nums[n+1]-nums[n] > 1 :
            result.append([nums[n]+1,nums[n+1]-1])


    return result


print(findmissingranges([1,3,50,75],0,99))
