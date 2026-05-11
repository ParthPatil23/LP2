from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

def bfs_recursive(queue, visited):
    if not queue:
        return

    node = queue.popleft()
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)

    bfs_recursive(queue, visited)

# Start BFS
start = 'A'
visited = set([start])
queue = deque([start])

print("Recursive BFS Traversal:")
bfs_recursive(queue, visited)