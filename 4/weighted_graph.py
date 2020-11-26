from graph import Graph
from weighted_edge import WeightedEdge

class WeightedGraph(Graph):
    def __init__(self, vertices):
        self._vertices = vertices
        self._edges = [[] for _ in vertices]

    def add_edge_by_indices(self, u, v, weight):
        edge = WeightedEdge(u, v, weight)
        self.add_edge(edge)

    def add_edge_by_vertices(self, first, second, weight):
        u = self._vertices.index(first)
        v = self._vertices.index(second)
        self.add_edge_by_indices(u, v, weight)

    def neighbors_for_index_with_weights(self, index):
        distance_tuples = []

        for edge in self.edges_for_index(index):
            distance_tuples.append((self.vertex_at(edge.v), edge.weight))

        return distance_tuples

    def __str__(self):
        description = ''

        for i in range(self.vertex_count):
            description += f'{self.vertex_at(i)} -> {self.neighbors_for_index_with_weights(i)}\n'

        return description
