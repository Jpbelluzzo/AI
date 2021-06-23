import bisect
from sys import path

# Depth-First Search Algorithm

def depth_first_search(init_node, end_node, vertices, connections):
    paths = [(init_node, [init_node])]
    visited = [False]*len(vertices)
    while(paths):
        (node, path) = paths.pop()
        if not visited[node]:
            if node == end_node:
                return path
            visited[node] = True
            for neighbour in connections[node]:
                paths.append((neighbour, path + [neighbour]))

# Breadth-First Search Algorithm

def breadth_first_search(init_node, end_node, vertices, connections):
    visited = [False]*len(vertices)
    visited[init_node] = True
    queue = [[init_node]]
    while(queue):
        path = queue.pop(0)
        node = path[-1]
        if node == end_node:
            return path
        neighbours = connections[node]
        for neighbour in neighbours:
            if not visited[neighbour]:
                aux = path + [neighbour]
                queue.append(aux)
                visited[neighbour] = True

# Best-First Search Algorithm

def best_first_search(init_node, end_node, vertices, connections, distances):
    visited = [False]*len(vertices)
    path = []
    queue = [init_node]
    visited[init_node] = True
    while(queue):
        first_node = queue[0]
        path.append(first_node)
        del queue[0]
        visited[first_node] = True
        node_connections = connections[first_node]
        if end_node in node_connections:
            path.append(end_node)
            return path
        node_distances = distances[first_node]
        neighbours = []
        for node in node_connections:
            if node not in queue and not visited[node]:
                neighbours.append((node, distances[first_node][node]))
        neighbours.sort(key = lambda x: x[1])
        for node in neighbours:
            queue.append(node[0])