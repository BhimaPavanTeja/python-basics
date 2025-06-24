from collections import deque

s = deque()
graph = {}
graph["A"] = ["B", "C","D"]
graph["B"] = ["E"]
graph["C"] = ["F"]
graph["D"] = ["G"]
graph["G"] = ["F"]
graph["F"] = ["H"]
graph["E"] = ["H"]
graph["H"] = []

def bfs(start):
    visited = set()
    s.append(start)
    while s:
        k = s.popleft()
        if k not in visited:
            print(k, end=" ")
            visited.add(k)
            for i in graph[k]:
                if i not in visited and i not in s:
                    s.append(i)

bfs("A")