class Solution():
    def largestSumCycle(self, N, Edge):
        visited = [False] * N
        inStack = [False] * N
        maxSum = -1
        
        def dfs(node, path, indexMap):
            nonlocal maxSum
            visited[node] = True
            inStack[node] = True
            path.append(node)
            indexMap[node] = len(path) - 1

            next_node = Edge[node]
            if next_node != -1:
                if not visited[next_node]:
                    dfs(next_node, path, indexMap)
                elif inStack[next_node]:
                    # Cycle found
                    cycle_start = indexMap[next_node]
                    cycle_nodes = path[cycle_start:]
                    maxSum = max(maxSum, sum(cycle_nodes))

            inStack[node] = False
            path.pop()
            indexMap.pop(node, None)


        for i in range(N):
            if not visited[i]:
                dfs(i, [], {})

        return maxSum

N = 4
Edge = [1, 2, 0, -1]
sol = Solution()
print(sol.largestSumCycle(N, Edge))