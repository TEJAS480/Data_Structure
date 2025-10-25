import sys

# Number of locations
N = 5

# Mapping nodes: A=0, B=1, C=2, D=3, E=4

# Adjacency matrix representing time to travel between locations
# 0 means no direct path
adj_matrix = [
    [0, 10, 15, 0, 0],  # A
    [10, 0, 35, 25, 0],  # B
    [15, 35, 0, 30, 20],  # C
    [0, 25, 30, 0, 15],  # D
    [0, 0, 20, 15, 0]  # E
]


def nearest_neighbor(start):
    visited = [False] * N
    visited[start] = True
    path = [start]
    total_time = 0
    current = start

    for _ in range(N - 1):
        nearest = -1
        min_time = sys.maxsize
        for i in range(N):
            if not visited[i] and adj_matrix[current][i] != 0 and adj_matrix[current][i] < min_time:
                min_time = adj_matrix[current][i]
                nearest = i
        visited[nearest] = True
        path.append(nearest)
        total_time += min_time
        current = nearest

    # Optionally return to start
    if adj_matrix[current][start] != 0:
        total_time += adj_matrix[current][start]
        path.append(start)

    return path, total_time


# Run nearest neighbor from A (0)
path, total_time = nearest_neighbor(0)

print("Delivery sequence:", " -> ".join(chr(node + ord('A')) for node in path))
print("Total delivery time:", total_time)
