import networkx as nx
import matplotlib.pyplot as plt
import math

def draw_circle_graph(vertices: int, edges: list[tuple[int, int]], x_origin: float = 0.0, y_origin: float = 0.0, radius: float = 1.0):
    G = nx.Graph(edges)
    pos = {}
    for i in range(vertices):
        alpha = 2 * math.pi / vertices
        x = x_origin + radius * math.cos(i * alpha)
        y = y_origin + radius * math.sin(i * alpha)
        pos[i] = (x, y)

    options = {
    "font_size": 36,
    "node_size": 2000,
    "node_color": "white",
    "edgecolors": "red",
    "linewidths": 5,
    "width": 5,
    }
    nx.draw(G, pos, with_labels=True, **options)
    plt.show()