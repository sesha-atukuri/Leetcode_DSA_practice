def movezeros(nums):
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1

    return nums


print(movezeros([0,1,0,3,12]))
'''i=0, j=0 and no change
i=1 j=0 , 1 0,0,3,12 
i=2, j=1 
i=3,j=1 1,3,0,0,12 
i=4,j=2 '''

