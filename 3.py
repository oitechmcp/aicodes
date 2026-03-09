# DFS (Depth First Search)

def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()

    visited.add(node)
    print(node, end=' ')

    for n in graph[node]:
        if n not in visited:
            dfs(graph, n, visited)

# Graph definition
graph = {0:[1,2], 1:[0,3,4], 2:[0], 3:[1], 4:[1]}

dfs(graph, 0)
print()
