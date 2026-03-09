import heapq

def astar(grid, start, goal):
    h = lambda a,b: abs(a[0]-b[0]) + abs(a[1]-b[1])
    pq = [(h(start,goal), 0, start, [start])]
    visited = set()

    while pq:
        f, g, node, path = heapq.heappop(pq)
        if node == goal: return path
        if node in visited: continue
        visited.add(node)

        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            x,y = node[0]+dx, node[1]+dy
            if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y]==0:
                heapq.heappush(pq,(g+1+h((x,y),goal), g+1, (x,y), path+[(x,y)]))

grid=[[0,0,0],[0,1,0],[0,0,0]]
print(astar(grid,(0,0),(2,2)))
