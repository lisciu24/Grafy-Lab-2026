from common import adjacency_matrix

def dijkstra(graph: list[list[int]], weights: list[list[int]], 
             start: int) -> tuple[bool, list[float], list[int|None]]:
    d, p = _init(len(graph), start)
    S = []
    while len(S) != len(graph):
        u = min([(d[i], i) for i in range(len(graph)) if i not in S])[1]
        S.append(u)
        neighbours = [v for v, n in enumerate(graph[u]) if n and v not in S]
        for v in neighbours:
            _relax(d, p, weights, u, v)

    return True, d, p

def bellman_ford(graph: list[list[int]], weights: list[list[int]], 
                 start: int) -> tuple[bool, list[float], list[int|None]]:
    d, p = _init(len(graph), start)
    _, edges = adjacency_matrix.get_edges(graph, digraph=True)
    for _ in range(len(graph) - 1):
        for u, v in edges:
            _relax(d, p, weights, u, v)

    for u, v in edges:
        if d[v] > d[u] + weights[u][v]:
            return False, d, p

    return True, d, p

def johnson(graph: list[list[int]], weights: list[list[int]]) -> list[list[int]]:
    Gs = [graph[v].copy() for v in range(len(graph))]
    Gs = adjacency_matrix.add_vertex([v for v in range(len(Gs))], Gs, digraph=True) 
    w = [weights[v].copy() for v in range(len(weights))]
    w = adjacency_matrix.add_vertex([], w)
    good, d, _ = bellman_ford(Gs, w, len(Gs) - 1)
    if not good:
        raise ValueError("Bellman ford found negative sum cycle.")

    h = [d[v] for v in range(len(Gs))]
    _, edges = adjacency_matrix.get_edges(Gs, digraph=True)
    for u, v in edges:
        w[u][v] = w[u][v] + h[u] - h[v] # type: ignore

    D = [[-1 for _ in range(len(graph))] for _ in range(len(graph))]
    for u in range(len(graph)):
        _, d, _ = dijkstra(graph, w, u)
        for v in range(len(graph)):
            D[u][v] = d[v] - h[u] + h[v] # type: ignore
            
    return D

def distance_matrix(graph: list[list[int]], weights: list[list[int]], 
                    fun) -> list[list[int]]:
    m = []
    for i in range(len(graph)):
        _, d, _ = fun(graph, weights, i)
        m.append(d)

    return m

def get_graph_center(distance_matrix: list[list[int]]) -> tuple[int,int]:
    d, i = min([(sum(d), i) for i, d in enumerate(distance_matrix)])

    return i, d

def get_graph_minmax_center(distance_matrix: list[list[int]]) -> tuple[int, int]:
    d, i = min([(max(d), i) for i, d in enumerate(distance_matrix)])

    return i, d

def _init(graph_size: int, s: int) -> tuple[list[float], list[int|None]]:
    d = [float('inf') for _ in range(graph_size)]
    p: list[int|None] = [None for _ in range(graph_size)]
    d[s] = 0
    return d, p

def _relax(d: list[float], p: list[int|None], w: list[list[int]], 
           u: int, v: int):
    if d[v] > d[u] + w[u][v]:
        d[v] = d[u] + w[u][v]
        p[v] = u



