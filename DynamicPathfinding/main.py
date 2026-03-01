# main.py
import tkinter as tk
from grid import Grid
from search_algorithms import greedy_best_first_search, a_star_search
from heuristics import manhattan, euclidean
from dynamic_obstacles import spawn_dynamic_obstacle
from utils import Timer

CELL_SIZE = 30

class PathfindingApp:
    def __init__(self, master, rows=20, cols=20, obstacle_density=0.2):
        self.master = master
        self.rows = rows
        self.cols = cols
        self.grid = Grid(rows, cols, obstacle_density)
        self.grid.random_obstacles()
        self.algorithm = "A*"  # Default
        self.heuristic = manhattan
        self.create_widgets()
        self.draw_grid()

    def create_widgets(self):
        self.canvas = tk.Canvas(self.master, width=self.cols*CELL_SIZE,
                                height=self.rows*CELL_SIZE)
        self.canvas.pack()
        self.run_button = tk.Button(self.master, text="Run", command=self.run_algorithm)
        self.run_button.pack()
        self.canvas.bind("<Button-1>", self.on_click)

    def on_click(self, event):
        col = event.x // CELL_SIZE
        row = event.y // CELL_SIZE
        self.grid.toggle_obstacle(row, col)
        self.draw_grid()

    def draw_grid(self, path=None, visited=None):
        self.canvas.delete("all")
        for r in range(self.rows):
            for c in range(self.cols):
                color = "white"
                if self.grid.grid[r][c] == 1:
                    color = "black"
                elif (r, c) == self.grid.start:
                    color = "blue"
                elif (r, c) == self.grid.goal:
                    color = "red"
                elif visited and (r, c) in visited:
                    color = "yellow"
                elif path and (r, c) in path:
                    color = "green"
                self.canvas.create_rectangle(c*CELL_SIZE, r*CELL_SIZE,
                                             (c+1)*CELL_SIZE, (r+1)*CELL_SIZE,
                                             fill=color, outline="gray")

    def run_algorithm(self):
        if self.algorithm == "A*":
            search_fn = lambda: a_star_search(self.grid, self.grid.start, self.grid.goal, self.heuristic)
        else:
            search_fn = lambda: greedy_best_first_search(self.grid, self.grid.start, self.grid.goal, self.heuristic)
        
        with Timer() as t:
            path = search_fn()
        
        self.draw_grid(path=path)
        print(f"Execution Time: {t.interval:.2f} ms")
        print(f"Path Length: {len(path)}")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Dynamic Pathfinding Agent")
    app = PathfindingApp(root)
    root.mainloop()