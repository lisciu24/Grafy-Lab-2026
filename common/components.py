from common import util

def DFS_vitis(v: int, G: list[list[int]], d: list[int], f: list[int], t: int) -> int:
    t = t + 1
    d[v] = t
    for u in (u for u, edge in enumerate(G[v]) if edge):
        if d[u] == -1:
            t = DFS_vitis(u, G, d, f, t)
    t = t + 1
    f[v] = t
    return t

def components_r(nr: int, v: int, Gt: list[list[int]], comp: list[int]) -> None:
    for u in (u for u, edge in enumerate(Gt[v]) if edge):
        if comp[u] == -1:
            comp[u] = nr
            components_r(nr, u, Gt, comp)

def kosaraju(graph: list[list[int]]) -> tuple[int, list[int]]:
    d = [-1 for _ in range(len(graph))]
    f = [-1 for _ in range(len(graph))]
    t = 0

    for v in range(len(graph)):
        if d[v] == -1: 
            t = DFS_vitis(v, graph, d, f, t)

    gt = util.transpose(graph)
    nr = 0
    comp = [-1 for _ in range(len(gt))]
    for _, v in sorted([(f[v], v) for v in range(len(f))], reverse=True):
        if comp[v] == -1:
            nr = nr + 1
            comp[v] = nr
            components_r(nr, v, gt, comp)
        
    return nr, comp



