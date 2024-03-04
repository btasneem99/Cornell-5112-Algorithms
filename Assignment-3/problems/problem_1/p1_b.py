# Problem 1b


def maximal_bipartite_match(g) -> int:
    def augment_path(node, visited):
        for v in range(num_right):
            if g[node][v] and not visited[v]:
                visited[v] = True
                if right_match[v] is None or augment_path(right_match[v], visited):
                    left_match[node] = v
                    right_match[v] = node
                    return True
        return False

    num_left = len(g)
    num_right = len(g[0])
    left_match = [None] * num_left
    right_match = [None] * num_right
    max_matches = 0

    for u in range(num_left):
        visited = [False] * num_right
        if augment_path(u, visited):
            max_matches += 1

    return max_matches