def jump_ways(n):
    """
    Args:
     n(int32)
    Returns:
     int64
    """
    # Write your code here.
    m = n+1
    table = [0]*(n+1)
    table[0] = 1
    table[1] = 1
    for i in range(2, m):
        table[i] = table[i-1] + table[i-2]
    return table[n]

print(jump_ways(3))