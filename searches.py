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
    visited[init_node] = True
    queue = [[init_node]]
    while(queue):
        path = queue.pop(0)
        node = path[-1]
        if node == end_node:
            return path
        neighbours = connections[node]
        best_paths = []
        for neighbour in neighbours:
            best_paths.append((neighbour, distances[neighbour][node]))
        best_paths.sort(key=lambda path:path[1])
        for neighbour in best_paths:
            if not visited[neighbour[0]]:
                aux = path + [neighbour[0]]
                queue.append(aux)
                visited[neighbour[0]] = True

# A Algorithm

def A_search(init_node, end_node, vertices, connections, distances):
    visited = [False]*len(vertices)
    visited[init_node] = True
    queue = [[init_node]]
    while(queue):
        path = queue.pop(0)
        node = path[-1]
        if node == end_node:
            return path
        neighbours = connections[node]
        best_paths = []
        for neighbour in neighbours:
            best_paths.append((neighbour, distances[neighbour][node]+distances[neighbour][end_node]))
        best_paths.sort(key=lambda path:path[1])
        for neighbour in best_paths:
            if not visited[neighbour[0]]:
                aux = path + [neighbour[0]]
                queue.append(aux)
                visited[neighbour[0]] = True