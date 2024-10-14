# Given an array of unique numbers, return in any order all its permutations.

def get_permutations(arr):

    result = []
    current = ['0']*len(arr)
    print(arr[:])
    helper(0, current, result)
    return result


def helper(index, current, result):
    if index == len(current):
        return result.append("".join(current))

    helper(index+1, current, result)


print(get_permutations([1,2,3]))