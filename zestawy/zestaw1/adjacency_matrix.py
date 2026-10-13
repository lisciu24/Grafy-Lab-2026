class matrix:
    def create_matrix(self, vertices: int, edges: list[tuple[int, int]])->list[list[int]]:
        matrix = [[0] * vertices for _ in range(vertices)]
        
        for edge in edges:
            u, v = edge
            matrix[u][v] = 1
            matrix[v][u] = 1
        
        return matrix

    def add_vertex(self, vertex_number: int, neighbours: set[int], graph: dict(int, set[int])) -> dict(int, set[int]):
        pass

    def drop_vertex(self, vertex_number: int, graph: dict(int, set[int])) -> dict(int, set[int]):
        pass
        
    def to_adjacency_matrix(graph: dict(int, list[int])):
        pass

    def to_incidence_matrix(graph: dict(int, list[int])):
        pass