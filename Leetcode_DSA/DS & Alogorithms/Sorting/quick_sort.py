import random
def quick_sort_helper(arr, start, end):

    if start >= end:
        return
    pivotindex = random.randrange(start, end)
    arr[start], arr[pivotindex] = arr[pivotindex], arr[start]
    pivot = arr[start]
    smaller = start+1
    bigger = end

    while smaller <= bigger:
        if arr[smaller] < pivot:
            smaller = smaller+1
        elif arr[bigger] > pivot:
            bigger = bigger-1
        else:
            arr[smaller], arr[bigger] = arr[bigger], arr[smaller]
            smaller = smaller+1
            bigger = bigger-1
    arr[start], arr[bigger] = arr[bigger], arr[start]

    quick_sort_helper(arr, start, bigger-1)
    quick_sort_helper(arr, bigger+1, end)


def quick_sort(arr):

    quick_sort_helper(arr, 0, len(arr)-1)

    return arr


print(quick_sort([5, 8, 3, 9, 4, 1, 7]))