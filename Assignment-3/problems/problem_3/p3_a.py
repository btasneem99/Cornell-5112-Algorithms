# Problem 3
from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.verts = vertices
        self.graph = defaultdict(list)
        self.flow_values = {}

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.flow_values[(u, v)] = 1
        self.flow_values[(v, u)] = 1

    def searching_path(self, s, t, parent):
        visited = [False] * (self.verts)
        queue = [s]
        visited[s] = True
        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if visited[val] == False and self.flow_values[(u, val)] > 0:
                    queue.append(val)
                    visited[val] = True
                    parent[val] = u
        return True if visited[t] else False

    def ford_fulkerson(self, source, sink):
        parent = [-1] * (self.verts)
        max_flow = 0
        while self.searching_path(source, sink, parent):
            path_flow = float("Inf")
            sink_temp = sink
            while sink_temp != source:
                path_flow = min(path_flow, self.flow_values[(parent[sink_temp], sink_temp)])
                sink_temp = parent[sink_temp]
            max_flow += path_flow
            v = sink
            while v != source:
                u = parent[v]
                self.flow_values[(u, v)] -= path_flow
                self.flow_values[(v, u)] += path_flow
                v = parent[v]
        return max_flow


def find_paths(n, paths):
    g = Graph(n+1) # Since vertices are 1-indexed
    for u, v in paths:
        g.add_edge(u, v)
    return g.ford_fulkerson(1, n)