def create_list(vertices: int, edges: list[tuple[int, int]], *, 
                digraph: bool = False) -> dict[int, set[int]]:
    if vertices < 0:
        raise ValueError("Number of vertices cannot be a negative number.")
    if len(edges) > vertices * (vertices - 1) / 2:
        raise ValueError("Number of edges out of possible range.")
    for edge in edges:
        if edge[0] > vertices - 1:
            raise ValueError(f"Edge ({edge[0]}, {edge[1]}) is incorrect. Vertex with label {edge[0]} does not exist.")
        if edge[1] > vertices - 1:
            raise ValueError(f"Edge ({edge[0]}, {edge[1]}) is incorrect. Vertex with label {edge[1]} does not exist.")
    
    adjacency_list = dict()
    
    for i in range(vertices):
        adjacency_list[i] = set()

    for edge in edges:
        vertex1, vertex2 = edge
        adjacency_list[vertex1].add(vertex2)
        if not digraph:
            adjacency_list[vertex2].add(vertex1)

    return adjacency_list

def add_vertex(vertex_number: int, neighbours: set[int], 
               graph: dict[int, set[int]], *, digraph: bool = False
               ) -> dict[int, set[int]]:
    graph.setdefault(vertex_number, set())
    current_neighbours = graph[vertex_number]
    new_neighbours = current_neighbours.union(neighbours)
    graph[vertex_number] = new_neighbours
    if not digraph:
        for n in new_neighbours:
            graph[n] = graph.setdefault(n, set()).union({vertex_number})
    return graph

def drop_vertex(vertex_number: int, 
                graph: dict[int, set[int]]) -> dict[int, set[int]]:
    if vertex_number in graph:
        for key in graph:
            graph[key].discard(vertex_number)
        graph.pop(vertex_number)
    return graph

def get_edges(graph: dict[int, set[int]], *, digraph: bool = False) -> tuple[int, list[tuple[int, int]]]:
    size = len(graph)
    unique_edges = set()

    for vertex, neighbors in graph.items():
        for neighbor in neighbors:
            edge = tuple(sorted((vertex, neighbor)) if not digraph else (vertex, neighbor))
            unique_edges.add(edge)
            
    return (size, list(unique_edges))

def from_file(filename: str) -> dict[int, set[int]]: 
    with open(filename, 'r') as f:
        l = {int(line.split('.')[0]) - 1 : 
             {int(num) - 1 for num in line.split('.')[1].split()} for line in f}

    return l
