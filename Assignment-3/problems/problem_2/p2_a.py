# Problem 2a,b,c 
# NOTE: Problem B and C are to be implemented in this file as well


import networkx as nx
import matplotlib.pyplot as plt


def visualize_res_graph(res_graph, n, k, source_idx=None, sink_idx=None, name='res_graph'):
    plt.cla()
    plt.clf()
    G = nx.DiGraph()  # Create a directed graph object

    if source_idx is None:
        source_idx = n + k
    if sink_idx is None:
        sink_idx = n + k + 1

    # Add nodes
    for i in range(len(res_graph)):
        G.add_node(i)

    # Add edges based on rGraph adjacency lists
    for i, neighbours in enumerate(res_graph):
        for neighbor in neighbours:
            G.add_edge(i, neighbor)

    # Set position manually for nodes to ensure no overlaps
    pos = {}

    # Position nodes with label 'c'
    for idx in range(n):
        pos[idx] = (0.25, idx / (n-1))

    # Position nodes with label 'r'
    for idx in range(n, n+k):
        pos[idx] = (0.75, (idx-n) / (k-1))

    # Set position for the Source and Sink
    pos[source_idx] = (0, 0.5)
    pos[sink_idx] = (1, 0.5)

    # Map nodes to labels
    labels = {i: "prov" + str(i - n) if i >= n and i < n+k else "hub" + str(i) for i in range(n + k)}
    labels[source_idx] = 'Source'
    labels[sink_idx] = 'Sink'

    # Draw the graph
    nx.draw(G, pos, labels=labels, with_labels=True, node_color="skyblue", node_size=1000, font_size=10, font_weight='bold', edge_color='gray', width=2.0, alpha=0.6)
    plt.savefig(name + ".png")



def plan_city_a(num_data_hubs, num_service_providers, connections, provider_capacities, preliminary_assignment) -> bool:
    """
    Optionally use the code below to verify graph connectivity.
    This is the example function call whose graph is provided in Problem 2.
        plan_city_a(num_data_hubs = 3, \
                    num_service_providers = 2, \
                    connections = {0: [3,4], 1: [3], 2: [3]}, \
                    provider_capacities = [0]*3 + [2, 1],
                    preliminary_assignment = {0: 3, 1: 3}))
    This is the function call whose graph is expected in Problem 2.
        plan_city_a(num_data_hubs = 5, \
                    num_service_providers = 5, \
                    connections = {0: [5,7,8], 1: [5, 8], 2: [7,8,9], 3: [5, 6, 8, 9], 4: [5,6,7,8]}, \
                    provider_capacities = [0]*5 + [0,1,0,2,2], \
                    preliminary_assignment = {0: 8, 1: 8, 2: 9, 3: 9}))
    """
    n = num_data_hubs
    k = num_service_providers
    # Assign source and sink indexes after data hub and service providers
    source, sink = n + k, n + k + 1

    # n data_hubs + k service_providers + 1 source + 1 sink
    res_graph = [[] for _ in range(num_data_hubs + num_service_providers + 2)]

    # Source to data_hubs + data_hubs to service_providers connectivity
    # Add code here # Problem 2a
    for i in range(n):
        if i in connections:
            res_graph[i] = connections[i]
    res_graph[n + k] = [i for i in range(n)]
    visualize_res_graph(res_graph, n, k, name='p2a_graph')

    # service_providers to Sink connectivity
    # Add code here # Problem 2b
    for i in range(n, n + k):
        if provider_capacities[i] > 0:
            res_graph[i] = [n + k + 1]
    visualize_res_graph(res_graph, n, k, name='p2b_graph')

    # Create residual graph accounting for preliminary_assignment
    # Add code here # Problem 2c
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
    visualize_res_graph(res_graph, n, k, name='p2c_graph')
    
