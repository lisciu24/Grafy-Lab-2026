def dijkstra(graph: list[list[int]], 
             weights: list[list[int]], 
             start: int) -> tuple[list[float], list[int|None]]:
    d = [float('inf') for _ in range(len(graph))]
    p: list[int|None] = [None for _ in range(len(graph))]
    d[start] = 0

    S = []
    while len(S) != len(graph):
        u = min([(d[i], i) for i in range(len(graph)) if i not in S])[1]
        S.append(u)
        neighbours = [i for i, n in enumerate(graph[u]) if n]
        for v in neighbours:
            if v in S: 
                continue
            if d[v] > d[u] + weights[u][v]:
                d[v] = d[u] + weights[u][v]
                p[v] = u

    return d, p

def distance_matrix(graph: list[list[int]], 
                    weights: list[list[int]]) -> list[list[int]]:
    m = []
    for i in range(len(graph)):
        d, _ = dijkstra(graph, weights, i)
        m.append(d)

    return m

def get_graph_center(distance_matrix: list[list[int]]) -> tuple[int,int]:
    d, i = min([(sum(d), i) for i, d in enumerate(distance_matrix)])

    return i, d

def get_graph_minmax_center(distance_matrix: list[list[int]]) -> tuple[int, int]:
    d, i = min([(max(d), i) for i, d in enumerate(distance_matrix)])

    return i, d
        



