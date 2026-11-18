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

from common import adjacency_list, adjacency_matrix, components
from common import util, conversions
from common.generate_graph import generate_random_graph, generate_random_weights
from common import shortest_path

GENERATE_GRAPH = True
GENERATE_WEIGHTS = True

def main():
    graph = adjacency_matrix.create_matrix(*generate_random_graph(10, edges_prob=0.2, digraph=True), digraph=True)

    if not GENERATE_GRAPH:
        graph = conversions.adjacency_list_to_adjacency_matrix(adjacency_list.from_file("zestawy/zestaw4/input_graph.txt"), digraph=True)

    size, edges = adjacency_matrix.get_edges(graph, digraph=True)
    util.print_matrix(graph)
    util.draw_graph(size, edges, digraph=True)

    comp = components.kosaraju(graph)
    print(comp)
    util.draw_graph(size, edges, components=comp, digraph=True)
    biggest_comp = components.biggest_component(comp)
    print(biggest_comp)
    for v in range(len(graph) - 1, -1, -1):
        if v not in biggest_comp:
            graph = adjacency_matrix.drop_vertex(v, graph)

    size, edges = adjacency_matrix.get_edges(graph, digraph=True)
    util.print_matrix(graph)
    util.draw_graph(size, edges, digraph=True)
     
    weights = generate_random_weights(graph, -2, 10, digraph=True)
    if not GENERATE_GRAPH and not GENERATE_WEIGHTS:
        weights = adjacency_matrix.from_file("zestawy/zestaw4/input_weights.txt")

    good, dbf, pbf = shortest_path.bellman_ford(graph, weights, 0)
    if good:
        print("START: s = 0")
        for end in range(len(dbf)):
            util.print_path(dbf, pbf, 0, end)
    else:
        print("not good")
        return
    print()

    m = shortest_path.distance_matrix(graph, weights, shortest_path.bellman_ford)
    util.print_matrix(m)

    m = shortest_path.johnson(graph, weights)
    util.print_matrix(m)

if __name__ == "__main__":
    main()