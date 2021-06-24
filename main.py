from random import randrange
import progressbar
import graphs_gen
import searches
import json
import matplotlib.pyplot as plt

GRAPH_GEN_ALGORITHM = 2
SEARCH_ALGORITHM = 1
k = 3
n = 12
x = 7000
y = 7000
start_node = 4
end_node = 10
if GRAPH_GEN_ALGORITHM == 1:
    vertices, connections, distances, x_coords, y_coords = graphs_gen.knn_generator(k, n, x, y)
elif GRAPH_GEN_ALGORITHM == 2:
    vertices, connections, distances, x_coords, y_coords = graphs_gen.complete_bipartite_graph_generator(n, x, y)

print('Executing search...')

if SEARCH_ALGORITHM == 1:
    path = searches.depth_first_search(start_node, end_node, vertices, connections)
    #print(path)
elif SEARCH_ALGORITHM == 2:
    path = searches.breadth_first_search(start_node, end_node, vertices, connections)
    #print(path)
elif SEARCH_ALGORITHM == 3:
    path = searches.best_first_search(start_node, end_node, vertices, connections, distances)
    #print(path)
elif SEARCH_ALGORITHM == 4:
    path = searches.A_search(start_node, end_node, vertices, connections, distances)
    #print(path)
elif SEARCH_ALGORITHM == 5:
    path = searches.A_star_search(start_node, end_node, vertices, connections, distances)
    #print(path)

if path:
    print('Generating plot...')

    #for i in range(len(vertices)):
    #    plt.annotate(str(i), (x_coords[i],y_coords[i]))
    plt.scatter(x_coords, y_coords, marker='o')

    print('Plotting graph...')

    with progressbar.ProgressBar(max_value=len(connections)) as bar:
        for index, nodes in enumerate(connections):
            point1 = index
            for node in nodes:
                point2 = node
                plt.plot((x_coords[point1], x_coords[point2]),(y_coords[point1], y_coords[point2]),'#eaff00')
            bar.update(index)

    print('Plotting search path...')

    with progressbar.ProgressBar(max_value=len(path)):
        for i in range(1, len(path)):
            plt.plot((x_coords[path[i]], x_coords[path[i-1]]),(y_coords[path[i]], y_coords[path[i-1]]),'#000000')
            bar.update(i)

    if (GRAPH_GEN_ALGORITHM == 2):
        plt.vlines([x/3, 2*x/3], 0, y, linestyles='dashed', colors='red')
    
    plt.savefig('teste.png')
#print(json.dumps(dict.__repr__(graph), indent=4))