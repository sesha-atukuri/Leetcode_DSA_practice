def funcDistinctPair(inputArray, targetValue):
    # Write your code here
    pair_set = set()
    visited = []
    for n in inputArray:
        if n in visited:
            continue
        second = targetValue - n
        if second in inputArray:
            visited.append(second)
            pair_set.add((n, second))

    # print(pair_set)

    return len(pair_set)
print(funcDistinctPair([9,3,6,6,6],12))
