def nearestMeetingCell(edges, node1, node2):
    def get_distances(start):
        n = len(edges)
        dist = [-1] * n
        curr = start
        d = 0
        while curr != -1 and dist[curr] == -1:
            dist[curr] = d
            d += 1
            curr = edges[curr]
        return dist

    dist1 = get_distances(node1)
    dist2 = get_distances(node2)
    
    min_distance = float('inf')
    meeting_cell = -1

    for i in range(len(edges)):
        if dist1[i] != -1 and dist2[i] != -1:
            max_dist = max(dist1[i], dist2[i])
            if max_dist < min_distance:
                min_distance = max_dist
                meeting_cell = i

    return meeting_cell

# Input reading
n = 23
edges = [4, 4, 1, 4, 13, 8, 8, 8, 0, 8, 14, 9, 15, 11, -1, 10, 15, 22, 22, 22, 22, 22, 21]
node1, node2 = 9, 2

# Function call
print(nearestMeetingCell(edges, node1, node2))