def mst_prim(graph: list[list[int]], 
             weights: list[list[int]]) -> tuple[int, list[int]]:
    T = [0]
    W = [i for i in range(1, len(graph))]
    res = []
    while len(T) != len(graph):
        l = min([(weights[u][v], u, v) for v in W for u in T if graph[u][v]])

        T.append(l[2])
        W.remove(l[2])
        res.append(l[1:])

    return sum(map(lambda e: weights[e[0]][e[1]], res)), res

def mst_kruskal(graph: list[list[int]], 
                weights: list[list[int]]) -> tuple[int, list[int]]:
    edges = [(weights[u][v], u, v) for v in range(len(graph)) 
             for u in range(len(graph)) if graph[u][v]]

    edges.sort()

    T: list[set[int]] = []
    res = []

    def get_group(n: int) -> int | None:
        for i, tree in enumerate(T):
            if n in tree:
                return i
        return None
                
    for _, u, v in edges:
        gu = get_group(u)
        gv = get_group(v)

        if gu is None and gv is None:
            T.append({u, v})
        elif gu is None and gv is not None:
            T[gv].add(u)
        elif gu is not None and gv is None:
            T[gu].add(v)
        elif gu != gv: 
            T[gu].update(T.pop(gv)) # type: ignore
        elif gu == gv:
            continue

        res.append((u, v))
        if len(res) == len(graph) - 1:
            break

    return sum(map(lambda e: weights[e[0]][e[1]], res)), res
