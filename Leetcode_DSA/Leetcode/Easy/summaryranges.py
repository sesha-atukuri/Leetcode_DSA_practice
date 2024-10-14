def summaryRanges(nums):
    start = nums[0]
    output =[]
    for n in range(len(nums)):

        while (n < len(nums)-1) and nums[n+1] == (nums[n]+1):
            n +=1

            end = nums[n]

        output.append([start,end]) if start != end else output.append([end])
        start = nums[n+1] if n < len(nums)-1 else ""

    return output



print(summaryRanges([0,1,2,4,5,7]))