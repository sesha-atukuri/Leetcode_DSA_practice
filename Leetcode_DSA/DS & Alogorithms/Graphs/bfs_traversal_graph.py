from collections import deque

def graph_helper(start_node, graph, is_visited, answer):
    is_visited[start_node] = True
    answer.append(start_node)
    q = deque([start_node])

    while q:
        u = q.popleft()
        print(u)
        for W in graph[u]:
            if not is_visited[W]:
                is_visited[W] = True
                q.append(W)
                answer.append(W)


def bfs_graph(n,edges):
    answer = []
    is_visited = [False] * n
    graph = [[] for _ in range(n)]

    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    for i in range(n):
        if not is_visited[i]:
            graph_helper(i, graph, is_visited,answer)


    return answer

print(bfs_graph(6,[[0, 1], [0, 2], [0, 4], [2, 3]]))
