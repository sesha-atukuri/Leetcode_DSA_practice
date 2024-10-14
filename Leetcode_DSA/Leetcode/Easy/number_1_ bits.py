def num_of_bits(n):
    binary = f'{n:b}'
    result = 0
    for i in binary:
        if i == '1':
            result += 1
    return result


print(num_of_bits(11))

'''optimal solution
def hammingWeight(n: int) -> int:
    count = 0
    while n != 0:
        n &= (n - 1)  # this is the main logic of the code, n-1 flips the bits including and after the right most '1'
        #print(n&(n-1))
        count += 1
    return count'''