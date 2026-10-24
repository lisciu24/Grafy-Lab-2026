from adjacency_matrix import adjacency_matrix
from adjacency_list import adjacency_list
from incidence_matrix import incidence_matrix
def adjacency_list_to_adjacency_matrix(graph: dict[int, set[int]])->list[list[int]]:
    size, edges = adjacency_list.get_edges(graph)
    return adjacency_matrix.create_matrix(size, edges)

def adjacency_list_to_incidence_matrix(graph: dict[int, set[int]])->list[list[int]]:
    size, edges = adjacency_list.get_edges(graph)
    return incidence_matrix.create_matrix(size, edges)

def adjacency_matrix_to_adjacency_list(graph: list[list[int]])->dict[int, set[int]]:
    size, edges = adjacency_matrix.get_edges(graph)
    return adjacency_list.create_list(size, edges)

def adjacency_matrix_to_incidence_matrix(graph: list[list[int]])->dict[int, set[int]]:
    size, edges = adjacency_matrix.get_edges(graph)
    return incidence_matrix.create_matrix(size, edges)

def incidence_matrix_to_adjacency_list(graph: list[list[int]])->list[list[int]]:
    size, edges = incidence_matrix.get_edges(graph)
    return adjacency_list.create_list(size, edges)

def incidence_matrix_to_adjacency_matrix(graph: list[list[int]])->list[list[int]]:
    size, edges = incidence_matrix.get_edges(graph)
    return adjacency_matrix.create_matrix(size, edges)