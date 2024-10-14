
 # Given a number n, generate all possible binary strings of length n.
def helper(index, current, result):
    if index == len(current):
        return result.append("".join(current))

    current[index] = '0'
    helper(index+1, current, result)
    current[index] = '1'
    helper(index+1, current, result)


def binary_strings(n):
    result = []
    current = ['0'] * n
    helper(0, current, result)
    return result

print(binary_strings(3))