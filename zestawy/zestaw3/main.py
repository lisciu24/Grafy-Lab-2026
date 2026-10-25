# Zestaw 3 (Grafy i ich zastosowania)
# 1. Korzystając z programów z poprzednich zestawów wygenerować spójny
#    graf losowy. Przypisać każdej krawędzi tego grafu losową wagę będącą
#    liczbą naturalną z zakresu 1 do 10.
#
# 2. Zaimplementować algorytm Dijkstry do znajdowania najkrótszych ścieżek od 
#    zadanego wierzchołka do pozostałych wierzchołków i zastosować
#    go do grafu z zadania pierwszego, w którym wagi krawędzi interpretowane 
#    są jako odległości wierzchołków. Wypisać wszystkie najkrótsze
#    ścieżki od danego wierzchołka i ich długości.
#
# 3. Wyznaczyć macierz odległości miedzy wszystkimi parami wierzchołków
#    na tym grafie.
#
# 4. Wyznaczyć centrum grafu, to znaczy wierzchołek, którego suma odległości 
#    do pozostałych wierzchołków jest minimalna. Wyznaczyć centrum minimax, 
#    to znaczy wierzchołek, którego odległość do najdalszego
#    wierzchołka jest minimalna.
#
# 5. Wyznaczyć minimalne drzewo rozpinające (algorytm Prima lub Kruskala).

from common import adjacency_list, adjacency_matrix, conversions
from common import dijkstra, util, spanning_tree

def main():
    graph = conversions.adjacency_list_to_adjacency_matrix(
        adjacency_list.from_file("zestawy/zestaw3/input_graph.txt"))
    weights = adjacency_matrix.from_file("zestawy/zestaw3/input_weights.txt")

    d, p = dijkstra.dijkstra(graph, weights, 0)

    print("START: s = 0")
    for end in range(len(d)):
        dijkstra.print_path(d, p, 0, end)
    print()

    dm = dijkstra.distance_matrix(graph, weights)
    util.print_matrix(dm)
    print()

    i, d = dijkstra.get_graph_center(dm)
    print(f"Centrum = {i} (suma odleglosci: {d})")
    i, d = dijkstra.get_graph_minmax_center(dm)
    print(f"Centrum minimax = {i} (odleglosc od najdalszego: {d})")

    print()

    print(spanning_tree.mst_prim(graph, weights))
    print(spanning_tree.mst_kruskal(graph, weights))

if __name__ == "__main__":
    main()
