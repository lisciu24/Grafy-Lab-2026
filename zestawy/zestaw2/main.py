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
from common.circle_graph import draw_circle_graph
from common import generate_graph, components, cycles

def main():

    #TASK 1
    print("===task 1 - graphical sequence===")
    sequences = [
        [4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2],
        [4, 4, 3, 1, 2],
        [],
        [1, 1, 1],
        [1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [4, 4, 3, 3, 3],
        [3, 3, 3, 3]
    ]
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
    sequence = [4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2]
    #sequence = [3, 3, 2, 2]
    vertices, edges = generate_graph.generate_graph_from_sequence(sequence)
    draw_graph(vertices, edges)
    print("edges before randomization: ", edges)
    generate_graph.randomize_graph(edges, 5)
    draw_graph(vertices, edges)
    print("edges after randomization: ", edges)


    #TASK 3
    print("\n\n===task 3 - find biggest graph component")
    vertices, edges = generate_graph.generate_random_graph(10, 6)
    #vertices, edges = generate_graph.generate_graph_from_sequence([2,2,2,1,1,1,1,0,0])
    #vertices, edges = generate_graph.generate_graph_from_sequence([0, 0, 0])
    #vertices, edges = generate_graph.generate_graph_from_sequence([])
    comp = components.components(vertices, edges)
    members = components.biggest_component(comp)
    print("biggest component members: ", members)
    draw_graph(vertices, edges)


    #TASK 4
    print("\n\n===task 4 - generate random Eulerian graph and find Eulerian cycle")
    v, e = generate_graph.generate_eulerian(5)
    cycle = cycles.find_euler_cycle(v, e)
    print("cycle: ", cycle)
    draw_graph(v, e)


    #TASK 5
    print("\n\n===task 5 - generate random k-regular graph")
    v, e = generate_graph.random_k_regular_graph(6, 2)
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