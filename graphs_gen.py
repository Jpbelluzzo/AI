from collections import defaultdict
from os import close
from random import seed
import math
import random
from matplotlib.pyplot import connect
import numpy as np
from numpy.core.defchararray import index
from scipy.spatial import distance, distance_matrix
import progressbar
seed(3)

def knn_generator(k, n, x, y):
    vertices = []
    x_coords = np.empty(0)
    y_coords = np.empty(0)
    connections = [[] for i in range(n)]
    for i in range(n):
        coords = tuple(generate_node(x, y))
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

def generate_node(x_limit, y_limit):
    return (random.random())*x_limit, (random.random())*y_limit
