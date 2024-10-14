def convert_edge_list_to_adjacency_list(n, edges):
    adjacency_list = [[] for _ in range(n)]

    print(adjacency_list)

    for edge in edges:
        adjacency_list[edge[0]].append(edge[1])
        adjacency_list[edge[1]].append(edge[0])
    print(adjacency_list)

    for i in range(n):
        adjacency_list[i].sort()

    return adjacency_list


print(convert_edge_list_to_adjacency_list(5, [[0, 1],
[1, 4],
[1, 2],
[1, 3],
[3, 4]
]))