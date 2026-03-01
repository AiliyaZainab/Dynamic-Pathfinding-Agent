# grid.py
import random

class Grid:
    def __init__(self, rows, cols, obstacle_density=0.3):
        self.rows = rows
        self.cols = cols
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]
        self.start = (0, 0)
        self.goal = (rows-1, cols-1)
        self.obstacle_density = obstacle_density

    def random_obstacles(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if (r, c) != self.start and (r, c) != self.goal:
                    self.grid[r][c] = 1 if random.random() < self.obstacle_density else 0

    def toggle_obstacle(self, row, col):
        if (row, col) != self.start and (row, col) != self.goal:
            self.grid[row][col] = 0 if self.grid[row][col] == 1 else 1

    def neighbors(self, node):
        r, c = node
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        result = []
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols and self.grid[nr][nc] == 0:
                result.append((nr, nc))
        return result