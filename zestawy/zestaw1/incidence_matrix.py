class incidence_matrix:
    
    @staticmethod
    def create_matrix(vertices: int, edges: list[tuple[int, int]])->list[list[int]]:
        matrix = [[0] * len(edges) for _ in range(vertices)]

        for v in range(vertices):
            for edge in enumerate(edges):
                if v in edge[1]:
                    matrix[v][edge[0]] = 1

        return matrix

    @staticmethod
    def add_vertex(neighbours: list[int], graph: list[list[int]]) -> list[list[int]]:
        new_vertex = len(graph)

        if new_vertex == 0:
            graph.append([])
            return graph

        for n in neighbours:
            for v in range(new_vertex):
                if v == n:
                    graph[v].append(1)
                else:
                    graph[v].append(0)

        old_edges_count = len(graph[0]) - len(neighbours)
        new_row = [0] * old_edges_count 
        new_row.extend([1] * len(neighbours))
        graph.append(new_row)
        
        return graph

    @staticmethod
    def drop_vertex(vertex_number: int, graph: list[list[int]]) -> list[list[int]]:
        trash_row = graph[vertex_number]
        neighbours_columns = [i for i in range(len(trash_row)) if trash_row[i] == 1]
        graph.pop(vertex_number)
        for row in graph:
            for column in reversed(neighbours_columns):
                row.pop(column)
        return graph
