import networkx as nx
import matplotlib.pyplot as plt
import math
from common import adjacency_matrix

def print_matrix(m: list[list[int]]) -> None:
    for row in m:
        print("".join(map(lambda el: str(el).rjust(3), row)))

def print_list(l: dict[int, set[int]]) -> None: 
    for v, n in l.items():
        print(f"{v}: {" ".join(map(str, n))}")

def print_path(d: list[float], p: list[int|None], start: int, end: int) -> None:
    tmp = end
    path = [] 
    while(tmp != None):
        path.append(str(tmp))
        tmp = p[tmp]
    path.reverse()
    print(f"d({end})\t= {d[end]}\t ==> [{" - ".join(path)}]")

def draw_graph(vertices: int, edges: list[tuple[int,int]], weights: list[list[int]] | None = None, *, cycles: list[list[int]] | None = None, digraph:bool = False, x_origin: float = 0.0, y_origin: float = 0.0, radius: float = 1.0):
    graph_edges = edges if weights is None else [(u, v, {"weight": weights[u][v]}) for u, v in edges]
    G = nx.DiGraph(graph_edges) if digraph else nx.Graph(graph_edges)
    G.add_nodes_from(range(vertices))
    pos = {}
    for i in range(vertices):
        alpha = 2 * math.pi / vertices
        x = x_origin + radius * math.cos(i * alpha)
        y = y_origin + radius * math.sin(i * alpha)
        pos[i] = (x, y)

    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos)

    if cycles:
        cmap = plt.colormaps["tab20"]
        for i, cycle in enumerate(cycles):
            color = cmap(i % 20)
            cycle_edges = list(zip(cycle[:-1], cycle[1:]))
            nx.draw_networkx_edges(G, pos, edgelist=cycle_edges, edge_color=color, arrows=True, arrowstyle="-|>")

    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels)
    plt.tight_layout()
    plt.show()

def transpose(m: list[list[int]]):
    return [list(row) for row in zip(*m)]
