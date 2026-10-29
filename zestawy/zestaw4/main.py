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
from common.generate_random_graph import generate_random_graph, generate_random_weights
from common import kosaraju, shortest_path

def main():
    graph = conversions.adjacency_list_to_adjacency_matrix(adjacency_list.from_file("zestawy/zestaw4/input_graph.txt"), digraph=True)
    # graph = adjacency_matrix.create_matrix(*generate_random_graph(10, edges_prob=0.3, digraph=True), digraph=True)
    util.print_matrix(graph)
    weights = adjacency_matrix.from_file("zestawy/zestaw4/input_weights.txt")

    nr, comp = kosaraju.kosaraju(graph)
    d : dict[int, list[int]] = {}
    for v, n in enumerate(comp):
        d.setdefault(n, []).append(v)

    biggest_comp = max((len(d[n]), d[n]) for n in d)[1]
    for v in range(len(graph) - 1, -1, -1):
        if v not in biggest_comp:
            graph = adjacency_matrix.drop_vertex(v, graph)
     
    # weights = generate_random_weights(graph, -5, 10)

    good, dbf, pbf = shortest_path.bellman_ford(graph, weights, 0)
    if good:
        print("START: s = 0")
        for end in range(len(dbf)):
            util.print_path(dbf, pbf, 0, end)
    else:
        print("not good")
    print()

    m = shortest_path.distance_matrix(graph, weights, shortest_path.bellman_ford)
    util.print_matrix(m)
    print()

    m = shortest_path.johnson(graph, weights)
    util.print_matrix(m)
    print()

if __name__ == "__main__":
    main()