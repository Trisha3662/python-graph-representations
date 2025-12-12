class EdgeListGraph:
    class Vertex:
        def __init__(self, element, position):
            self.element = element
            self.position = position

        def __str__(self):
            return "Vertex("+str(self.element)+",pos="+str(self.position) + ")"

        __repr__ = __str__

    class Edge:
        def __init__(self, element, u, v, position):
            self.element = element
            self.origin = u
            self.destination = v
            self.position = position

        def get_endpoints(self):
            return [self.origin, self.destination]

        def __str__(self):
            return "Edge("+str(self.element)+",pos=" + str(self.position) + ")"

        __repr__ = __str__

    def __init__(self):
        self.vertices = []
        self.edges = []

    # Insert vertex
    def insert_vertex(self, x):
        v = self.Vertex(x, len(self.vertices))
        self.vertices.append(v)
        return v

    # Insert edge
    def insert_edge(self, u, v, elem):
        e = self.Edge(elem, u, v, len(self.edges))
        self.edges.append(e)
        return e

    # Remove edge
    def remove_edge(self, e):
        if e in self.edges:
            self.edges.remove(e)
            # changing positions
            for new_pos, edge in enumerate(self.edges):
                edge.position = new_pos

    # Remove vertex
    def remove_vertex(self, v):
        # Remove all edges touching v (use copy to avoid mutating while iterating)
        self.edges = [e for e in self.edges if v not in e.get_endpoints()]

        # changing edge positions
        for new_pos, e in enumerate(self.edges):
            e.position = new_pos

        # remove the vertex if present
        if v in self.vertices:
            self.vertices.remove(v)

        # changing vertex positions
        for new_pos, vert in enumerate(self.vertices):
            vert.position = new_pos


if __name__ == "__main__":
    g = EdgeListGraph()
    a = g.insert_vertex("A")
    b = g.insert_vertex("B")
    c = g.insert_vertex("C")
    e1 = g.insert_edge(a, b, "e1")
    e2 = g.insert_edge(b, c, "e2")

    print("Vertices:")
    for v in g.vertices:
        print(v)
    print("\nEdges:")
    for e in g.edges:
        print(e)

    g.remove_edge(e1)
    print("\nAfter removing e1:")
    for e in g.edges:
        print(e)

    g.remove_vertex(b)
    print("\nAfter removing vertex B:")
    for v in g.vertices:
        print(v)
    for e in g.edges:
        print(e)
