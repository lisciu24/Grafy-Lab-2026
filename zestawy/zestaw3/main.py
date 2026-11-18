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

from common import adjacency_list, adjacency_matrix, conversions, shortest_path
from common import util, spanning_tree, components, generate_graph

GENERATE_GRAPGH = True
GENERATE_WEIGHTS = True

def main():

    size, edges = generate_graph.generate_solid(12, 36)
    graph = adjacency_matrix.create_matrix(size, edges)
    util.print_matrix(graph)

    if not GENERATE_GRAPGH:
        graph = adjacency_matrix.from_file("zestawy/zestaw3/input_graph.txt")

    size, edges = adjacency_matrix.get_edges(graph);
    comp = components.components(size, edges)
    if size != len(components.biggest_component(comp)):
        print("Graf nie jest spójny")
        return

    weights = generate_graph.generate_random_weights(graph, 1, 10)
    if not GENERATE_GRAPGH and not GENERATE_WEIGHTS:
        weights = adjacency_matrix.from_file("zestawy/zestaw3/input_weights.txt")

    print()
    util.print_matrix(weights)

    util.draw_graph(size, edges, weights, circle=False)

    _, d, p = shortest_path.dijkstra(graph, weights, 0)

    print("START: s = 0")
    for end in range(len(d)):
        util.print_path(d, p, 0, end)
    print()

    dm = shortest_path.distance_matrix(graph, weights, shortest_path.dijkstra)
    util.print_matrix(dm)
    print()

    i, d = shortest_path.get_graph_center(dm)
    print(f"Centrum = {i} (suma odleglosci: {d})")
    i, d = shortest_path.get_graph_minmax_center(dm)
    print(f"Centrum minimax = {i} (odleglosc od najdalszego: {d})")

    print()

    mst = spanning_tree.mst_prim(graph, weights)
    print(mst)
    util.draw_graph(size, edges, weights, circle=False, mst=mst[1])
    
    mst = spanning_tree.mst_kruskal(graph, weights)
    print(mst)
    util.draw_graph(size, edges, weights, circle=False, mst=mst[1])

if __name__ == "__main__":
    main()
