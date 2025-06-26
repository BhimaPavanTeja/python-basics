class Solution:
    def dfs(self, i, adj, vis, recStack):
        vis[i]=True
        recStack[i]=True
        
        for x in adj[i]:
            if not vis[x]:
                if(self.dfs(x,adj,vis,recStack)):
                    return True
            elif recStack[x]==True:
                    return True
        recStack[i] = False
        return False
    def isCycle(self, V, edges):
        adj = [[] for _ in range(V)]
        
        for u,v in edges:
            adj[u].append(v)
            
        vis = [False]*V
        recStack = [False]*V
        
        for i in range(V):
            if vis[i] == False:
                if(self.dfs(i, adj, vis, recStack)):
                    return True
                    
        return False
                    
edges = [[0, 1], [0, 2], [1, 2], [2, 0], [2, 3]]
V = 4
sol = Solution()
print("Graph-01:",end=" ")
print("Cycle Detected" if sol.isCycle(V, edges) else "No Cycle")

edges = [[0, 1], [0, 2], [1, 2], [2, 3]]
V = 4
sol = Solution()
print("Graph-02:", end=" ")
print("Cycle Detected" if sol.isCycle(V, edges) else "No Cycle")
