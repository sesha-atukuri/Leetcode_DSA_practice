def subset(n):
    if n ==0:
        return 1
    else:
        return 2*subset(n-1)


print(subset(27))