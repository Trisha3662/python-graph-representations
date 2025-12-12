class AdjacencyListGraph:
    class Vertex:
        def __init__(self, element, position):
            self.element = element
            self.position = position
            self.incident_edges = []   # edges connected to this vertex
            self.edge_count = 0

        def __str__(self):
            return "Vertex(" + str(self.element) + ", pos=" + str(self.position) + ")"

        __repr__ = __str__

    class Edge:
        def __init__(self, element, u, v):
            self.element = element
            self.origin = u
            self.dest = v

        def get_endpoints(self):
            return [self.origin, self.dest]

        def __str__(self):
            return "Edge(" + str(self.element) + ", " + \
                   str(self.origin.element) + "-" + str(self.dest.element) + ")"

        __repr__ = __str__

    def __init__(self):
        self.vertices = []
        self.edges = []

    # Insert a vertex
    def insert_vertex(self, x):
        v = self.Vertex(x, len(self.vertices))
        self.vertices.append(v)
        return v

    # Insert an edge
    def insert_edge(self, u, v, elem):
        e = self.Edge(elem, u, v)
        self.edges.append(e)
        # Add to adjacency list
        u.incident_edges.append(e)
        u.edge_count += 1
        v.incident_edges.append(e)
        v.edge_count += 1
        return e

    # Remove an edge
    def remove_edge(self, e):
        if e in self.edges:
            self.edges.remove(e)
        # Remove from both vertices (defensive checks)
        u = e.origin
        v = e.dest
        if e in getattr(u, "incident_edges", []):
            u.incident_edges.remove(e)
            u.edge_count = max(0, u.edge_count - 1)
        if e in getattr(v, "incident_edges", []):
            v.incident_edges.remove(e)
            v.edge_count = max(0, v.edge_count - 1)

    # Remove a vertex
    def remove_vertex(self, v):
        # Remove edges connected to v (use a copy)
        for e in list(self.edges):
            if v in e.get_endpoints():
                self.remove_edge(e)
        # Remove vertex
        if v in self.vertices:
            self.vertices.remove(v)
        # Update positions
        for pos, vert in enumerate(self.vertices):
            vert.position = pos


if __name__ == "__main__":
    g = AdjacencyListGraph()
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
    print("\nEdges after removing e1:")
    for e in g.edges:
        print(e)
    g.remove_vertex(b)
    print("\nVertices after removing B:")
    for v in g.vertices:
        print(v)
    print("\nEdges after removing B:")
    for e in g.edges:
        print(e)
