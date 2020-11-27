import sys
sys.path.insert(0, '../2')
from weighted_graph import WeightedGraph
from weighted_graph import WeightedEdge
from generic_search import PriorityQueue

def total_weight(weighted_path):
    return sum([e.weight for e in weighted_path])

def mst(weighted_graph, start=0):
    if start > (weighted_graph.vertex_count - 1) or start < 0:
        return None

    result = []
    priority_queue = PriorityQueue()
    visited = [False] * weighted_graph.vertex_count

    def visit(index):
        visited[index] = True

        for edge in weighted_graph.edges_for_index(index):
            # Add all edges coming from here to priority queue
            if not visited[edge.v]:
                priority_queue.push(edge)

    visit(start)

    while not priority_queue.empty:
        edge = priority_queue.pop()

        if visited[edge.v]:
            continue # Don't ever revisit

        # This is the current smallest, so add it to solution
        result.append(edge)
        visit(edge.v)

    return result

def print_weighted_path(weighted_graph, weighted_path):
    for edge in weighted_path:
        print(f'{weighted_graph.vertex_at(edge.u)} {edge.weight}> {weighted_graph.vertex_at(edge.v)}')

    print(f'Total weight: {total_weight(weighted_path)}')

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

    result = mst(city_graph)

    if result is None:
        print('No solution found!')
    else:
        print_weighted_path(city_graph, result)
