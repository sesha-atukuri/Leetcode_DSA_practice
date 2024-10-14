def dfs_traversal(n, edges):
    """
    Args:
     n(int32)
     edges(list_list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    is_visited = [False] * n
    answer = []
    adjlist = [[] for _ in range(n)]
    for edge in edges:
        adjlist[edge[0]].append(edge[1])
        adjlist[edge[1]].append(edge[0])

    for i in range(n):
        if is_visited[i] == False:
            answer.append(i)
            dfs_graph(i, adjlist, is_visited, answer)
    return answer


def dfs_graph(start_node, adjlist, is_visited, answer):
    is_visited[start_node] = True
    for w in adjlist[start_node]:
        if is_visited[w] == False:
            answer.append(w)
            dfs_graph(w, adjlist, is_visited,answer)

print(dfs_traversal(6, [
[0, 1],
[0, 2],
[1, 4],
[3, 5]
]))