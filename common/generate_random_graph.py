from random import sample, random
def generate_random_graph(vertices: int, edges: int = None, edges_prob: float = None) -> (int, list[tuple[int, int]]):
    if vertices < 0:
        raise ValueError("Number of vertices cannot be a negative number.")
    if None == edges and None == edges_prob:
        return
    if edges != None:
        if edges >= 0 and edges <= vertices * (vertices - 1) / 2:
            g_edges = set()

            while edges > len(g_edges):
                vertex1, vertex2 = sample(range(0, vertices), 2)
                if (vertex1, vertex2) not in g_edges and (vertex2, vertex1) not in g_edges:
                    g_edges.add((vertex1, vertex2))
            g_edges = [*g_edges]
            return vertices, g_edges
        else:
            raise ValueError("Value out of possible range.")
    elif edges_prob != None:
        if edges_prob >= 0 or edges_prob <= 1:
            g_edges = set()

            for vertex1 in range(vertices):
                for vertex2 in range(vertices):
                    if vertex1 != vertex2 and (vertex1, vertex2) not in g_edges and (vertex2, vertex1) not in g_edges:
                        r_number = random()
                        if r_number < edges_prob:
                            g_edges.add((vertex1, vertex2))
            g_edges = [*g_edges]
            return vertices, g_edges
        else:
            raise ValueError("Value out of possible range.")
