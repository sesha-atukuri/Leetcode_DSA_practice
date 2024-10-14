def removeDuplicates(nums):



    ouput_set = set("_" * len(nums))

    for i in nums:
        ouput_set.add(i)
    return ouput_set

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))