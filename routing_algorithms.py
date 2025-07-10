from collections import deque
import heapq

# -------------------------
# Dijkstra’s Algorithm
# -------------------------
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_dist, current_node = heapq.heappop(pq)
        if current_dist > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances

# -------------------------
# BFS (Breadth-First Search)
# -------------------------
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    order = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            order.append(node)
            for neighbor in graph.get(node, []):
                queue.append(neighbor)
    return order

# -------------------------
# Union-Find (Disjoint Set)
# -------------------------
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            self.parent[root_v] = root_u

    def connected(self, u, v):
        return self.find(u) == self.find(v)

# -------------------------
# Flood-Fill Algorithm
# -------------------------
def flood_fill(grid, x, y, target, replacement):
    rows, cols = len(grid), len(grid[0])
    if grid[x][y] != target:
        return

    def dfs(i, j):
        if i < 0 or i >= rows or j < 0 or j >= cols:
            return
        if grid[i][j] != target:
            return
        grid[i][j] = replacement
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)

    dfs(x, y)
