# dynamic_obstacles.py
import random

def spawn_dynamic_obstacle(grid, probability=0.05):
    r = random.randint(0, grid.rows-1)
    c = random.randint(0, grid.cols-1)
    if (r, c) != grid.start and (r, c) != grid.goal:
        if random.random() < probability:
            grid.grid[r][c] = 1
            return (r, c)
    return None