# 13. Missionaries and Cannibals
def missionaries_cannibals():
    start = (3,3,1); goal = (0,0,0)
    def valid(m,c): return (m==0 or m>=c) and (3-m==0 or 3-m>=3-c)
    queue = deque([(start,[start])])
    visited = {start}
    while queue:
        state, path = queue.popleft()
        if state==goal: return path
        m,c,b = state
        moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]
        for dm,dc in moves:
            if b==1: nm,nc,nb = m-dm,c-dc,0
            else: nm,nc,nb = m+dm,c+dc,1
            if 0<=nm<=3 and 0<=nc<=3 and valid(nm,nc) and valid(3-nm,3-nc):
                ns=(nm,nc,nb)
                if ns not in visited: visited.add(ns); queue.append((ns,path+[ns]))

path = missionaries_cannibals()
print("M&C steps:", len(path)-1)