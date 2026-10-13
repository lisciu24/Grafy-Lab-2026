class list:
    def create_list(self, vertices: int, edges: list[tuple[int, int]]) -> dict(int, set[int]):
        adjacency_list = dict()

        for i in range(vertices):
            adjacency_list[i] = set()

        for edge in edges:
            vertex1, vertex2 = edge
            adjacency_list[vertex1].add(vertex2)

        return adjacency_list

    def add_vertex(self, vertex_number: int, neighbours: set[int], graph: dict(int, set[int])) -> dict(int, set[int]):
        graph.setdefault(vertex_number, set())
        current_neighbours = graph[vertex_number]
        new_neighbours = current_neighbours.union(neighbours)
        graph[vertex_number] = new_neighbours
        for n in new_neighbours:
            graph[n] = graph.setdefault(n, set()).union({vertex_number})
        return graph

    def drop_vertex(self, vertex_number: int, graph: dict(int, set[int])) -> dict(int, set[int]):
        if vertex_number in graph:
            for key in graph[vertex_number]:
                graph[key].discard(vertex_number)
            graph.pop(vertex_number)
        return graph

    def to_adjacency_matrix(graph: dict(int, list[int])):
        pass

    def to_incidence_matrix(graph: dict(int, list[int])):
        pass
