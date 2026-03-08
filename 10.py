# 10. Monkey Banana Problem (BFS)
def monkey_banana():
    start = ('door','floor','door',False)
    goal  = ('middle','on_box','middle',True)
    def moves(state):
        pos,on,box,has = state; next_states=[]
        if on=='floor':
            for p in ['door','middle','window']:
                next_states.append((p,on,box,has))
            if pos==box: next_states.append((pos,'on_box',box,has))
        if on=='on_box' and pos=='middle': next_states.append((pos,on,box,True))
        if on=='floor':
            for p in ['door','middle','window']:
                next_states.append((pos,on,p,has))
        return next_states
    queue = deque([(start,[start])])
    visited = {start}
    while queue:
        state, path = queue.popleft()
        if state == goal: return path
        for ns in moves(state):
            if ns not in visited: visited.add(ns); queue.append((ns,path+[ns]))

print("Monkey Banana steps:", len(monkey_banana())-1)