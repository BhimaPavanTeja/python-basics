import heapq

class Solution:
    # Returns shortest distance from src to dest
    def dijkstra(self, V, edges, src, dest):
        adj = [[] for _ in range(V)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))  # Because the graph is undirected
        
        dis = [float('inf')] * V
        dis[src] = 0
        
        pq = []
        heapq.heappush(pq, (0, src))
        
        while pq:
            d, u = heapq.heappop(pq)
            
            if u == dest:
                return dis[u]  # Early return if destination is reached
            
            if d > dis[u]:
                continue
            
            for v, w in adj[u]:
                if dis[v] > dis[u] + w:
                    dis[v] = dis[u] + w
                    heapq.heappush(pq, (dis[v], v))
        
        return -1  # If destination is not reachable

# Example usage
edges = [[0, 1, 1], [1, 2, 3], [0, 2, 6]]
V = 3
src = 2
dest = 0

sol = Solution()
print(f"Shortest distance from {src} -> {dest} is", sol.dijkstra(V, edges, src, dest))
