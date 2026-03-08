# 3. DFS
def dfs(graph, node, visited=None):
    if visited is None: visited = set()
    visited.add(node); print(node, end=' ')
    for n in graph[node]:
        if n not in visited: dfs(graph, n, visited)

dfs(graph, 0)
print()