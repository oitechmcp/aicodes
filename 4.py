# 4. A* Search
def astar(grid, start, goal):
    def h(a, b): return abs(a[0]-b[0]) + abs(a[1]-b[1])
    open_set = [(0+h(start,goal), 0, start, [start])]
    visited = set()
    while open_set:
        f, g, curr, path = heapq.heappop(open_set)
        if curr == goal: return path
        if curr in visited: continue
        visited.add(curr)
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx,ny = curr[0]+dx, curr[1]+dy
            if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and grid[nx][ny]==0 and (nx,ny) not in visited:
                ng = g+1
                heapq.heappush(open_set, (ng+h((nx,ny),goal), ng, (nx,ny), path+[(nx,ny)]))

grid = [[0,0,0],[0,1,0],[0,0,0]]
print("A*:", astar(grid,(0,0),(2,2)))