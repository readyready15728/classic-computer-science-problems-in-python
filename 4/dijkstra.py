import sys
sys.path.insert(0, '../2')
from dataclasses import dataclass
from mst import print_weighted_path
from weighted_graph import WeightedGraph
from weighted_edge import WeightedEdge
from generic_search import PriorityQueue

@dataclass
class DijkstraNode:
    vertex: int
    distance: float

    def __lt__(self, other):
        return self.distance < other.distance

    def __eq__(self, other):
        return self.distance == other.distance

def dijkstra(weighted_graph, root):
    first = weighted_graph.index_of(root) # Find starting index
    distances = [None] * weighted_graph.vertex_count # Distances are unknown at first
    distances[first] = 0
    path_dict = {} # How we got to each index
    priority_queue = PriorityQueue()
    priority_queue.push(DijkstraNode(first, 0))

    while not priority_queue.empty:
        u = priority_queue.pop().vertex # Explore the next closest vertex
        distance_u = distances[u] # Should have already seen seen it

        for weighted_edge in weighted_graph.edges_for_index(u):
            distance_v = distances[weighted_edge.v] # The old distance to the vertex
            if distance_v is None or distance_v > weighted_edge.weight + distance_u: # No old distance or found shorter path
                distances[weighted_edge.v] = weighted_edge.weight + distance_u # Update distance to this vertex
                path_dict[weighted_edge.v] = weighted_edge # Update the edge on the shortest path to this vertex
                priority_queue.push(DijkstraNode(weighted_edge.v, weighted_edge.weight + distance_u)) # Explore it soon

    return distances, path_dict

def distance_array_to_vertex_dict(weighted_graph, distances): # Helper function to get easier access to results
    distance_dict = {}

    for i in range(len(distances)):
        distance_dict[weighted_graph.vertex_at(i)] = distances[i]

    return distance_dict

def path_dict_to_path(start, end, path_dict): # Takes a dictionary of edges to reach each node and returns a list of edges that goes from start to end
    if len(path_dict) == 0:
        return []

    edge_path = []
    e = path_dict[end]
    edge_path.append(e)

    while e.u != start:
        e = path_dict[e.u]
        edge_path.append(e)

    return list(reversed(edge_path))

if __name__ == '__main__':
    city_graph = WeightedGraph([
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

    city_graph.add_edge_by_vertices('Seattle', 'Chicago', 1737)
    city_graph.add_edge_by_vertices('Seattle', 'San Francisco', 678)
    city_graph.add_edge_by_vertices('San Francisco', 'Riverside', 386)
    city_graph.add_edge_by_vertices('San Francisco', 'Los Angeles', 348)
    city_graph.add_edge_by_vertices('Los Angeles', 'Riverside', 50)
    city_graph.add_edge_by_vertices('Los Angeles', 'Phoenix', 357)
    city_graph.add_edge_by_vertices('Riverside', 'Phoenix', 307)
    city_graph.add_edge_by_vertices('Riverside', 'Chicago', 1704)
    city_graph.add_edge_by_vertices('Phoenix', 'Dallas', 887)
    city_graph.add_edge_by_vertices('Phoenix', 'Houston', 1015)
    city_graph.add_edge_by_vertices('Dallas', 'Chicago', 805)
    city_graph.add_edge_by_vertices('Dallas', 'Atlanta', 721)
    city_graph.add_edge_by_vertices('Dallas', 'Houston', 225)
    city_graph.add_edge_by_vertices('Houston', 'Atlanta', 702)
    city_graph.add_edge_by_vertices('Houston', 'Miami', 968)
    city_graph.add_edge_by_vertices('Atlanta', 'Chicago', 588)
    city_graph.add_edge_by_vertices('Atlanta', 'Washington', 543)
    city_graph.add_edge_by_vertices('Atlanta', 'Miami', 604)
    city_graph.add_edge_by_vertices('Miami', 'Washington', 923)
    city_graph.add_edge_by_vertices('Chicago', 'Detroit', 238)
    city_graph.add_edge_by_vertices('Detroit', 'Boston', 613)
    city_graph.add_edge_by_vertices('Detroit', 'Washington', 396)
    city_graph.add_edge_by_vertices('Detroit', 'New York', 482)
    city_graph.add_edge_by_vertices('Boston', 'New York', 190)
    city_graph.add_edge_by_vertices('New York', 'Philadelphia', 81)
    city_graph.add_edge_by_vertices('Philadelphia', 'Washington', 123)

    distances, path_dict = dijkstra(city_graph, 'Los Angeles')
    name_distance = distance_array_to_vertex_dict(city_graph, distances)
    print('Distances from Los Angeles:')

    for key, value in name_distance.items():
        print(f'{key}: {value}')

    print()

    print('Shortest path from Los Angeles to Boston:')
    path = path_dict_to_path(city_graph.index_of('Los Angeles'), city_graph.index_of('Boston'), path_dict)
    print_weighted_path(city_graph, path)

    print(path_dict)
