# Zestaw 1 (Grafy i ich zastosowania)
# 1. Napisać program kodujący grafy proste za pomocą macierzy sąsiedztwa, 
#    macierzy incydencji i list sąsiędztwa. Stworzyć moduł do zmiany
#    danego kodowania na pozostałe.
#
# 2. Napisać program do wizualizacji grafów prostych używający reprezentacji, 
#    w której wierzchołki grafu są równomiernie rozłożone na okręgu.
#
# 3. Napisać program do generowania grafów losowych G(n, l) oraz G(n, p).


import adjacency_matrix
import adjacency_list
import incidence_matrix
from circle_graph import draw_circle_graph
import generate_random_graph
import conversions
def main():
    print("Adjacency list")
    V1 = 4
    edges1 = [[0, 1], [1, 2], [1, 3], [2, 3], [3, 0]]
    graph = adjacency_list.adjacency_list.create_list(V1, edges1)
    print(graph)
    graph2 = conversions.adjacency_list_to_adjacency_matrix(graph)
    for line in graph2:
        print(line)
    graph3 = conversions.adjacency_list_to_incidence_matrix(graph)
    for line in graph3:
        print(line)
    graph = adjacency_list.adjacency_list.add_vertex(4, {2, 3}, graph)
    print(graph)


    print("Adjacency matrix")
    V2 = 4
    edges2 = [[0, 1], [1, 2], [1, 3], [2, 3], [3, 0]]
    graph = adjacency_matrix.adjacency_matrix.create_matrix(V2, edges2)
    for line in graph:
        print(line)
    graph2 = conversions.adjacency_matrix_to_adjacency_list(graph)
    print(graph2)    
    graph3 = conversions.adjacency_matrix_to_incidence_matrix(graph)
    for line in graph3:
        print(line)
    graph = adjacency_matrix.adjacency_matrix.add_vertex([2, 3], graph)
    print(graph)
    graph = adjacency_matrix.adjacency_matrix.drop_vertex(2, graph)
    print(graph)

    
    print("Incidence matrix")
    V3 = 4
    edges3 = [[0, 1], [1, 2], [1, 3], [2, 3], [3, 0]]
    graph = incidence_matrix.incidence_matrix.create_matrix(V3, edges3)
    for line in graph:
        print(line)
    graph2 = conversions.incidence_matrix_to_adjacency_matrix(graph)
    for line in graph2:
        print(line)
    graph3 = conversions.incidence_matrix_to_adjacency_list(graph)
    print(graph3)
    graph = incidence_matrix.incidence_matrix.add_vertex([2, 3], graph)
    for line in graph:
        print(line)
    graph = incidence_matrix.incidence_matrix.drop_vertex(0, graph)
    for line in graph:
        print(line)

    size, edges = generate_random_graph.generate_random_graph(20, edges = 190)
    print(len(edges))
    draw_circle_graph(size, edges)

if __name__ == "__main__":
    main()