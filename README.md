# Dynamic Pathfinding Agent

A Python project that implements a **dynamic pathfinding agent** navigating a grid from a **Start** node to a **Goal** node using **Greedy Best-First Search (GBFS)** and **A*** algorithms. The agent handles **dynamic obstacles** appearing while moving and efficiently **re-plans paths in real-time**.

---

## Features

- **Dynamic Grid:** Set custom rows and columns.  
- **Random Obstacles:** Generate obstacles with user-defined density.  
- **Manual Editing:** Add or remove obstacles by clicking on the grid.  
- **Heuristic Selection:** Choose between **Manhattan** or **Euclidean** distance.  
- **Algorithms:**  
  - **Greedy Best-First Search (GBFS):** Fast but not always optimal.  
  - **A* Search:** Guarantees optimal path with admissible heuristics.  
- **Dynamic Obstacles:** Obstacles can spawn while the agent is moving.  
- **Re-planning:** Agent detects blocked paths and recalculates efficiently.  
- **GUI Visualization:**  
  - Frontier nodes: Yellow  
  - Visited nodes: Red/Blue  
  - Final path: Green  
- **Metrics Dashboard:** Nodes visited, path cost, execution time.

---

## Dependencies

- Python 3.x  
- [Pygame](https://www.pygame.org/) or Tkinter (for GUI)

Install Pygame using pip:

```bash
pip install pygame
