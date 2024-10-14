def consecutive_odds(arr):
    count = 0
    for i in arr:
        if i %2 !=0:
            count += 1
            if count>=3:
                break
        else:
            count = 0
    if count == 3:
        return True
    return False



print(consecutive_odds([1,2,34,3,4,5,7,23,12]))