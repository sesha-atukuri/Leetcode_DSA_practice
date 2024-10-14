def happy_num(n):
    visited = set()
    while n != 1 and n not in visited:
        visited.add(n)
        n = sum([int(digit)**2 for digit in str(n)])
        #n = sum(digit**2 for digit in digits)

    return n == 1


print(happy_num(19))