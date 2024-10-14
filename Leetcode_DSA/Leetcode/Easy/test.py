def funcLargestElement(inputList):
    # Write your code here
    dict1 = {}
    for num in range(len(inputList)):
        print(dict1[inputList[num]])
        if dict1[inputList[num]] not in dict1:
            dict1[inputList[num]] = 1
        else:
            dict1[inputList[num]] += 1

    max_num = inputList[0]
    for num in range(1, len(inputList)):
        if inputList[num] > max_num:
            max_num = inputList[num]

    return dict1[max_num]

print(funcLargestElement([1,2,3,4]))