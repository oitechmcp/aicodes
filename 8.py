# 8. Water Jug Problem (BFS)
def water_jug(cap_a, cap_b, target):
    visited = set()
    queue = deque([(0,0,[])])
    while queue:
        a, b, path = queue.popleft()
        if (a,b) in visited: continue
        visited.add((a,b)); path = path + [(a,b)]
        if a==target or b==target: return path
        states = [(cap_a,b),(a,cap_b),(0,b),(a,0),
                  (a-min(a,cap_b-b),b+min(a,cap_b-b)),
                  (a+min(b,cap_a-a),b-min(b,cap_a-a))]
        for s in states:
            if s not in visited: queue.append((*s,path))

print("Water Jug:", water_jug(4,3,2))