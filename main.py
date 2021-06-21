from graphs_gen import knn_generator
import searches
import json
import matplotlib.pyplot as plt

graph, x_coords, y_coords, connections = knn_generator(4, 15, 500, 500)

for i in range(len(graph)):
    plt.annotate(str(i), (x_coords[i],y_coords[i]))

plt.scatter(x_coords, y_coords, marker='o')
for connection in connections:
    point1 = connection[0]
    point2 = connection[1]
    plt.plot((graph[point1]['x'], graph[point2]['x']),(graph[point1]['y'], graph[point2]['y']),'r')

dfs_search = searches.depth_first_search(11, 8, graph, connections)
print(dfs_search)

bfs_search = searches.breadth_first_search(11, 8, graph, connections)
print(bfs_search)

plt.savefig('teste.png')
#print(json.dumps(dict.__repr__(graph), indent=4))