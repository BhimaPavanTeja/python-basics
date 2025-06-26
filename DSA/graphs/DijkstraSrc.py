import heapq
class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        adj = [[] for _ in range(V)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        
        dis = [float('inf')]*V
        dis[src]=0
        
        pq = []
        heapq.heappush(pq, (0,src))
        
        while pq:
            d, u = heapq.heappop(pq)
            if d > dis[u]:
                continue
            for v,w in adj[u]:
                if dis[v] > dis[u]+w:
                    dis[v] = dis[u]+w
                    heapq.heappush(pq, (dis[v], v))
                    
        return dis
        
edges = [[0, 1, 1], [1, 2, 3], [0, 2, 6]]
V = 3
src = 2
sol = Solution()
print(f"Shortest distances from {src}:", sol.dijkstra(V, edges, src))