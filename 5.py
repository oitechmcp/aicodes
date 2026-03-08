# 5. AO* Search
def ao_star(graph, start, costs):
    def solve(node):
        if node not in graph: return costs.get(node, 0), [node]
        best_cost, best_path = float('inf'), []
        for group in graph[node]:
            c = sum(costs.get(n,0) for n in group)
            paths = [n for n in group]
            if c < best_cost: best_cost, best_path = c, [node] + paths
        return best_cost, best_path
    return solve(start)

ao_graph = {'A': [['B','C'], ['D']], 'B': [['E']], 'C': [['F']]}
ao_costs = {'E':1,'F':2,'D':3}
print("AO*:", ao_star(ao_graph, 'A', ao_costs))