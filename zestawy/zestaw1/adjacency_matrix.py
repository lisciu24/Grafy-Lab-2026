class adjacency_matrix:
    @staticmethod
    def create_matrix(vertices: int, edges: list[tuple[int, int]])->list[list[int]]:
        if vertices < 0:
            raise ValueError("Number of vertices cannot be a negative number.")
        if len(edges) > vertices * (vertices - 1) / 2:
            raise ValueError("Number of edges out of possible range.")
        for edge in edges:
            if edge[0] > vertices - 1:
                raise ValueError(f"Edge ({edge[0]}, {edge[1]}) is incorrect. Vertex with label {edge[0]} does not exist.")
            if edge[1] > vertices - 1:
                raise ValueError(f"Edge ({edge[0]}, {edge[1]}) is incorrect. Vertex with label {edge[1]} does not exist.")
        matrix = [[0] * vertices for _ in range(vertices)]
        
        for edge in edges:
            u, v = edge
            matrix[u][v] = 1
            matrix[v][u] = 1
        
        return matrix

    @staticmethod
    def add_vertex(neighbours: list[int], graph: list[list[int]]) -> list[list[int]]:
        new_vertex = len(graph)
        
        new_row = []

        for i in range(new_vertex):
            if i in neighbours:
                graph[i].append(1)
                new_row.append(1)
            else:
                graph[i].append(0)
                new_row.append(0)

        new_row.append(0)

        graph.append(new_row)

        return graph

    @staticmethod
    def drop_vertex(vertex_number: int, graph: list[list[int]]) -> list[list[int]]:
        graph.pop(vertex_number)
        
        for row in graph:
            row.pop(vertex_number)
            
        return graph

    @staticmethod
    def get_edges(graph: list[list[int]]) -> (int, list[tuple[int, int]]):
        size = len(graph)
        edges = []
        for row in range(size):
            for col in range(row, size):
                if graph[row][col] == 1:
                    edges.append((row, col))
        return (size, edges)