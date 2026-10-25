def create_matrix(vertices: int, edges: list[tuple[int, int]], *, 
                  digraph: bool = False)->list[list[int]]:
    if vertices < 0:
        raise ValueError("Number of vertices cannot be a negative number.")
    if len(edges) > vertices * (vertices - 1) / 2:
        raise ValueError("Number of edges out of possible range.")
    for edge in edges:
        if edge[0] > vertices - 1:
            raise ValueError(f"Edge ({edge[0]}, {edge[1]}) is incorrect. Vertex with label {edge[0]} does not exist.")
        if edge[1] > vertices - 1:
            raise ValueError(f"Edge ({edge[0]}, {edge[1]}) is incorrect. Vertex with label {edge[1]} does not exist.")
    matrix = [[0] * len(edges) for _ in range(vertices)]

    for i, edge in enumerate(edges):
        matrix[edge[0]][i] = 1 if not digraph else -1
        matrix[edge[1]][i] = 1

    return matrix

def add_vertex(neighbours: list[int], graph: list[list[int]], *, 
               digraph: bool = False) -> list[list[int]]:
    new_vertex = len(graph)

    if new_vertex == 0:
        graph.append([])
        return graph

    for n in neighbours:
        for v in range(new_vertex):
            if v == n:
                graph[v].append(1)
            else:
                graph[v].append(0)

    old_edges_count = len(graph[0]) - len(neighbours)
    new_row = [0] * old_edges_count 
    new_row.extend([1 if not digraph else -1] * len(neighbours))
    graph.append(new_row)
    
    return graph

def drop_vertex(vertex_number: int, graph: list[list[int]]) -> list[list[int]]:
    trash_row = graph[vertex_number]
    neighbours_columns = [i for i in range(len(trash_row)) if trash_row[i] != 0]
    graph.pop(vertex_number)
    for row in graph:
        for column in reversed(neighbours_columns):
            row.pop(column)
    return graph

def get_edges(graph: list[list[int]], *, digraph: bool = False) -> tuple[int, list[tuple[int, int]]]:
    """Digraph is not used, provided only to achievie coherent API."""
    edges = []
    for edge_row in [list(row) for row in zip(*graph)]:
        edge = tuple(map(lambda el: el[1], 
                         sorted([(v, i) for i, v in enumerate(edge_row) if v])))
        edges.append(edge)

    return len(graph), edges
        
def from_file(filename: str) -> list[list[int]]: 
    with open(filename, 'r') as f:
        m = [[int(num) for num in line.split()] for line in f]
    return m