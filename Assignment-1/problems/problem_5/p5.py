'''
Problem 5

input: List of tuples representing the friend's apartments.
output: List of apartment pairs.

TODO: implement your solution.
'''
import heapq


def cookies_distribution_map(apartments) -> list:
    current_tree = []
    current_node = (1, 1)
    priority_queue = []
    visited = {(1, 1)}

    edges_matrix = generate_all_edges(apartments)
    while len(current_tree) != len(apartments) - 1:
        available_edges = edges_matrix[current_node]
        for neighbor_node, edge_cost in available_edges.items():
            if neighbor_node not in visited:
                heapq.heappush(priority_queue, [edge_cost, current_node, neighbor_node])
        edge_cost, current_node, next_node = heapq.heappop(priority_queue)
        if next_node not in visited:
            visited.add(next_node)
            current_tree.append((current_node, next_node))
            current_node = next_node
    return set(current_tree)


def manhattan_distance(coord1, coord2):
    x_diff = abs(coord1[0] - coord2[0])
    y_diff = abs(coord1[1] - coord2[1])
    return x_diff + y_diff


def generate_all_edges(coordinates):
    coordinates.append((1, 1))

    edges_matrix = {coord: {} for coord in coordinates}
    for i in range(len(coordinates)):
        for j in range(len(coordinates)):
            if i != j:
                mh_distance = manhattan_distance(coordinates[i], coordinates[j])
                edges_matrix[coordinates[i]][coordinates[j]] = mh_distance
    return edges_matrix


# Example usage:
# apartments = [(1, 1), (1, 2), (2, 1), (2, 2), (3, 1), (3, 2)]  # List of apartments
# pairs = minimize_steps(apartments)
# print(pairs)