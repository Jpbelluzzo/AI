from random import randrange
import progressbar
import graphs_gen
import searches
import time
import matplotlib.pyplot as plt

GRAPH_GEN_ALGORITHM = 1
SEARCH_ALGORITHM = 5
k = 4
n = 3000
x = 7000
y = 7000
start_node = 1424
end_node = 2111

if GRAPH_GEN_ALGORITHM == 1:
    vertices, connections, distances, x_coords, y_coords = graphs_gen.knn_generator(k, n, x, y)
elif GRAPH_GEN_ALGORITHM == 2:
    vertices, connections, distances, x_coords, y_coords = graphs_gen.complete_bipartite_graph_generator(n, x, y)

if SEARCH_ALGORITHM == 1:
    print('Executing depth-first search...')
    plot_title = 'Busca em profundidade' 
    start = time.time()
    path = searches.depth_first_search(start_node, end_node, vertices, connections)
    end = time.time()
    print('Time to execute search algorithm: ' + str(end-start))
elif SEARCH_ALGORITHM == 2:
    print('Executing breadth-first search...')
    plot_title = 'Busca em largura' 
    start = time.time()
    path = searches.breadth_first_search(start_node, end_node, vertices, connections)
    end = time.time()
    print('Time to execute search algorithm: ' + str(end-start))
    #print(path)
elif SEARCH_ALGORITHM == 3:
    print('Executing best-first search...')
    plot_title = 'Busca best-first' 
    start = time.time()
    path = searches.best_first_search(start_node, end_node, vertices, connections, distances)
    end = time.time()
    print('Time to execute search algorithm: ' + str(end-start))
    #print(path)
elif SEARCH_ALGORITHM == 4:
    print('Executing A-Algorithm search...')
    plot_title = 'Algoritmo A' 
    start = time.time()
    path = searches.A_search(start_node, end_node, vertices, connections, distances)
    end = time.time()
    print('Time to execute search algorithm: ' + str(end-start))
    #print(path)
elif SEARCH_ALGORITHM == 5:
    print('Executing A*-Algorithm search...')
    plot_title = 'Algoritmo A*' 
    start = time.time()
    path = searches.A_star_search(start_node, end_node, vertices, connections, distances)
    end = time.time()
    print('Time to execute search algorithm: ' + str(end-start))
    #print(path)

distance = graphs_gen.get_path_distance(path, distances)

if path:
    print('Generating plot...')
    fig, ax = plt.subplots()

    ax.scatter(x_coords, y_coords, zorder=2, marker='o', color='#0015ff', s=3)
    ax.scatter([x_coords[start_node], x_coords[end_node]], [y_coords[start_node], y_coords[end_node]], zorder=3, marker='o', color='#000000')
    ax.annotate('ORIGEM', [x_coords[start_node], y_coords[start_node]], weight='bold', size=6)
    ax.annotate('DESTINO', [x_coords[end_node], y_coords[end_node]], weight='bold', size=6)
    # for i in range(len(vertices)):
    #     plt.annotate(str(i), (x_coords[i],y_coords[i]))
    print('Plotting graph...')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(plot_title, loc='left')
    if GRAPH_GEN_ALGORITHM == 1:
        text = '\n'.join((
            r'$k=%d$' % (k, ),
            r'$n=%d$' % (n, ),
            r'$d=%.2f$'% (distance, )))
    elif GRAPH_GEN_ALGORITHM == 2:
        text = '\n'.join((
            r'$n=%d$' % (n, ),
            r'$d=%.2f$' % (distance, )))

    props = dict(boxstyle='round', facecolor='wheat', alpha=0.9)
    # place a text box in upper right in axes coords
    ax.text(0.8, 0.97, text, transform=plt.gcf().transFigure, fontsize=12,
        verticalalignment='top', bbox=props)

    with progressbar.ProgressBar(max_value=len(connections)) as bar:
        for index, nodes in enumerate(connections):
            point1 = index
            for node in nodes:
                point2 = node
                plt.plot((x_coords[point1], x_coords[point2]),(y_coords[point1], y_coords[point2]), '#fcd703', zorder=1)
            bar.update(index)

    print('Plotting search path...')

    with progressbar.ProgressBar(max_value=len(path)):
        for i in range(1, len(path)):
            plt.plot((x_coords[path[i]], x_coords[path[i-1]]),(y_coords[path[i]], y_coords[path[i-1]]),'#000000')
            # plt.annotate(str(i), (x_coords[path[i]],y_coords[path[i]]))
            bar.update(i)

    if (GRAPH_GEN_ALGORITHM == 2):
        plt.vlines([x/3, 2*x/3], 0, y, linestyles='dashed', colors='red')

    # plt.savefig('/mnt/c/Users/bellu/Desktop/teste.png')
    plt.savefig('graph.png')