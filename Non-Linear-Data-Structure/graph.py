"""
Graph structure (Assessment 3.3)

Vertices: R, E1, P, U, N, T, E2 (the two E's are numbered to tell them apart)
Edges: R-E1, R-P, E1-U, E1-N, N-P, N-E2, P-T, T-E2
"""
from collections import deque


class Graph:
    def __init__(self):
        self.adjacency = {}

    def add_vertex(self, vertex):
        self.adjacency.setdefault(vertex, [])

    def add_edge(self, a, b):
        self.adjacency[a].append(b)
        self.adjacency[b].append(a)

    def build(self):
        """Algorithm 2A: build the graph from the diagram."""
        for vertex in ["R", "E1", "P", "U", "N", "T", "E2"]:
            self.add_vertex(vertex)
        self.add_edge("R", "E1")
        self.add_edge("R", "P")
        self.add_edge("E1", "U")
        self.add_edge("E1", "N")
        self.add_edge("N", "P")
        self.add_edge("N", "E2")
        self.add_edge("P", "T")
        self.add_edge("T", "E2")

    def bfs(self, start):
        """Algorithm 2B: breadth-first search using a queue and visited set."""
        visited = {start}
        queue = deque([start])
        result = []
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            for neighbor in self.adjacency[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return result

    def dfs(self, start):
        """Algorithm 2C: depth-first search using recursion and visited set."""
        result = []
        self._dfs_visit(start, set(), result)
        return result

    def _dfs_visit(self, vertex, visited, result):
        visited.add(vertex)
        result.append(vertex)
        for neighbor in self.adjacency[vertex]:
            if neighbor not in visited:
                self._dfs_visit(neighbor, visited, result)


def run():
    """Build the graph and print its adjacency list and traversals."""
    graph = Graph()
    graph.build()
    print("=== GRAPH ===")
    for vertex, neighbors in graph.adjacency.items():
        print(f"{vertex}: {', '.join(neighbors)}")
    print("BFS:", " -> ".join(graph.bfs("R")))
    print("DFS:", " -> ".join(graph.dfs("R")))


if __name__ == "__main__":
    run()
