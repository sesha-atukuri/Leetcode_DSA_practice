def check_if_sum_possible(arr, k):
    """
    Args:
     arr(list_int64)
     k(int64)
    Returns:
     bool
    """
    # Write your code here.
    count = 0
    for i in range(0,len(arr)):
        b = k - arr[i]
        if b in arr:
            count = count +1
    if count == 0:
        return False
    else:
        return True