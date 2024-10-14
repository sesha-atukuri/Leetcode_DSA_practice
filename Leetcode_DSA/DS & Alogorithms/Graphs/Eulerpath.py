
def eulerpath(n,edges):
    degree = [0] * n
    print(type(degree))
    count = 0
    for edge in edges:
        degree[edge[0]] += 1
        degree[edge[1]] += 1

    for d in degree:
        if d % 2 != 0:
            count += 1
    if count == 0 or count == 2:
        return True
    return False

print(eulerpath(4,[[0, 1],
[1, 2],
[1, 3],
[2, 0],
[3, 2]]))