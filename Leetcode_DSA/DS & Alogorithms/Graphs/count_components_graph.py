def number_of_connected_components(n, edges):
    """
    Args:
     n(int32)
     edges(list_list_int32)
    Returns:
     int32
    """
    # Write your code here.
    is_visited = [False] * n
    answer = 0
    adjlist = [[] for _ in range(n)]
    for edge in edges:
        adjlist[edge[0]].append(edge[1])
        adjlist[edge[1]].append(edge[0])

    for i in range(n):
        if is_visited[i] == False:
            answer += 1
            dfs_graph(i, adjlist, is_visited)
    return answer


def dfs_graph(start_node, adjlist, is_visited):
    is_visited[start_node] = True
    for w in adjlist[start_node]:
        if is_visited[w] == False:
            dfs_graph(w, adjlist, is_visited)


print(number_of_connected_components(5,[[0 ,1], [1, 2], [0, 2], [3, 4]]))