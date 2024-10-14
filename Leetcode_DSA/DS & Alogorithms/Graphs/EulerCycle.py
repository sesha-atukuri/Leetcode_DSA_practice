
def eulercycle(n,edges):
    degree = [0] * n
    for edge in edges:
        degree[edge[0]] += 1
        degree[edge[1]] += 1

    for d in degree:
        if d % 2 != 0:
            return False
    return True

print(eulercycle(5,[[0, 1],
[0, 2],
[1, 3],
[3, 0],
[3, 2],
[4, 3],
[4, 0]]))