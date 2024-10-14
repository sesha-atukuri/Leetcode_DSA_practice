def sqft(x):

    if x == 0 or x == 1:
        return x
    start = 2
    end = x
    while start<=end:
        mid = start + ((end-start)//2)
        if x == (mid*mid):
            return mid
        elif (mid*mid) > x:
            end = mid-1
        else:
            start = mid+1
        return end


    '''if x < 4: return 1 if x else 0
    s, e, m = 1, x, -1
    while (s <= e):
        m = (s + e) // 2
        if m * m == x:
            return m
        elif m * m > x:
            e = m - 1
        else:
            s = m + 1
    return m - 1 if m * m > x else m'''
    '''temp= 2
    while temp<=(x//2):
        if temp*temp == x:
            return temp
        elif temp*temp > x:
            return temp-1
        temp += 1'''



print(sqft(8))