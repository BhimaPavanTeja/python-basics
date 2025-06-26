from collections import deque

class Solution:
    def topoSort(self, V, edges):
        # Step 1: Build adjacency list and in-degree list
        adj = [[] for _ in range(V)]
        in_degree = [0] * V

        for u, v in edges:
            adj[u].append(v)
            in_degree[v] += 1

        # Step 2: Initialize queue with nodes having 0 in-degree
        queue = deque([i for i in range(V) if in_degree[i] == 0])
        topo_order = []

        while queue:
            node = queue.popleft()
            topo_order.append(node)
            for x in adj[node]:
                in_degree[x] -= 1
                if in_degree[x] == 0:
                    queue.append(x)

        # Return topological order
        return topo_order if len(topo_order) == V else []

# Function to check if the topological order is valid
def isValidTopoOrder(V, edges, order):
    pos = [0] * V
    for i, val in enumerate(order):
        pos[val] = i  # Record position of each node

    for u, v in edges:
        if pos[u] > pos[v]:
            return False  # u must come before v
    return True

V = 4
edges = [[3, 0], [1, 0], [2, 0]]
obj = Solution()
topo = obj.topoSort(V, edges)
print("Topological Sort:", topo)
print("Valid:", isValidTopoOrder(V, edges, topo))

# Example 2
V = 6
edges = [[1, 3], [2, 3], [4, 1], [4, 0], [5, 0], [5, 2]]
topo = obj.topoSort(V, edges)
print("Topological Sort:", topo)
print("Valid:", isValidTopoOrder(V, edges, topo))  # Output: True
