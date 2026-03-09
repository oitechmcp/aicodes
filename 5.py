# 5. AO* Search
def ao_star(graph, start, costs):

    def solve(node):
        if node not in graph:
            return costs.get(node, 0), [node]

        best_cost = float('inf')
        best_path = []

        for group in graph[node]:   # AND groups
            total_cost = 0
            path = [node]

            for n in group:
                c, p = solve(n)
                total_cost += c
                path += p

            if total_cost < best_cost:
                best_cost = total_cost
                best_path = path

        return best_cost, best_path

    return solve(start)


ao_graph = {'A': [['B','C'], ['D']], 'B': [['E']], 'C': [['F']]}
ao_costs = {'E':1, 'F':2, 'D':3}

print("AO*:", ao_star(ao_graph, 'A', ao_costs))
