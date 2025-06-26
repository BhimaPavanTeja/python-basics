class Solution:
    def dfs(self, i, vis, edges, prev):
        vis[i] = True
        
        for x in edges[i]:
            if vis[x] is False:
                if self.dfs(x, vis, edges, i):
                    return True
            else:
                if x != prev:
                    return True
                    
        return False

    def isCycle(self, V, edges_list):
        # Convert edge list to adjacency list
        edges = [[] for _ in range(V)]
        for u, v in edges_list:
            edges[u].append(v)
            edges[v].append(u)
            
        ans = False
        vis = [False]*V
        
        for i in range(V):
            if vis[i] is False:
                ans = ans or self.dfs(i,vis,edges,-1)
        
        return ans
    
edges_list = [[0, 1], [0, 2], [1, 2], [2, 3]]
V = 4

sol = Solution()
print("It is a Cyclic Graph" if sol.isCycle(V, edges_list) else "No Cycle")

