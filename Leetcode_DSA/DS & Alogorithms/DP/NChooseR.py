def ncr(n,r):
    global result
    result = [[0 for _ in range(r + 1)] for _ in range(n + 1)]
    return ncr1(n,r)

def ncr1(n,r):
    if r>n:
        return 0
    if n==r or r == 0:
        return 1


    result[n][r] = (ncr1(n - 1, r) + ncr1(n - 1, r - 1)) % 1000000007
    return result[n][r]


print(ncr(5,3))

