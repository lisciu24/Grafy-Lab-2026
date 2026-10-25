from common import adjacency_matrix, adjacency_list, incidence_matrix
def adjacency_list_to_adjacency_matrix(graph: dict[int, set[int]], *, digraph: bool = False)->list[list[int]]:
    size, edges = adjacency_list.get_edges(graph, digraph=digraph)
    return adjacency_matrix.create_matrix(size, edges, digraph=digraph)

def adjacency_list_to_incidence_matrix(graph: dict[int, set[int]], *, digraph: bool = False)->list[list[int]]:
    size, edges = adjacency_list.get_edges(graph, digraph=digraph)
    return incidence_matrix.create_matrix(size, edges, digraph=digraph)

def adjacency_matrix_to_adjacency_list(graph: list[list[int]], *, digraph: bool = False)->dict[int, set[int]]:
    size, edges = adjacency_matrix.get_edges(graph, digraph=digraph)
    return adjacency_list.create_list(size, edges, digraph=digraph)

def adjacency_matrix_to_incidence_matrix(graph: list[list[int]], *, digraph: bool = False)->list[list[int]]:
    size, edges = adjacency_matrix.get_edges(graph, digraph=digraph)
    return incidence_matrix.create_matrix(size, edges, digraph=digraph)

def incidence_matrix_to_adjacency_list(graph: list[list[int]], *, digraph: bool = False)->dict[int, set[int]]:
    size, edges = incidence_matrix.get_edges(graph, digraph=digraph)
    return adjacency_list.create_list(size, edges, digraph=digraph)

def incidence_matrix_to_adjacency_matrix(graph: list[list[int]], *, digraph: bool = False)->list[list[int]]:
    size, edges = incidence_matrix.get_edges(graph, digraph=digraph)
    return adjacency_matrix.create_matrix(size, edges, digraph=digraph)