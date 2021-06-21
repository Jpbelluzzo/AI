from collections import defaultdict
from random import seed
from random import randint
import math
import numpy as np
seed(3)

def knn_generator(k, n, x, y):
    knn_graph = defaultdict(dict)
    x_coords = []
    y_coords = []
    connections = []
    for i in range(n):
        knn_graph[i]['x'], knn_graph[i]['y'] = generate_node(x, y)
        x_coords += [knn_graph[i]['x']]
        y_coords += [knn_graph[i]['y']]
        knn_graph[i]['connections'] = []
    distances = get_nodes_distances(knn_graph)
    for node in knn_graph:
        closest_nodes = np.argsort(distances[node])
        for i in range(k):
            if i<n:
                closest_node = closest_nodes[i+1]
                if closest_node not in knn_graph[node]['connections']:
                    knn_graph[node]['connections'] += [closest_node]
                if node not in knn_graph[closest_node]['connections']:
                    knn_graph[closest_node]['connections'].append(node)
                if [closest_nodes[i+1],node] not in connections:
                    connections += [[node, closest_nodes[i+1]]]
    return knn_graph, x_coords, y_coords, connections

def generate_node(x_limit, y_limit):
    return randint(0, x_limit), randint(0, y_limit)

def get_nodes_distances(graph):
    distances = np.zeros( (len(graph), len(graph)) )
    for i in range(1, len(graph)):
        for j in range(i+1):
            distances[i][j] = distances[j][i] = get_euclidean_distance(graph, i, j)
    return distances

def get_euclidean_distance(graph, i, j):
    return math.sqrt(math.pow(graph[i]['x']-graph[j]['x'], 2) + math.pow(graph[i]['y']-graph[j]['y'], 2))
