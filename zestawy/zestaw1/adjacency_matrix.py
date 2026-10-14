class matrix:
    def create_matrix(self, vertices: int, edges: list[tuple[int, int]])->list[list[int]]:
        matrix = [[0] * vertices for _ in range(vertices)]
        
        for edge in edges:
            u, v = edge
            matrix[u][v] = 1
            matrix[v][u] = 1
        
        return matrix

    def add_vertex(self, neighbours: list[int], graph: list[list[int]]) -> list[list[int]]:
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

    def drop_vertex(self, vertex_number: int, graph: list[list[int]]) -> list[list[int]]:
        graph.pop(vertex_number)
        
        for row in graph:
            row.pop(vertex_number)
            
        return graph


        
    def to_adjacency_list(graph: dict(int, list[int])):
        pass

    def to_incidence_matrix(graph: dict(int, list[int])):
        pass