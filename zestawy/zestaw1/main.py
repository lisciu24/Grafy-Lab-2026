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
def main():

    x = adjacency_list.list()
    V2 = 4
    edges2 = [[0, 1], [1, 2], [1, 3], [2, 3], [3, 0]]
    graph = x.create_list(V2, edges2)
    print(graph)
    graph = x.add_vertex(4, {2, 3}, graph)
    print(graph)


if __name__ == "__main__":
    main()