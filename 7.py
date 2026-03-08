# 7. 8-Puzzle (A*)
def eight_puzzle(start, goal):
    def h(s): return sum(1 for i in range(9) if s[i]!=0 and s[i]!=goal[i])
    open_set = [(h(start), 0, start, [])]
    visited = set()
    while open_set:
        f, g, state, path = heapq.heappop(open_set)
        if state == goal: return path + [state]
        if state in visited: continue
        visited.add(state)
        i = state.index(0)
        moves = []
        if i%3>0: moves.append(i-1)
        if i%3<2: moves.append(i+1)
        if i>2: moves.append(i-3)
        if i<6: moves.append(i+3)
        for j in moves:
            ns = list(state); ns[i],ns[j]=ns[j],ns[i]; ns=tuple(ns)
            if ns not in visited:
                heapq.heappush(open_set,(g+1+h(ns),g+1,ns,path+[state]))

start = (1,2,5,3,4,0,6,7,8)
goal  = (1,2,5,3,4,8,6,7,0)
path = eight_puzzle(start, goal)
print("8-Puzzle steps:", len(path)-1)