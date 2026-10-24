def create_matrix(vertices: int, edges: list[tuple[int, int]])->list[list[int]]:
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

    for v in range(vertices):
        for edge in enumerate(edges):
            if v in edge[1]:
                matrix[v][edge[0]] = 1

    return matrix

def add_vertex(neighbours: list[int], graph: list[list[int]]) -> list[list[int]]:
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
    new_row.extend([1] * len(neighbours))
    graph.append(new_row)
    
    return graph

def drop_vertex(vertex_number: int, graph: list[list[int]]) -> list[list[int]]:
    trash_row = graph[vertex_number]
    neighbours_columns = [i for i in range(len(trash_row)) if trash_row[i] == 1]
    graph.pop(vertex_number)
    for row in graph:
        for column in reversed(neighbours_columns):
            row.pop(column)
    return graph

def get_edges(graph: list[list[int]]) -> tuple[int, list[tuple[int, int]]]:
    size = len(graph)
    col_size = len(graph[0])
    edges = []
    for col in range(col_size):
        edge = []
        for row in range(size):
            if graph[row][col] == 1:
                edge.append(row)
        if len(edge) == 2:
            edges.append((edge[0], edge[1]))
    return size, edges