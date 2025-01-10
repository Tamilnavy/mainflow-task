import random
from collections import deque

# Maze Generation using Recursive Backtracking
def generate_maze(width, height):
    maze = [[1] * width for _ in range(height)]
    def carve_passages(x, y):
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx * 2, y + dy * 2
            if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == 1:
                maze[ny][nx] = maze[y + dy][x + dx] = 0
                carve_passages(nx, ny)
    maze[1][1] = 0
    carve_passages(1, 1)
    return maze

# Solve the maze using BFS
def bfs_solve(maze, start, end):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([start])
    visited = {start}
    parent = {start: None}

    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            break
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(maze[0]) and 0 <= ny < len(maze) and maze[ny][nx] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))
                parent[(nx, ny)] = (x, y)

    path = []
    current = end
    while current != start:
        path.append(current)
        current = parent[current]
    path.append(start)
    return path[::-1]

# Print the maze
def print_maze(maze, path=[]):
    for y, row in enumerate(maze):
        print(''.join(['#' if cell == 1 else (' ' if (x, y) not in path else '.') for x, cell in enumerate(row)]))

# Main program
width, height = 21, 21
maze = generate_maze(width, height)
start, end = (1, 1), (width - 2, height - 2)
path = bfs_solve(maze, start, end)

# Print the maze with the path
print("Generated Maze with Path:")
print_maze(maze, path)
