import sys
sys.path.insert(0, '../2')
from edge import Edge
from generic_search import bfs, node_to_path, Node

class Graph:
    def __init__(self, vertices):
        self._vertices = vertices
        self._edges = [[] for _ in vertices]

    @property
    def vertex_count(self):
        return len(self._vertices)

    @property
    def edge_count(self):
        return sum(len(edge) for edge in self._edges)

    # Add a vertex to the graph and return its index
    def add_vertex(self, vertex):
        self._vertices.append(vertex)
        self._edges.append([]) # Empty list for edges
        return self.vertex_count - 1 # Return index of added vertex

    # This is an undirected graph, so we always add edges in both directions
    def add_edge(self, edge):
        self._edges[edge.u].append(edge)
        self._edges[edge.v].append(edge.reversed())

    # Add an edge using vertex indices (convenience method)
    def add_edge_by_indices(self, u, v):
        edge = Edge(u, v)
        self.add_edge(edge)

    # Add an edge by looking up vertex indices (convenience method)
    def add_edge_by_vertices(self, first, second):
        u = self._vertices.index(first)
        v = self._vertices.index(second)
        self.add_edge_by_indices(u, v)

    # Find the vertex at a specific index
    def vertex_at(self, index):
        return self._vertices[index]

    # Find the index of a vertex in the graph
    def index_of(self, vertex):
        return self._vertices.index(vertex)

    # Find the vertices that a vertex at some index is connected to
    def neighbors_for_index(self, index):
        return [self.vertex_at(e.v) for e in self._edges[index]]

    # Look up a vertice's index and find its neighbors (convenience method)
    def neighbors_for_vertex(self, vertex):
        return self.neighbors_for_index(self.index_of(vertex))

    # Return all of the edges associated with a vertex at some index
    def edges_for_index(self, index):
        return self._edges[index]

    # Look up the index of a vertex and return its edges (convenience method)
    def edges_for_vertex(self, vertex):
        return self.edges_for_index(self.index_of(vertex))

    # Make it easy to pretty print a Graph
    def __str__(self):
        description = ''

        for i in range(self.vertex_count):
            description += f'{self.vertex_at(i)} -> {self.neighbors_for_index(i)}\n'

        return description.strip()

if __name__ == '__main__':
    # Test basic Graph construction
    city_graph = Graph([
        'Seattle',
        'San Francisco',
        'Los Angeles',
        'Riverside',
        'Phoenix',
        'Chicago',
        'Boston',
        'New York',
        'Atlanta',
        'Miami',
        'Dallas',
        'Houston',
        'Detroit',
        'Philadelphia',
        'Washington'
    ])

    city_graph.add_edge_by_vertices('Seattle', 'Chicago')
    city_graph.add_edge_by_vertices('Seattle', 'San Francisco')
    city_graph.add_edge_by_vertices('San Francisco', 'Riverside')
    city_graph.add_edge_by_vertices('San Francisco', 'Los Angeles')
    city_graph.add_edge_by_vertices('Los Angeles', 'Riverside')
    city_graph.add_edge_by_vertices('Los Angeles', 'Phoenix')
    city_graph.add_edge_by_vertices('Riverside', 'Phoenix')
    city_graph.add_edge_by_vertices('Riverside', 'Chicago')
    city_graph.add_edge_by_vertices('Phoenix', 'Dallas')
    city_graph.add_edge_by_vertices('Phoenix', 'Houston')
    city_graph.add_edge_by_vertices('Dallas', 'Chicago')
    city_graph.add_edge_by_vertices('Dallas', 'Atlanta')
    city_graph.add_edge_by_vertices('Dallas', 'Houston')
    city_graph.add_edge_by_vertices('Houston', 'Atlanta')
    city_graph.add_edge_by_vertices('Houston', 'Miami')
    city_graph.add_edge_by_vertices('Atlanta', 'Chicago')
    city_graph.add_edge_by_vertices('Atlanta', 'Washington')
    city_graph.add_edge_by_vertices('Atlanta', 'Miami')
    city_graph.add_edge_by_vertices('Miami', 'Washington')
    city_graph.add_edge_by_vertices('Chicago', 'Detroit')
    city_graph.add_edge_by_vertices('Detroit', 'Boston')
    city_graph.add_edge_by_vertices('Detroit', 'Washington')
    city_graph.add_edge_by_vertices('Detroit', 'New York')
    city_graph.add_edge_by_vertices('Boston', 'New York')
    city_graph.add_edge_by_vertices('New York', 'Philadelphia')
    city_graph.add_edge_by_vertices('Philadelphia', 'Washington')

    bfs_result = bfs('Boston', lambda x: x == 'Miami', city_graph.neighbors_for_vertex)

    if bfs_result is None:
        print('No solution found using BFS!')
    else:
        path = node_to_path(bfs_result)
        print('Path from Boston to Miami:')
        print(path)
