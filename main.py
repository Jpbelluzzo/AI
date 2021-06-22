from graphs_gen import knn_generator
import searches
import json
import matplotlib.pyplot as plt

graph, x_coords, y_coords, connections = knn_generator(5, 50, 500, 500)

for i in range(len(graph)):
    plt.annotate(str(i), (x_coords[i],y_coords[i]))
plt.scatter(x_coords, y_coords, marker='o')
for index, nodes in enumerate(connections):
    point1 = index
    for node in nodes:
        point2 = node
        plt.plot((x_coords[point1], x_coords[point2]),(y_coords[point1], y_coords[point2]),'r')

dfs_search = searches.depth_first_search(22, 21, graph, connections)
print(dfs_search)

bfs_search = searches.breadth_first_search(22, 21, graph, connections)
print(bfs_search)

plt.savefig('teste.png')
#print(json.dumps(dict.__repr__(graph), indent=4))