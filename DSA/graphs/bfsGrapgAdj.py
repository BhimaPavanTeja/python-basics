from collections import deque
class Solution:
    # Breadth First Search Traversal of given graph.
    def bfs(self, adj):
        # code here
        n = len(adj)
        visited = [False]*n
        res = []
        s = deque()
        
        s.append(0)
        visited[0] = True
        
        while s:
            k = s.popleft()
            res.append(k)
            
            for x in adj[k]:
                if visited[x] is False:
                    visited[x] = True
                    s.append(x)
            
        return res

# Adjacency list of graph
adj = [[2, 3, 1], [0], [0, 4], [0], [2]]
s = Solution()
print(s.bfs(adj))