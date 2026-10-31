# Zestaw 6 (Grafy i ich zastosowania)
# 1. Zaimplementować algorytm PageRank dla digrafu metodą polegającą na przechodzeniu od wierzchołka do sąsiedniego
# wierzchołka za pomocą błądzenia przypadkowego.
# 
# 2. Zaimplementować algorytm PageRank dla digrafu metodą iteracji wektora obsadzeń pt.
#
# 3. Zaimplementować algorytm do wyszukiwania możliwie najkrótszej zamkniętej
# drogi przechodzącej przez wszystkie zadane wierzchołki rozrzucone na planszy
# kwadratowej. Zastosować metodę symulowanego wyżarzania opartą o łańcuch
# Markowa, którego pojedyncze kroki są wykonywane jako operacje 2-opt zgodnie
# z algorytmem Metropolisa-Hastingsa.

from common.directed_graph import draw_digraph
import common.adjacency_list as adjacency_list
from common.generate_random_graph import generate_random_graph
from common.page_rank import page_rank_random, page_rank_vector
from common.conversions import adjacency_list_to_adjacency_matrix
def main():
    # graph = adjacency_list.create_list(*generate_random_graph(10, edges_prob=0.2, digraph=True), digraph=True)
    graph = adjacency_list.from_file("zestawy/zestaw6/input_graph.txt")
    rank = page_rank_random(graph=graph, N=1000000, d=0.15)
    dsc = {k: v for k, v in sorted(rank.items(), key=lambda item: item[1], reverse=True)}
    print(dsc)
    rank = page_rank_vector(graph=adjacency_list_to_adjacency_matrix(graph, digraph=True), d=0.15, tol=1e-4)
    dsc = {k: v for k, v in sorted(rank.items(), key=lambda item: item[1], reverse=True)}
    print(dsc)
    vertices, edges = adjacency_list.get_edges(graph=graph, digraph=True)
    draw_digraph(vertices=vertices, edges=edges)

if __name__ == "__main__":
    main()