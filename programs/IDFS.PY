def depth_limited_dfs(graph, node, depth, visited):
    """
    Performs a depth-limited depth-first search (DFS) traversal.

    Args:
    graph (dict): The graph represented as an adjacency list.
    node (str): The current node being visited.
    depth (int): The current depth of the search.
    visited (set): A set of visited nodes.

    Returns:
    bool: True if the search is successful, False otherwise.
    """
    if depth >= 0:  # corrected the condition
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
        if depth == 0:
            return True
        elif depth > 0:
            for neighbor in graph[node]:
                if neighbor not in visited:
                    if depth_limited_dfs(graph, neighbor, depth - 1, visited):
                        return True
    return False

def iddfs(graph, start, max_depth):
    """
    Performs an iterative deepening depth-first search (IDDFS) traversal.

    Args:
    graph (dict): The graph represented as an adjacency list.
    start (str): The starting node for the search.
    max_depth (int): The maximum depth of the search.
    """
    for depth in range(max_depth + 1):  # corrected the range
        print(f"\nDepth: {depth}")
        visited = set()
        depth_limited_dfs(graph, start, depth, visited)

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("IDDFS traversal starting from vertex A up to depth 3:")
iddfs(graph, 'A', 3)