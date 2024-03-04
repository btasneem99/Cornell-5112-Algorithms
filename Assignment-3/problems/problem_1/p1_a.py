from collections import deque


def is_bipartite(g_l):
    def is_bipartite_component(start_node, color):
        queue = deque()
        queue.append(start_node)
        color[start_node] = 0  # Color the starting node with 0

        while queue:
            current_node = queue.popleft()
            current_color = color[current_node]

            for neighbor in g_l[current_node]:
                if color[neighbor] == -1:
                    color[neighbor] = 1 - current_color  # Color the neighbor with the opposite color
                    queue.append(neighbor)
                elif color[neighbor] == current_color:
                    return False  # Graph is not bipartite

        return True

    if not g_l:
        return True  # An empty graph is trivially bipartite

    num_nodes = len(g_l)
    color = [-1] * num_nodes

    for node in range(num_nodes):
        if color[node] == -1:
            if not is_bipartite_component(node, color):
                return False

    return True
