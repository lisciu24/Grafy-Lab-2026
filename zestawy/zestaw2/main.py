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

import common.incidence_matrix as incidence_matrix
from common.circle_graph import draw_circle_graph
from common.generate_random_graph import generate_random_graph
from collections import Counter
import random
import time


def check_if_graphical(sequence: list[int]) -> bool:
    n = len(sequence)    
    s = sequence
    s = sorted(s, reverse=True)
    while True:
        if all(x == 0 for x in s):
            return True
        if s[0] >= n or not all(x >= 0 for x in s):
            return False

        for i in range(1, s[0] + 1):
            s[i] -= 1
        s[0] = 0
        s = sorted(s, reverse=True)


def generate_graph_from_sequence(sequence: list[int]):
    s = sequence
    v = len(sequence)
    e = []
    finished = False
    id_s = [[i, s[i]] for i in range(len(s))]
    id_s = sorted(id_s, key=lambda x: x[1], reverse=True)

    while not finished:
        for i in range(1, id_s[0][1] + 1):
            id_s[i][1] -= 1
            e.append((id_s[0][0], id_s[i][0]))
        id_s[0][1] = 0
        id_s = sorted(id_s, key=lambda x: x[1], reverse=True)

        if all(x[1] == 0 for x in id_s):
            finished = True

    return v, e


def randomize_graph(edges, n):
    random.seed(time.time())
    for _ in range(n):
        index1 = random.randrange(0, len(edges))
        a, b = edges[index1]
        invalid = True
        while invalid:
            index2 = random.randrange(0, len(edges) - 1)
            c, d = edges[index2]
            if index2 != index1 and c not in (a, b) and d not in (a, b):
                if (a, d) not in edges and (d, a) not in edges and (b, c) not in edges and (c, b) not in edges: 
                    invalid = False

        edges[index1] = (a, d)
        edges[index2] = (b, c)



def components_R(nr, v, edges, comp, size):
    neighbors = [u for u in range(size) if (u, v) in edges or (v, u) in edges]
    for u in neighbors:
        if comp[u] == -1:
            comp[u] = nr
            components_R(nr, u, edges, comp, size)



def components(size, edges):
    nr = 0
    comp = [-1] * size
    for v in range(size):
        if comp[v] == -1:
            nr += 1
            comp[v] = nr
            components_R(nr, v, edges, comp, size)

    return comp


def biggest_component(size, edges):
    comp = components(size, edges)
    count = Counter(comp)
    biggest_nr = max(count, key=count.get)
    members = [v for v in range(size) if comp[v] == biggest_nr]
    return members


def random_k_regular_graph(n, k):
    if n <= k or (k%2 == 1 and n%2 == 1):
        print("invalid input")
        return None
    sequence = [k] * n
    v, e = generate_graph_from_sequence(sequence)
    randomize_graph(e, n)

    return v, e





def main():

    #TASK 1
    print("===task 1 - graphical sequence===")
    sequences = [
        [4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2],
        [4, 4, 3, 1, 2],
    ]
    for sequence in sequences:
        print(f'\nsequence: {sequence}')
        if not check_if_graphical(sequence):
            print("sequence is not graphical - skipping")
            continue
        vertices, edges = generate_graph_from_sequence(sequence)
        graph = incidence_matrix.create_matrix(vertices, edges)
        for line in graph:
            print(line)
        draw_circle_graph(vertices, edges)


    #TASK 2
    print("\n\n===task 2 - randomize graph")
    sequence = [4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2]
    vertices, edges = generate_graph_from_sequence(sequence)
    draw_circle_graph(vertices, edges)
    print("edges before randomization: ", edges)
    randomize_graph(edges, 10)
    draw_circle_graph(vertices, edges)
    print("edges after randomization: ", edges)


    #TASK 3
    print("\n\n===task 3 - find biggest graph component")
    vertices, edges = generate_random_graph(20, 10)
    members = biggest_component(vertices, edges)
    print("biggest component members: ", members)
    draw_circle_graph(vertices, edges)  #does not draw vertices with no neighbors



    #TASK 4




    #TASK 5
    print("\n\n===task 5 - generate random k-regular graph")
    v, e = random_k_regular_graph(10, 3)
    draw_circle_graph(v, e)


    #TASK 6
    
    




if __name__ == "__main__":
    main()