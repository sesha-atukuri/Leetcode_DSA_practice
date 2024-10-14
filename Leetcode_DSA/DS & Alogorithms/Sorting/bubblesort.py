def bubblesort(arr):

    for i in range(len(arr)):
        print(arr[i])
        for j in range(len(arr)-1, i, -1):
            print(arr[j],arr[j-1])
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                print(arr[j], arr[j - 1])


    return arr


print(bubblesort([5, 8, 3, 9, 4, 1, 7]))