# Zestaw 1 (Grafy i ich zastosowania)
# 1. Napisać program kodujący grafy proste za pomocą macierzy sąsiedztwa, 
#    macierzy incydencji i list sąsiędztwa. Stworzyć moduł do zmiany
#    danego kodowania na pozostałe.
#
# 2. Napisać program do wizualizacji grafów prostych używający reprezentacji, 
#    w której wierzchołki grafu są równomiernie rozłożone na okręgu.
#
# 3. Napisać program do generowania grafów losowych G(n, l) oraz G(n, p).


import common.adjacency_matrix as adjacency_matrix
import common.adjacency_list as adjacency_list
import common.incidence_matrix as incidence_matrix
from common.circle_graph import draw_circle_graph
import common.generate_graph as generate_graph
import common.conversions as conversions
from common import user_input, util

conversions_input_config = [
    user_input.Field(
        key="format", 
        label="Wybierz formatowanie", 
        type="choice",
        options=[
            user_input.Option("am", "adjacency matrix"), 
            user_input.Option("al", "adjacency list"), 
            user_input.Option("im", "incidence matrix")
        ]
    ),
    user_input.Field(
        key="filename",
        label="Nazwa pliku",
        type="str",
    )
]

generation_input_config = [
    user_input.Field(
        key="gen_method",
        label="Wybierz sposób generowania grafu",
        type="choice",
        options=[
            user_input.Option("prob", "G(n, p)", fields=[
                user_input.Field("n", "Liczba wierzchołków", "int"),
                user_input.Field("p", "Prawdobodobieństwo krawędzi", "float")
            ]),
            user_input.Option("edge", "G(n, l)", fields=[
                user_input.Field("n", "Liczba wierzchołków", "int"),
                user_input.Field("l", "Liczba krawędzi", "int")
            ])
        ]
    )
]


def main():
    config_result = user_input.get_input(conversions_input_config)
    input_format = config_result["format"]
    filename = config_result["filename"]

    if input_format == "al":
        graph = adjacency_list.from_file(filename)
        print("Wczytano z listy sąsiedztwa")
        util.print_list(graph)
        print("Macierz sąsiedztwa")
        print(conversions.adjacency_list_to_adjacency_matrix(graph))
        print("Macierz incidencji")
        print(conversions.adjacency_list_to_incidence_matrix(graph))
    elif input_format == "am":
        graph = adjacency_matrix.from_file(filename)
        print("Wczytano z macierzy sąsiedztwa")
        util.print_matrix(graph)
        print("Lista sąsiedztwa")
        util.print_list(conversions.adjacency_matrix_to_adjacency_list(graph))
        print("Macierz incidencji")
        util.print_matrix(conversions.adjacency_matrix_to_incidence_matrix(graph))
    elif input_format == "im":
        graph = incidence_matrix.from_file(filename)
        print("Wczytano z listy sąsiedztwa")
        util.print_matrix(graph)
        print("Macierz sąsiedztwa")
        util.print_list(conversions.incidence_matrix_to_adjacency_list(graph))
        print("Macierz incidencji")
        util.print_matrix(conversions.incidence_matrix_to_adjacency_matrix(graph))


    config_result = user_input.get_input(generation_input_config)
    method, params = next(iter(config_result["gen_method"].items()))
    size, edges = 0,[]
    if method == "prob":
        size, edges = generate_graph.generate_random_graph(params["n"], edges_prob=params["p"])
        print(size, edges)
    elif method == "edge":
        size, edges = generate_graph.generate_random_graph(params["n"], edges=params["l"])
        print(size, edges)

    draw_circle_graph(size, edges)
    


    return 
    ###################################################################
    # Poniżej jest stary zahardkodowany kod prezentowany na zajęciach #
    ###################################################################
    print("Adjacency list")
    V1 = 4
    edges1 = [(0, 1), (1, 2), (1, 3), (2, 3), (3, 0)]
    graph = adjacency_list.create_list(V1, edges1)
    print(graph)
    graph2 = conversions.adjacency_list_to_adjacency_matrix(graph)
    for line in graph2:
        print(line)
    graph3 = conversions.adjacency_list_to_incidence_matrix(graph)
    for line in graph3:
        print(line)
    graph = adjacency_list.add_vertex(4, {2, 3}, graph)
    print(graph)


    print("Adjacency matrix")
    V2 = 4
    edges2 = [(0, 1), (1, 2), (1, 3), (2, 3), (3, 0)]
    graph = adjacency_matrix.create_matrix(V2, edges2)
    for line in graph:
        print(line)
    graph2 = conversions.adjacency_matrix_to_adjacency_list(graph)
    print(graph2)    
    graph3 = conversions.adjacency_matrix_to_incidence_matrix(graph)
    for line in graph3:
        print(line)
    graph = adjacency_matrix.add_vertex([2, 3], graph)
    print(graph)
    graph = adjacency_matrix.drop_vertex(2, graph)
    print(graph)

    
    print("Incidence matrix")
    V3 = 4
    edges3 = [(0, 1), (1, 2), (1, 3), (2, 3), (3, 0)]
    graph = incidence_matrix.create_matrix(V3, edges3)
    for line in graph:
        print(line)
    graph2 = conversions.incidence_matrix_to_adjacency_matrix(graph)
    for line in graph2:
        print(line)
    graph3 = conversions.incidence_matrix_to_adjacency_list(graph)
    print(graph3)
    graph = incidence_matrix.add_vertex([2, 3], graph)
    for line in graph:
        print(line)
    graph = incidence_matrix.drop_vertex(0, graph)
    for line in graph:
        print(line)

    size, edges = generate_graph.generate_random_graph(20, edges = 190)
    print(len(edges))
    draw_circle_graph(size, edges)

if __name__ == "__main__":
    main()