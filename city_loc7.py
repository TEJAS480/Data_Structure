from collections import deque

# Number of locations
N = 5

# Mapping nodes: A=0, B=1, C=2, D=3, E=4

# Adjacency Matrix for DFS
adj_matrix = [
    [0, 1, 1, 0, 0],  # A connected to B, C
    [1, 0, 0, 1, 0],  # B connected to A, D
    [1, 0, 0, 1, 1],  # C connected to A, D, E
    [0, 1, 1, 0, 1],  # D connected to B, C, E
    [0, 0, 1, 1, 0]  # E connected to C, D
]

# Adjacency List for BFS
adj_list = [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if adj_matrix[i][j] == 1:
            adj_list[i].append(j)


# DFS using adjacency matrix
def dfs(node, visited):
    visited[node] = True
    print(chr(node + ord('A')), end=" ")

    for i in range(N):
        if adj_matrix[node][i] == 1 and not visited[i]:
            dfs(i, visited)


# BFS using adjacency list
def bfs(start):
    visited = [False] * N
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        print(chr(node + ord('A')), end=" ")
        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)


# Run DFS from A
print("DFS starting from A: ", end="")
visited = [False] * N
dfs(0, visited)
print()

# Run BFS from A
print("BFS starting from A: ", end="")
bfs(0)
print()
