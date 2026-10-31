from random import randint, random, choice
def page_rank_random(graph: dict[int, set[int]], N: int, d: float) -> dict[int, int]:
    v = len(graph)
    selected_v = randint(0, v-1)
    rank = {}
    for i in range(v):
        rank[i] = 0
    for _ in range(N):
        rank[selected_v] += 1
        next_move = random()
        if (1 - d > next_move and graph[selected_v]):
            selected_v = choice(list(graph[selected_v]))
        else:
            selected_v = randint(0, v-1)
    for i in range(v):
        rank[i] /= N
    return rank

def page_rank_vector(graph: list[list[int]], d: float = 0.85, tol: float = 1e-6) -> dict[int, float]:
    v = len(graph)
    if v == 0:
        return {}
        
    P = [[0.0] * v for _ in range(v)]
    for i in range(v):
        row_sum = sum(graph[i])
        if row_sum == 0:
            for j in range(v):
                P[j][i] = 1.0 / v
        else:
            for j in range(v):
                P[j][i] = (1 - d) * (graph[i][j] / row_sum) + (d / v)
                
    rank = [1.0 / v] * v
    while True:
        new_rank = [0.0] * v
        for i in range(v):
            for j in range(v):
                new_rank[i] += P[i][j] * rank[j]
        if all(abs(rank[k] - new_rank[k]) < tol for k in range(v)):
            break
            
        rank = list(new_rank)
        
    return {i: rank[i] for i in range(v)}

