import networkx as nx
import matplotlib.pyplot as plt

def draw_digraph(vertices, edges: list[tuple[int, int]]):
    G = nx.DiGraph()
    
    if isinstance(vertices, int):
        G.add_nodes_from(range(vertices))
    else:
        G.add_nodes_from(vertices)
        
    G.add_edges_from(edges)

    options = {
        "font_size": 20,
        "node_size": 2000,
        "node_color": "white",
        "edgecolors": "black",
        "linewidths": 5,
        "width": 2,
        "arrows": True,
        "arrowsize": 10,     
    }

    pos = nx.spring_layout(G, seed=42, k=0.5)

    nx.draw(G, pos, with_labels=True, **options)
    plt.show()