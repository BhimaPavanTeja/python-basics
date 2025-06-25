# def dfs(self, node, adj, visited, result):
#     visited[node] = True
#     result.append(node)
        
#     for x in adj[node]:
#         if visited[x] is False:
#             self.dfs(x, adj, visited, result)

#     def dfsOfGraph(self, adj):
#         n = len(adj)
#         visited = [False] * n
#         result = []

#         self.dfs(0, adj, visited, result)

#         return result


from collections import deque

class Solution:
    def dfs(self, adj):
        n = len(adj)
        visited = [False] * n
        result = []

        s = deque()
        s.append(0)

        while s:
            node = s.pop()

            if visited[node] is False:
                visited[node] = True
                result.append(node)

                # Push x in reverse to maintain order
                for x in reversed(adj[node]):
                    if visited[x] is False:
                        s.append(x)

        return result

    
adj = [[2, 3, 1], [0], [0, 4], [0], [2]]
s = Solution()
print(s.dfs(adj))