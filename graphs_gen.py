from collections import defaultdict
from random import seed
import math
import random
from matplotlib.pyplot import connect
import numpy as np
from numpy.core.defchararray import index
import progressbar
seed(3)

def knn_generator(k, n, x, y):
    knn_graph = []
    x_coords = np.empty(0)
    y_coords = np.empty(0)
    connections = list()
    for i in range(n):
        coords = tuple(generate_node(x, y))
        knn_graph.append(coords)
        x_coords = np.append(x_coords, coords[0])
        y_coords = np.append(y_coords, coords[1])
    print('Nodes generated with success!')
    print('Calculating distances...')
    distances = get_nodes_distances(knn_graph)
    print('Generating edges...')
    with progressbar.ProgressBar(max_value=len(knn_graph)) as bar:
        for index, node in enumerate(knn_graph):
            node_connections = []
            for i in range(k):
                if i<n:
                    closest_node = np.argpartition(distances[index], i+1)[i+1]
                    node_connections.append(closest_node)
            connections.append(node_connections)
            bar.update(index)
    return knn_graph, x_coords, y_coords, connections

def generate_node(x_limit, y_limit):
    return (random.random())*x_limit, (random.random())*y_limit

def get_nodes_distances(graph):
    distances = np.zeros( (len(graph), len(graph)) )
    with progressbar.ProgressBar(max_value=len(graph)) as bar:
        for i in range(1, len(graph)):
            for j in range(i+1):
                p1 = graph[i]
                p2 = graph[j]
                distances[i][j] = distances[j][i] = get_euclidean_distance(p1, p2)
            bar.update(i)
    return distances

def get_euclidean_distance(p1, p2):
    return math.sqrt(math.pow(p1[0]-p2[0], 2) + math.pow(p1[1]-p2[1], 2))
