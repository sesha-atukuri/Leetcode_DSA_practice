def smallersum(target,arr):
    #res = set()
    count = 0
    arr.sort()
    for i in range(len(arr)):
        j = i + 1
        k = len(arr) - 1
        while j < k:
            total = arr[i] + arr[j] + arr[k]
            if total < target:
                count += k-j
                j += 1
            else:

                k -= 1


    return count

print(smallersum(4,[5, 0, -1, 3, 2]))

