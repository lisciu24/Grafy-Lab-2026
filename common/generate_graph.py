from random import sample, random, randint, randrange
from common import components

def generate_random_graph(vertices: int, edges: int | None = None, edges_prob: float | None = None, *, digraph: bool = False) -> tuple[int, list[tuple[int, int]]]:
    if vertices < 0:
        raise ValueError("Number of vertices cannot be a negative number.")
    if None == edges and None == edges_prob:
        raise ValueError("Specify either edges or edges_prob.")
    if edges != None:
        if edges >= 0 and ((digraph == False and edges <= vertices * (vertices - 1) / 2) or (digraph == True and edges <= vertices * (vertices - 1))):
            g_edges = set()

            while edges > len(g_edges):
                vertex1, vertex2 = sample(range(0, vertices), 2)
                if (vertex1, vertex2) not in g_edges and (digraph or (vertex2, vertex1) not in g_edges):
                    g_edges.add((vertex1, vertex2))
            g_edges = [*g_edges]
            return vertices, g_edges
        else:
            raise ValueError("Value out of possible range.")
    elif edges_prob != None:
        if edges_prob >= 0 or edges_prob <= 1:
            g_edges = set()

            for vertex1 in range(vertices):
                for vertex2 in range(vertices):
                    if vertex1 != vertex2 and (vertex1, vertex2) not in g_edges and (digraph or (vertex2, vertex1) not in g_edges):
                        r_number = random()
                        if r_number < edges_prob:
                            g_edges.add((vertex1, vertex2))
            g_edges = [*g_edges]
            return vertices, g_edges
        else:
            raise ValueError("Value out of possible range.")

    raise Exception("Should not ever get here!")

def generate_random_weights(graph: list[list[int]], min_w: int, max_w: int) -> list[list[int]]:
    return [[randint(min_w, max_w) if graph[v][u] else 0 for u in range(len(graph))] for v in range(len(graph))]

def generate_graph_from_sequence(sequence: list[int]) -> tuple[int, list[tuple[int, int]]]:
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

def random_k_regular_graph(n: int, k: int) -> tuple[int, list[tuple[int, int]]]:
    if n <= k or (k%2 == 1 and n%2 == 1):
        raise ValueError("invalid input")
    sequence = [k] * n
    v, e = generate_graph_from_sequence(sequence)
    randomize_graph(e, n)

    return v, e


def generate_eulerian(size: int = 0) -> tuple[int, list[tuple[int, int]]]:
    if not size:
        size = randint(3, 10)
    if size < 3:
        raise ValueError("eulerian graph needs at least 3 vertices")

    solid = False

    while not solid:
        degrees = [randrange(2, size, 2) for _ in range(size)]        
        
        while not check_if_graphical(degrees):
            degrees = [randrange(2, size, 2) for _ in range(size)]

        v, e = generate_graph_from_sequence(degrees)
        randomize_graph(e, v)
        comp = components.components(v, e)
        members = components.biggest_component(comp)
        
        if len(members) == v:
            return v, e

    raise Exception("Should not ever get here!")
            
def randomize_graph(edges: list[tuple[int,int]], n: int) -> None:
    if len(edges) < 2: 
        return
        
    for _ in range(n):
        index1 = randrange(0, len(edges))
        a, b = edges[index1]
        
        invalid = True
        retries = 0
        while invalid and retries < 50:
            index2 = randrange(0, len(edges))
            c, d = edges[index2]
            if (index2 != index1 and c not in (a, b) and d not in (a, b)
                    and (a, d) not in edges and (d, a) not in edges
                    and (b, c) not in edges and (c, b) not in edges):
                invalid = False
            retries += 1
            
        if not invalid:
            edges[index1] = (a, d) # type: ignore
            edges[index2] = (b, c) # type: ignore

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


