def depth_first_search(init_node, end_node, graph, connections):
    visited = []
    visited = dfs_recursion(init_node, end_node, visited, graph, connections)
    return visited

def dfs_recursion(node, end_node, visited, graph, connections):
    visited.append(node)
    if node == end_node:
        return visited
    neighbours = graph[node]['connections']
    for neighbour in neighbours:
        if neighbour not in visited:
            #print(node, neighbour)
            dfs_recursion(neighbour, end_node, visited, graph, connections)
            if(visited[-1] == end_node):
                return visited