
def solve_maze(maze, x=0, y=0, path=[]):
    if x < 0 or y < 0 or x >= len(maze) or y >= len(maze[0]) or maze[x][y] == 0:
        return False
    if (x, y) == (len(maze) - 1, len(maze[0]) - 1):
        path.append((x, y))
        print("Path found:", path)
        return True
    maze[x][y] = 0
    path.append((x, y))
    if (solve_maze(maze, x + 1, y, path) or solve_maze(maze, x, y + 1, path) or
        solve_maze(maze, x - 1, y, path) or solve_maze(maze, x, y - 1, path)):
        return True
    path.pop()
    return False

maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]
solve_maze(maze)
