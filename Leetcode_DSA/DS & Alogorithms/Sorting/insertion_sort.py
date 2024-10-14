def insertionsort(arr):

    for i in range(1, len(arr)):

        temp = arr[i]
        empty_index = i
        while empty_index>0 and arr[empty_index-1] > temp:

            arr[empty_index] = arr[empty_index-1]
            empty_index = empty_index - 1

        arr[empty_index] = temp

    return arr


print(insertionsort([5, 8, 3, 9, 4, 1, 7]))