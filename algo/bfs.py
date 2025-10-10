graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

def bfs(graph, start_node):
    """
    Performs a Breadth-First Search (BFS) on a graph.

    Args:
        graph (dict): An adjacency list representation of the graph.
                      Keys are nodes, values are lists of connected nodes.
        start_node: The starting node for the BFS traversal.

    Returns:
        list: A list of nodes in the order they were visited during BFS.
    """

    queue = [start_node]
    visited = [start_node]

    while queue:
        next = queue.pop(0)
        for neighbor in graph[next]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
    return visited

print(bfs(graph, 'A'))           
            


