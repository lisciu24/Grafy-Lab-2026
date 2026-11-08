# Zestaw 2 (Grafy i ich zastosowania)
# 1. Napisać program do sprawdzania, czy dana sekwencja liczb naturalnych
#    jest ciągiem graficznym, i do konstruowania grafu prostego o stopniach
#    wierzchołków zadanych przez ciąg graficzny.
#
# 2. Napisać program do randomizacji grafów prostych o zadanych stopniach wierzchołków. 
#    Do tego celu wielokrotnie powtórzyć operację zamieniającą losowo wybraną parę krawędzi: 
#    ab i cd na parę ad i bc.
#
# 3. Napisać program do znajdowania największej spójnej składowej na grafie.
#
# 4. Używając powyższych programów napisać program do tworzenia losowego 
#    grafu eulerowskiego i znajdowania na nim cyklu Eulera.
#
# 5. Napisać program do generowania losowych grafów k-regularnych.
#
# 6. Napisać program do sprawdzania (dla małych grafów), czy graf jest
#    hamiltonowski.

from common.util import draw_graph
from common import adjacency_matrix
from common import generate_graph, components, cycles
from common import user_input

def main():

    #TASK 1
    print("===task 1 - graphical sequence===")
    input_result = user_input.get_input([
        user_input.Field("seq", "Sekwencja", "list", item_type="int", required=False)
    ])

    seq = input_result["seq"]
    graphical_seq = generate_graph.check_if_graphical(seq) if seq else False
    graph_seq = generate_graph.generate_graph_from_sequence(seq) if graphical_seq else None
    sequences = [
        [4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2],
        [4, 4, 3, 1, 2],
        [],
        [1, 1, 1],
        [1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [4, 4, 3, 3, 3],
        [3, 3, 3, 3]
    ] if not seq else [seq]

    for sequence in sequences:
        print(f'\nsequence: {sequence}')
        if not generate_graph.check_if_graphical(sequence):
            print("sequence is not graphical - skipping")
            continue
        vertices, edges = generate_graph.generate_graph_from_sequence(sequence)
        graph = adjacency_matrix.create_matrix(vertices, edges)
        for line in graph:
            print(line)
        draw_graph(vertices, edges)


    #TASK 2
    print("\n\n===task 2 - randomize graph")
    sequence = [4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2] if not graphical_seq else seq
    #sequence = [3, 3, 2, 2]
    vertices, edges = generate_graph.generate_graph_from_sequence(sequence)
    draw_graph(vertices, edges)
    print("edges before randomization: ", edges)
    generate_graph.randomize_graph(edges, 5)
    draw_graph(vertices, edges)
    print("edges after randomization: ", edges)


    #TASK 3
    print("\n\n===task 3 - find biggest graph component")
    vertices, edges = generate_graph.generate_random_graph(10, 6) if not graph_seq else graph_seq
    #vertices, edges = generate_graph.generate_graph_from_sequence([2,2,2,1,1,1,1,0,0])
    #vertices, edges = generate_graph.generate_graph_from_sequence([0, 0, 0])
    #vertices, edges = generate_graph.generate_graph_from_sequence([])
    comp = components.components(vertices, edges)
    members = components.biggest_component(comp)
    print("biggest component members: ", members)
    draw_graph(vertices, edges)


    #TASK 4
    print("\n\n===task 4 - generate random Eulerian graph and find Eulerian cycle")
    input_result = user_input.get_input([
        user_input.Field("n", "Liczba wierzchołków", "int", default=5)
    ])
    n = input_result["n"]
    v, e = generate_graph.generate_eulerian(n)
    cycle = cycles.find_euler_cycle(v, e)
    print("cycle: ", cycle)
    draw_graph(v, e)


    #TASK 5
    print("\n\n===task 5 - generate random k-regular graph")
    input_result = user_input.get_input([
        user_input.Field("n", "Liczba wierzchołków", "int", default=6),
        user_input.Field("k", "Stopień wierzchołków", "int", default=2)
    ])
    n = input_result["n"]
    k = input_result["k"]
    v, e = generate_graph.random_k_regular_graph(n, k)
    # v, e = generate_graph.random_k_regular_graph(0, 0)
    draw_graph(v, e)


    #TASK 6
    print("\n\n===task 6 - find hamilton")
    cycle = cycles.find_hamilton(v, e)
    if cycle:
        print("cycle: ", cycle)
    else:
        print("no cycle found")
    # draw_circle_graph(v, e)
    

if __name__ == "__main__":
    main()