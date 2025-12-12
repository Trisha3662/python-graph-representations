class AdjacencyMatrixGraph:
    class Vertex:
        def __init__(self, element, position):
            self.element = element
            self.position = position

        def __str__(self):
            return "Vertex("+str(self.element)+",pos="+str(self.position) + ")"

        __repr__ = __str__

    class Edge:
        def __init__(self, element, u, v):
            self.element = element
            self.origin = u
            self.dest = v

        def __str__(self):
            return "Edge("+str(self.element)+","+str(self.origin.element) + "-" + str(self.dest.element) + ")"

        __repr__ = __str__

    def __init__(self, max_vertices):
        self.vertices = []
        self.edges = []
        self.max_vertices = max_vertices
        # Create 2D matrix and fill with 0 (meaning no edge)
        self.matrix = [[0 for _ in range(max_vertices)] for _ in range(max_vertices)]

    # Insert a vertex
    def insert_vertex(self, element):
        if len(self.vertices) >= self.max_vertices:
            raise ValueError("Maximum number of vertices reached")
        v = self.Vertex(element, len(self.vertices))
        self.vertices.append(v)
        return v

    # Insert an edge
    def insert_edge(self, u, v, element):
        if u.position >= self.max_vertices or v.position >= self.max_vertices:
            raise IndexError("Vertex position out of matrix bounds")
        e = self.Edge(element, u, v)
        self.edges.append(e)
        i = u.position
        j = v.position
        # store edge name in matrix (undirected graph)
        self.matrix[i][j] = element
        self.matrix[j][i] = element
        return e

    # Remove an edge
    def remove_edge(self, e):
        if e in self.edges:
            self.edges.remove(e)
        i = e.origin.position
        j = e.dest.position
        # guard indices
        if 0 <= i < self.max_vertices and 0 <= j < self.max_vertices:
            self.matrix[i][j] = 0
            self.matrix[j][i] = 0

    # Remove a vertex
    def remove_vertex(self, v):
        index = v.position
        # Remove associated edges — iterate over a copy of edges
        for e in list(self.edges):
            if (e.origin == v) or (e.dest == v):
                self.remove_edge(e)
        # clear the row and column (safe-guard indices)
        if 0 <= index < self.max_vertices:
            for i in range(self.max_vertices):
                self.matrix[index][i] = 0
                self.matrix[i][index] = 0
        # remove the vertex
        if v in self.vertices:
            self.vertices.remove(v)
        # update vertex positions
        for pos, vert in enumerate(self.vertices):
            vert.position = pos

    def display(self):
        print("\nAdjacency Matrix:")
        for i in range(len(self.vertices)):
            row = []
            for j in range(len(self.vertices)):
                row.append(self.matrix[i][j])
            print(row)
        print("\nVertices:")
        for v in self.vertices:
            print(v)
        print("\nEdges:")
        for e in self.edges:
            print(e)


if __name__ == "__main__":
    g = AdjacencyMatrixGraph(10)
    a = g.insert_vertex("A")
    b = g.insert_vertex("B")
    c = g.insert_vertex("C")
    e1 = g.insert_edge(a, b, "e1")
    e2 = g.insert_edge(b, c, "e2")
    e3 = g.insert_edge(a, c, "e3")
    g.display()
    print("\nRemoving e1:")
    g.remove_edge(e1)
    g.display()
    print("\nRemoving vertex B:")
    g.remove_vertex(b)
    g.display()
