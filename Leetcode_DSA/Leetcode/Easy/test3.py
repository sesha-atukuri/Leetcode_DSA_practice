def funcPrint(numRow, numColumn):
    # Write your code here
    output = [''.join('#' if (row + col) % 2 == 0 else '$' for col in range(numColumn)) for row in range(numRow)]
    result = '\n'.join(output)
    '''for row in range(numRow):
        for col in range(numColumn):
            if (row+ col)%2 == 0:
                print('#', end = '')
            else:
                print('$',end = '')

        print()'''
    return result
