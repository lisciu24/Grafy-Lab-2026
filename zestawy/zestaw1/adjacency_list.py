class adjacency_list:
    @staticmethod
    def create_list(vertices: int, edges: list[tuple[int, int]]) -> dict(int, set[int]):
        if vertices < 0:
            raise ValueError("Number of vertices cannot be a negative number.")
        if len(edges) > vertices * (vertices - 1) / 2:
            raise ValueError("Number of edges out of possible range.")
        for edge in edges:
            if edge[0] > vertices - 1:
                raise ValueError(f"Edge ({edge[0]}, {edge[1]}) is incorrect. Vertex with label {edge[0]} does not exist.")
            if edge[1] > vertices - 1:
                raise ValueError(f"Edge ({edge[0]}, {edge[1]}) is incorrect. Vertex with label {edge[1]} does not exist.")
        
        adjacency_list = dict()
        
        for i in range(vertices):
            adjacency_list[i] = set()

        for edge in edges:
            vertex1, vertex2 = edge
            adjacency_list[vertex1].add(vertex2)
            adjacency_list[vertex2].add(vertex1)

        return adjacency_list

    @staticmethod
    def add_vertex(vertex_number: int, neighbours: set[int], graph: dict(int, set[int])) -> dict(int, set[int]):
        graph.setdefault(vertex_number, set())
        current_neighbours = graph[vertex_number]
        new_neighbours = current_neighbours.union(neighbours)
        graph[vertex_number] = new_neighbours
        for n in new_neighbours:
            graph[n] = graph.setdefault(n, set()).union({vertex_number})
        return graph

    @staticmethod
    def drop_vertex(vertex_number: int, graph: dict(int, set[int])) -> dict(int, set[int]):
        if vertex_number in graph:
            for key in graph[vertex_number]:
                graph[key].discard(vertex_number)
            graph.pop(vertex_number)
        return graph

    @staticmethod
    def get_edges(graph: dict(int, set[int])) -> (int, list[tuple[int, int]]):
        size = len(graph)
        unique_edges = set()
    
        for vertex, neighbors in graph.items():
            for neighbor in neighbors:
                edge = tuple(sorted((vertex, neighbor)))
                unique_edges.add(edge)
                
        return (size, list(unique_edges))
