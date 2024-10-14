'''def twoSum(num, target):
    n2, outindex = 0, []
    #d1 = num.split(',')
    for k,v in enumerate(num):
        n2 = target - v
        if n2 in num:
            outindex.append(k)
    print(outindex)


twoSum([2,3,6,8],10)'''


# not using enumerate

def twoSumsec(n1, target):
    n2, outindex = 0, []
    d1 = {}
    # d1 = num.split(',')
    for i in range(len(n1)):
        d1[n1[i]] = i

    for n in n1:
        n2 = target - n
        if n2 in n1:
            print(d1[n])


twoSumsec([2, 3, 6, 8], 9)
