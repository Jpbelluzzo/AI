# Depth-First Search Algorithm

def depth_first_search(init_node, end_node, graph, connections):
    visited = []
    visited = dfs_recursion(init_node, end_node, visited, graph, connections)
    return visited

def dfs_recursion(node, end_node, visited, graph, connections):
    visited.append(node)
    if node == end_node:
        return visited
    neighbours = connections[node]
    for neighbour in neighbours:
        if neighbour not in visited:
            dfs_recursion(neighbour, end_node, visited, graph, connections)
            if(visited[-1] == end_node):
                return visited

# Breadth-First Search Algorithm

def breadth_first_search(init_node, end_node, graph, connections):
    path = []
    queue = [init_node]
    bfs_recursion(init_node, end_node, path, queue, graph, connections)
    return path

def bfs_recursion(node, end_node, path, queue, graph, connections):
    path.append(node)
    if node == end_node:
        return path
    neighbours = connections[node]
    for neighbour in neighbours:
        if neighbour not in queue:        
            queue += [neighbour]
    del(queue[0])
    bfs_recursion(queue[0], end_node, path, queue, graph, connections)