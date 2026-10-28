# Zestaw 4 (Grafy i ich zastosowania)
# 1. Napisać program do kodowania grafów skierowanych (digrafów) i do
#    generowania losowych digrafów z zespołu G(n, p).
#
# 2. Zaimplementować algorytm Kosaraju do szukania silnie spójnych składowych 
#    na digrafie i zastosować go do digrafu losowego.
#
# 3. Wykorzystując algorytmy z powyższych punktów wygenerować losowy
#    silnie spójny digraf. Łukom tego digrafu przypisać losowe wagi będące
#    liczbami całkowitymi z zakresu [−5, 10]. Zaimplementować algorytm
#    Bellmana-Forda do znajdowania najkrótszych ścieżek od danego wierzchołka.
#
# 4. Zaimplementować algorytm Johnsona do szukania odegłości pomiędzy
#    wszystkimi parami wierzchołków na ważonym grafie skierowanym.

from common import adjacency_list, adjacency_matrix
from common import util, conversions

def main():
    graph = conversions.adjacency_list_to_adjacency_matrix(adjacency_list.from_file("zestawy/zestaw4/input_graph.txt"), digraph=True)
    util.print_matrix(graph)
    weights = adjacency_matrix.from_file("zestawy/zestaw4/input_weights.txt")

    util.draw_graph(graph, weights, digraph=True)
    

if __name__ == "__main__":
    main()