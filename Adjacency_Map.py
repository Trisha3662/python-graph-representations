class AdjacencyMapGraph:

    class Vertex:
        def __init__(self, element):
            self.element = element

        def __str__(self):
            return "Vertex(" + str(self.element) + ")"

        __repr__ = __str__

        # Make explicit hash behavior (identity-based)
        def __hash__(self):
            return id(self)

        def __eq__(self, other):
            return self is other

    class Edge:
        def __init__(self, element, u, v):
            self.element = element
            self.origin = u
            self.destination = v

        def endpoints(self):
            return self.origin, self.destination

        def __str__(self):
            return "Edge(" + str(self.element) + ", " + \
                   str(self.origin.element) + "-" + str(self.destination.element) + ")"

        __repr__ = __str__

    def __init__(self):
        self._outgoing = {}   # vertex → dict of (neighbor → edge)
        self._incoming = {}   # same as outgoing for undirected graph
        self.edges = []

    # Insert vertex
    def insert_vertex(self, x):
        v = self.Vertex(x)
        self._outgoing[v] = {}
        self._incoming[v] = {}
        return v

    # Insert edge
    def insert_edge(self, u, v, element):
        # Defensive: ensure u and v are in maps
        if u not in self._outgoing or v not in self._outgoing:
            raise KeyError("Both vertices must be inserted before adding an edge")
        e = self.Edge(element, u, v)
        self.edges.append(e)

        # For undirected graph, store edge in both maps
        self._outgoing[u][v] = e
        self._outgoing[v][u] = e

        self._incoming[u][v] = e
        self._incoming[v][u] = e

        return e

    # Get edge between two vertices
    def get_edge(self, u, v):
        if u not in self._outgoing:
            return None
        return self._outgoing[u].get(v)

    # Remove edge
    def remove_edge(self, e):
        u, v = e.endpoints()
        # Defensive removals (pop with default)
        if u in self._outgoing:
            self._outgoing[u].pop(v, None)
        if v in self._outgoing:
            self._outgoing[v].pop(u, None)
        if u in self._incoming:
            self._incoming[u].pop(v, None)
        if v in self._incoming:
            self._incoming[v].pop(u, None)
        if e in self.edges:
            self.edges.remove(e)

    # Remove vertex
    def remove_vertex(self, v):
        # Remove all edges connected to vertex (copy values first)
        incident_edges = list(self._outgoing.get(v, {}).values())
        for e in incident_edges:
            self.remove_edge(e)

        # delete the vertex maps (defensive)
        self._outgoing.pop(v, None)
        self._incoming.pop(v, None)

    # Display adjacency map
    def display(self):
        print("\nAdjacency Map:")
        for v in self._outgoing:
            print(v.element, "->", [nbr.element for nbr in self._outgoing[v]])


if __name__ == "__main__":
    g = AdjacencyMapGraph()

    a = g.insert_vertex("A")
    b = g.insert_vertex("B")
    c = g.insert_vertex("C")
    d = g.insert_vertex("D")

    g.insert_edge(a, b, "e1")
    g.insert_edge(a, c, "e2")
    g.insert_edge(b, d, "e3")

    g.display()
