# 2. BFS
def bfs(graph, start):
    visited, queue = set(), deque([start])
    visited.add(start)
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for n in graph[node]:
            if n not in visited:
                visited.add(n); queue.append(n)

graph = {0:[1,2],1:[0,3,4],2:[0],3:[1],4:[1]}
bfs(graph, 0)
print()
