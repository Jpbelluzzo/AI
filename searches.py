import numpy as np
from numpy.core import numeric

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
    queue = [([init_node],0)]
    while(queue):
        (path, accumulated_distance) = min(queue, key= lambda tup: tup[1])
        queue.remove((path, accumulated_distance))
        node = path[-1]
        if node == end_node:
            return path
        neighbours = connections[node]
        best_paths = []
        for neighbour in neighbours:
            best_paths.append((neighbour, accumulated_distance + distances[neighbour][node]))
        best_paths.sort(key=lambda path:path[1])
        for neighbour in best_paths:
            if not visited[neighbour[0]]:
                aux = path + [neighbour[0]]
                queue.append((aux, neighbour[1]))
                visited[neighbour[0]] = True

# A Algorithm

def reconstructed_path(cameFrom, current):
    total_path = [current]
    while (int(cameFrom[current]) != -1):
        current = int(cameFrom[current])
        total_path = [current] + total_path
    return total_path

def A_search(init_node, end_node, vertices, connections, distances):
    queue = [init_node]

    n = len(vertices)

    cameFrom = np.zeros(n) - 1

    gScore = np.ones(n) * np.inf
    gScore[init_node] = 0

    fScore = np.ones(n) * np.inf
    fScore[init_node] = 0

    while(queue):

        current, _ = min([(x, fScore[x]) for x in queue], key= lambda tup: tup[1])

        if(current == end_node):
            return reconstructed_path(cameFrom, current)
    
        queue.remove(current)

        neighbours = connections[current]

        for neighbour in neighbours:
            tentative_score = gScore[current] + distances[current][neighbour]
            if tentative_score < gScore[neighbour]:
                cameFrom[neighbour] = current
                gScore[neighbour] = tentative_score
                fScore[neighbour] = gScore[neighbour] + gScore[neighbour]/distances[init_node][neighbour] * distances[neighbour][end_node]
                if neighbour not in queue:
                    queue.append(neighbour)


def A_star_search(init_node, end_node, vertices, connections, distances):
    queue = [init_node]

    n = len(vertices)

    cameFrom = np.zeros(n) - 1

    gScore = np.ones(n) * np.inf
    gScore[init_node] = 0

    fScore = np.ones(n) * np.inf
    fScore[init_node] = 0

    while(queue):

        current, _ = min([(x, fScore[x]) for x in queue], key= lambda tup: tup[1])

        if(current == end_node):
            return reconstructed_path(cameFrom, current)
    
        queue.remove(current)

        neighbours = connections[current]

        for neighbour in neighbours:
            tentative_score = gScore[current] + distances[current][neighbour]
            if tentative_score < gScore[neighbour]:
                cameFrom[neighbour] = current
                gScore[neighbour] = tentative_score
                fScore[neighbour] = gScore[neighbour] + distances[neighbour][end_node]
                if neighbour not in queue:
                    queue.append(neighbour)

'''
# A Algorithm

def A_search(init_node, end_node, vertices, connections, distances):
    visited = [False]*len(vertices)
    visited[init_node] = True
    queue = [([init_node],0)]
    while(queue):
        (path, accumulated_distance) = min(queue, key= lambda tup: tup[1])
        queue.remove((path, accumulated_distance))
        node = path[-1]
        if node == end_node:
            return path
        neighbours = connections[node]
        best_paths = []
        for neighbour in neighbours:
            best_paths.append((neighbour, accumulated_distance + distances[neighbour][node] + distances[neighbour][end_node]**2))
        best_paths.sort(key=lambda path:path[1])
        for neighbour in best_paths:
            if not visited[neighbour[0]]:
                aux = path + [neighbour[0]]
                queue.append((aux, neighbour[1]))
                visited[neighbour[0]] = True

# A* Algorithm

def A_star_search(init_node, end_node, vertices, connections, distances):
    visited = [False]*len(vertices)
    visited[init_node] = True
    queue = [([init_node],0)]
    while(queue):
        (path, accumulated_distance) = min(queue, key= lambda tup: tup[1])
        queue.remove((path, accumulated_distance))
        node = path[-1]
        if node == end_node:
            return path
        neighbours = connections[node]
        best_paths = []
        for neighbour in neighbours:
            best_paths.append((neighbour, accumulated_distance + distances[neighbour][node] + distances[neighbour][end_node]))
        best_paths.sort(key=lambda path:path[1])
        for neighbour in best_paths:
            if not visited[neighbour[0]]:
                aux = path + [neighbour[0]]
                queue.append((aux, neighbour[1]))
                visited[neighbour[0]] = True
'''