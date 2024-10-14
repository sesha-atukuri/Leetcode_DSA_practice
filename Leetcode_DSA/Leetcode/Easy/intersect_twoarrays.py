def intersect_arrays(arr1,arr2):
    dict1 = {}
    result = []
    for num in arr1:
        if num not in dict1:
            dict1[num] = 1
        else:
            dict1[num] += 1
    for num2 in arr2:
        if num2 in dict1 and dict1[num2]>0:
            result.append(num2)
            dict1[num2] -= 1


    '''for i in arr1:
        if i in arr2:
            if i not in result:
                result.append(i)'''

    return result

print(intersect_arrays([4,9,5],[9,4,9,8,4]))