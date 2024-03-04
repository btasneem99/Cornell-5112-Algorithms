# Problem 2e


def plan_city_e(num_data_hubs, num_service_providers, connections, provider_capacities, preliminary_assignment):
    
    n = num_data_hubs
    k = num_service_providers
    # Assign source and sink indexes after data hub and service providers
    source, sink = n + k, n + k + 1 
    
    # n data_hubs + k service_providers + 1 source + 1 sink
    res_graph = [{} for _ in range(num_data_hubs + num_service_providers + 2)]

    # Source to data_hubs + data_hubs to service_providers connectivity
    # Add code here # Problem 2a

    for node, neighbours in list(connections.items()):
        res_graph[source][node] = 1
        for neighbour in neighbours:
            res_graph[node][neighbour] = 1

    # service_providers to Sink connectivity
    # Add code here # Problem 2a

    # # Create residual graph accounting for preliminary_assignment
    # # Add code here # Problem 2b

    for i in range(len(provider_capacities)):
        if provider_capacities[i] > 0:
            res_graph[i][sink] = provider_capacities[i]

    # # Create residual graph accounting for preliminary_assignment
    # # Add code here # Problem 2c
    
    for i in range(len(res_graph)):
        for j in res_graph[i]:
            if i not in res_graph[j]:
                res_graph[j][i] = 0

    for i in range(n-1):
        res_graph[source][i] -= 1
        res_graph[i][preliminary_assignment[i]] -= 1
        res_graph[preliminary_assignment[i]][i] += 1
        res_graph[preliminary_assignment[i]][sink] -= 1
        res_graph[sink][preliminary_assignment[i]] += 1
    
    def ford_fulkerson(res_graph):
        max_flow = 0
        # Find all possible augmenting paths using the residual graph, then update it until no path can be found
        while True:
            path, path_flow = find_augmenting_path(res_graph)
            if path is None:  # No augmenting path found
                break
            max_flow += path_flow
            v = sink
            while v != source:
                u = path[v]
                # Increase reverse capacity by path_flow
                res_graph[v][u] += path_flow
                # Decrease forward capacity by path_flow
                res_graph[u][v] -= path_flow
                # Go to next node in path
                v = u
        return max_flow

    def find_augmenting_path(res_graph):
        # Use BFS to find an augmenting path
        visited = [False] * len(res_graph)
        # Keep track of path taken
        curr_path = [-1] * len(res_graph)
        queue = [source]
        visited[source] = True

        # Do BFS here
        while queue:
            u = queue.pop(0)
            for v in res_graph[u]:
                # only visit a node if their capacity is > 0
                if not visited[v]:
                    if res_graph[u][v] > 0:
                        queue.append(v)
                        visited[v] = True
                        curr_path[v] = u
                        # If v is the sink, we found an augmenting path
                        if v == sink:
                            # Calculate flow of augmented path
                            path_flow = float("inf")
                            s = sink
                            while s != source:
                                # path flow is the minimum residual capacity along path
                                path_flow = min(res_graph[curr_path[s]][s], path_flow)
                                s = curr_path[s]
                            return curr_path, path_flow
        # No augmenting path found
        return None, 0

    flow_status = ford_fulkerson(res_graph) == 1

    if flow_status:
        connectivity_map = []
        for hub in range(n):
            for prov in range(n, n+k):
                if hub in res_graph[prov]:
                    if res_graph[prov][hub] > 0:
                        connectivity_map.append(prov)
                        break
    else:
        connectivity_map = [0]*n
        for prov in res_graph[sink]:
            if res_graph[sink][prov] > 0:
                connectivity_map.append(1)
            else:
                connectivity_map.append(0)
    return connectivity_map