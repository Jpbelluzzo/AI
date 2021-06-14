from collections import defaultdict
from random import seed
from random import randint
import json
seed(1)

def generate_node(x_limit, y_limit):
    return randint(0, x_limit), randint(0, y_limit)

def knn_generator(k, n, x, y):
    knn_graph = defaultdict(dict)
    for i in range(n):
        knn_graph['x'+str(i)]['x'], knn_graph['x'+str(i)]['y'] = generate_node(x, y)
    return knn_graph

graph = knn_generator(1, 5, 500, 500)
print(json.dumps(graph, indent=4))
