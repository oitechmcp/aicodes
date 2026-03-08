# 9. Travelling Salesman Problem (brute force)
def tsp(dist):
    n = len(dist)
    cities = list(range(1,n))
    best = float('inf')
    for perm in itertools.permutations(cities):
        route = [0]+list(perm)+[0]
        cost = sum(dist[route[i]][route[i+1]] for i in range(n))
        best = min(best, cost)
    return best

dist = [[0,10,15,20],[10,0,35,25],[15,35,0,30],[20,25,30,0]]
print("TSP:", tsp(dist))