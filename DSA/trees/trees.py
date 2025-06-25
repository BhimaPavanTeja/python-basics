from collections import deque

s = deque()

tree = {}
tree["A"] = ["B", "C", "D"]
tree["B"] = ["E", "F"]
tree["C"] = ["G", "H"]
tree["D"] = []
tree["E"] = []
tree["F"] = []
tree["G"] = []
tree["H"] = []

s += tree["A"]

while s:
    k = s.popleft()
    print(k)
    s += tree[k]
