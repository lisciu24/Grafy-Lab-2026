from common import components

def find_euler_cycle(v, e):
    edges = e.copy()
    curr = 0
    cycle = [curr]

    while edges:
        neighbor_edges = [edge for edge in edges if curr in edge]

        for edge in neighbor_edges:
            nxt = edge[1] if edge[0] == curr else edge[0]

            if len(neighbor_edges) == 1: # only possibility - need to go this way
                edges.remove(edge)
                curr = nxt
                cycle.append(curr)
                break

            comp_before = max(components.components(v, edges))
            edges_without = [x for x in edges if x != edge]
            comp_after = max(components.components(v, edges_without))

            if comp_after <= comp_before: # not a bridge - can go this way
                edges.remove(edge)
                curr = nxt
                cycle.append(curr)
                break

    return cycle


def find_hamilton(v, e):
    adj = {i: [] for i in range(v)}
    for a, b in e:
        adj[a].append(b)
        adj[b].append(a)

    path = [0]

    def backtrack(curr):
        if len(path) == v:
            return 0 in adj[curr] # is it a cycle?
                
        for neighbor in adj[curr]:
            if neighbor not in path:
                path.append(neighbor) # try this new path
                
                if backtrack(neighbor): # if true - hamilton found
                    return True
                    
                path.pop() # otherwise pop - backtracking

        return False

    if backtrack(0): #starting backtracking ad vertex 0. if returns true - hamilton found
        path.append(0)  
        return path
    else:
        return None   

    