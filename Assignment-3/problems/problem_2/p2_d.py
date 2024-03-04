# Problem 2d
from collections import deque


def plan_city_d(num_data_hubs, num_service_providers, connections, provider_capacities, preliminary_assignment):
    n = num_data_hubs
    k = num_service_providers
    
    # Create a residual graph
    res_graph = [[] for _ in range(num_data_hubs + num_service_providers + 2)]

    # Add edges based on connections (part 2a)
    for i in range(n):
        if i in connections:
            res_graph[i] = connections[i]
    res_graph[n + k] = [i for i in range(n)]
    
    # Add edges based on provider capacities (part 2b)
    for i in range(n, n + k):
        if provider_capacities[i] > 0:
            res_graph[i] = [n + k + 1]

    # Create residual graph accounting for preliminary_assignment (part 2c)
    for i in range(n - 1):
        res_graph[i].append(n + k)
        p = preliminary_assignment[i]
        if p in res_graph[i]:
            res_graph[i].remove(p)
        res_graph[p].append(i)
    
    for i in range(n, n + k):
        if provider_capacities[i] < len(res_graph[i]):
            res_graph[i].remove(n + k + 1)
    res_graph[n + k] = [n - 1]

    # Check if there's a valid flow from source to sink using BFS
    source = n + k
    sink = n + k + 1

    # Implement BFS
    visited = [False] * len(res_graph)
    queue = deque([source])
    visited[source] = True

    while queue:
        node = queue.popleft()
        for neighbor in res_graph[node]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

    if visited[sink]:
        return True
    else:
        return False
