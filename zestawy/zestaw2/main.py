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

import random
from collections import Counter

from common import incidence_matrix
from common.circle_graph import draw_circle_graph
from common.generate_random_graph import generate_random_graph


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
    if len(edges) < 2: 
        return
        
    for _ in range(n):
        index1 = random.randrange(0, len(edges))
        a, b = edges[index1]
        
        invalid = True
        retries = 0
        while invalid and retries < 50:
            index2 = random.randrange(0, len(edges))
            c, d = edges[index2]
            if (index2 != index1 and c not in (a, b) and d not in (a, b)
                    and (a, d) not in edges and (d, a) not in edges
                    and (b, c) not in edges and (c, b) not in edges):
                invalid = False
            retries += 1
            
        if not invalid:
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


def generate_eulerian(size = 0):
    if not size:
        size = random.randint(3, 10)
    if size < 3:
        print("eulerian graph needs at least 3 vertices")
        return None

    solid = False

    while not solid:
        degrees = [random.randrange(2, size, 2) for _ in range(size)]        
        
        while not check_if_graphical(degrees):
            degrees = [random.randrange(2, size, 2) for _ in range(size)]

        v, e = generate_graph_from_sequence(degrees)
        randomize_graph(e, v)
        members = biggest_component(v, e)
        
        if len(members) == v:
            solid = True
            
    return v, e


def find_euler_cycle(v, e):
    edges = e.copy()
    curr = 0
    cycle = [curr]

    while edges:
        neighbor_edges = [edge for edge in edges if curr in edge]

        for edge in neighbor_edges:
            nxt = edge[1] if edge[0] == curr else edge[0]

            if len(neighbor_edges) == 1: # only possibility - need to go this way
                edges.remove(edge)
                curr = nxt
                cycle.append(curr)
                break

            comp_before = max(components(v, edges))
            edges_without = [x for x in edges if x != edge]
            comp_after = max(components(v, edges_without))

            if comp_after <= comp_before: # not a bridge - can go this way
                edges.remove(edge)
                curr = nxt
                cycle.append(curr)
                break

    return cycle


def find_hamilton(v, e):
    adj = {i: [] for i in range(v)}
    for a, b in e:
        adj[a].append(b)
        adj[b].append(a)

    path = [0]

    def backtrack(curr):
        if len(path) == v:
            return 0 in adj[curr] # is it a cycle?
                
        for neighbor in adj[curr]:
            if neighbor not in path:
                path.append(neighbor) # try this new path
                
                if backtrack(neighbor): # if true - hamilton found
                    return True
                    
                path.pop() # otherwise pop - backtracking

        return False

    if backtrack(0): #starting backtracking ad vertex 0. if returns true - hamilton found
        path.append(0)  
        return path
    else:
        return None     
    
    



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
    vertices, edges = generate_random_graph(10, 6)
    members = biggest_component(vertices, edges)
    print("biggest component members: ", members)
    draw_circle_graph(vertices, edges)


    #TASK 4
    print("\n\n===task 4 - generate random Eulerian graph and find Eulerian cycle")
    v, e = generate_eulerian(8)
    cycle = find_euler_cycle(v, e)
    print("cycle: ", cycle)
    draw_circle_graph(v, e)


    #TASK 5
    print("\n\n===task 5 - generate random k-regular graph")
    v, e = random_k_regular_graph(10, 3)
    draw_circle_graph(v, e)


    #TASK 6
    print("\n\n===task 6 - find hamilton")
    cycle = find_hamilton(v, e)
    if cycle:
        print("cycle: ", cycle)
    else:
        print("no cycle found")
    draw_circle_graph(v, e)
    
    
    


if __name__ == "__main__":
    main()