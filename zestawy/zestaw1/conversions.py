import adjacency_matrix
import adjacency_list
import incidence_matrix
def adjacency_list_to_adjacency_matrix(graph: dict[int, set[int]])->list[list[int]]:
    size = len(graph)

    unique_edges = set()
    
    for vertex, neighbors in graph.items():
        for neighbor in neighbors:
            edge = tuple(sorted((vertex, neighbor)))
            unique_edges.add(edge)
            
    edges = list(unique_edges)
    return adjacency_matrix.adjacency_matrix.create_matrix(size, edges)
    

def adjacency_list_to_incidence_matrix(graph: dict[int, set[int]])->list[list[int]]:
    size = len(graph)

    unique_edges = set()
    
    for vertex, neighbors in graph.items():
        for neighbor in neighbors:
            edge = tuple(sorted((vertex, neighbor)))
            unique_edges.add(edge)
            
    edges = list(unique_edges)
    return incidence_matrix.incidence_matrix.create_matrix(size, edges)

def adjacency_matrix_to_adjacency_list(graph: list[list[int]])->dict[int, set[int]]:
    size = len(graph)

    edges = []
    for row in range(size):
        for col in range(row, size):
            if graph[row][col] == 1:
                edges.append((row, col))
    return adjacency_list.adjacency_list.create_list(size, edges)

def adjacency_matrix_to_incidence_matrix(graph: list[list[int]])->dict[int, set[int]]:
    size = len(graph)

    edges = []
    for row in range(size):
        for col in range(row, size):
            if graph[row][col] == 1:
                edges.append((row, col))
    return incidence_matrix.incidence_matrix.create_matrix(size, edges)

def incidence_matrix_to_adjacency_list(graph: list[list[int]])->list[list[int]]:

    pass

def incidence_matrix_to_adjacency_matrix(graph: list[list[int]])->list[list[int]]:
    pass