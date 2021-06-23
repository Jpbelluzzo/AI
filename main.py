import progressbar
from graphs_gen import knn_generator
import searches
import json
import matplotlib.pyplot as plt

vertices, connections, distances, x_coords, y_coords = knn_generator(3, 7000, 7000, 7000)

print('Executing search...')

path = searches.depth_first_search(1232, 676, vertices, connections)
print(path)

#path = searches.breadth_first_search(12, 10, vertices, connections)
#print(path)

# path = searches.best_first_search(8, 10, vertices, connections, distances)
#print(path)

print('Generating plot...')

#for i in range(len(vertices)):
#    plt.annotate(str(i), (x_coords[i],y_coords[i]))
plt.scatter(x_coords, y_coords, marker='o')
with progressbar.ProgressBar(max_value=len(connections)) as bar:
    for index, nodes in enumerate(connections):
        point1 = index
        for node in nodes:
            point2 = node
            #print(str(point1) + ' ' + str(point2))
            plt.plot((x_coords[point1], x_coords[point2]),(y_coords[point1], y_coords[point2]),'#eaff00')
        bar.update(index)
with progressbar.ProgressBar(max_value=len(path)):
    for i in range(1, len(path)):
        plt.plot((x_coords[path[i]], x_coords[path[i-1]]),(y_coords[path[i]], y_coords[path[i-1]]),'#000000')
        bar.update(i)

plt.savefig('teste.png')
#print(json.dumps(dict.__repr__(graph), indent=4))