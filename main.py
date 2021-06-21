from graphs_gen import knn_generator
import dfs
import json
import matplotlib.pyplot as plt

graph, x_coords, y_coords, connections = knn_generator(4, 30, 500, 500)

for i in range(len(graph)):
    plt.annotate(str(i), (x_coords[i],y_coords[i]))

plt.scatter(x_coords, y_coords, marker='o')
for connection in connections:
    point1 = connection[0]
    point2 = connection[1]
    plt.plot((graph[point1]['x'], graph[point2]['x']),(graph[point1]['y'], graph[point2]['y']),'r')

dfs_search = dfs.depth_first_search(11, 23, graph, connections)
print(dfs_search)

plt.savefig('teste.png')
#print(json.dumps(dict.__repr__(graph), indent=4))