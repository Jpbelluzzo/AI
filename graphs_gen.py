from collections import defaultdict
from os import close
from random import seed
import math
import random
from matplotlib.pyplot import connect
import numpy as np
from numpy.core.defchararray import index, mod
from scipy.spatial import distance, distance_matrix
import progressbar
import networkx
seed(3)

def knn_generator(k, n, x, y):
    vertices = []
    x_coords = np.empty(0)
    y_coords = np.empty(0)
    connections = [[] for i in range(n)]
    for i in range(n):
        coords = tuple(generate_node(0, x, 0, y))
        vertices.append(coords)
        x_coords = np.append(x_coords, coords[0])
        y_coords = np.append(y_coords, coords[1])
    print('Nodes generated with success!')
    print('Calculating distances...')
    points = []
    for i in range(n):
        points.append([x_coords[i], y_coords[i]])
    distances = distance_matrix(points, points)
    print('Generating edges...')
    with progressbar.ProgressBar(max_value=len(vertices)) as bar:
        for index, node in enumerate(vertices):
            node_connections = connections[index]
            for i in range(k):
                if i<n:
                    closest_node = np.argpartition(distances[index], i+1)[i+1]
                    if closest_node not in node_connections:
                        node_connections.append(closest_node)
                    if index not in connections[closest_node]:
                        connections[closest_node].append(index)
            connections[index] = node_connections
            bar.update(index)
    return vertices, connections, distances, x_coords, y_coords

def generate_node(x_start, x_limit, y_start, y_limit):
    return round(random.uniform(x_start, x_limit), 1), round(random.uniform(y_start, y_limit), 1)

def complete_bipartite_graph_generator(n, x, y):
    vertices_1 = []
    vertices_2 = [] # particao do meio
    vertices = []
    connections = [[] for i in range(n)]
    x_coords = np.empty(0)
    y_coords = np.empty(0)
    for i in range(n):
        partition = i % 3
        coords = tuple(generate_node(partition * x/3, (partition+1) * x/3, 0, y))
        if partition == 1:
            vertices_2.append(coords)
        else:
            vertices_1.append(coords)
    print('Nodes generated with success!')
    vertices = vertices_1 + vertices_2
    print('Generating edges...')
    with progressbar.ProgressBar(max_value=len(vertices)) as bar:
        for index, vertice in enumerate(vertices_1):
            for i in range(len(vertices_1), len(vertices)):
                connections[index].append(i)
                connections[i].append(index)
            bar.update(index)
    x_coords = [vertice[0] for vertice in vertices]
    y_coords = [vertice[1] for vertice in vertices]
    points = []
    for i in range(n):
        points.append([x_coords[i], y_coords[i]])
    print('Calculating distances...')
    distances = distance_matrix(points, points)
    return vertices, connections, distances, x_coords, y_coords