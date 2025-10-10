def dfs_iterative(graph, start_node):
    """
    Performs a Depth-First Search (DFS) on a graph.

    Args:
        graph (dict): An adjacency list representation of the graph.
                      Keys are nodes, values are lists of connected nodes.
        start_node: The starting node for the DFS traversal.
        visited (set, optional): A set to keep track of visited nodes.
                                 Defaults to None for initial call.

    Returns:
        list: A list of nodes in the order they were visited during DFS.
    """
    visited = set()
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)
    return visited

def dfs_recursive(graph, start_node, visited=None):
    if visited == None:
        visited = set()
    visited.add(start_node)
    for neighbor in graph[start_node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)
    return visited