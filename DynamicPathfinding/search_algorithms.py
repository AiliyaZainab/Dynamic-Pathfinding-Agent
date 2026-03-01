# search_algorithms.py
import heapq

def greedy_best_first_search(grid, start, goal, heuristic):
    open_set = []
    heapq.heappush(open_set, (heuristic(start, goal), start))
    came_from = {}
    visited = set()
    
    while open_set:
        _, current = heapq.heappop(open_set)
        if current == goal:
            return reconstruct_path(came_from, start, goal)
        visited.add(current)
        
        for neighbor in grid.neighbors(current):
            if neighbor not in visited:
                heapq.heappush(open_set, (heuristic(neighbor, goal), neighbor))
                if neighbor not in came_from:
                    came_from[neighbor] = current
    return []

def a_star_search(grid, start, goal, heuristic):
    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start, goal), 0, start))
    came_from = {}
    g_score = {start: 0}
    
    while open_set:
        _, cost, current = heapq.heappop(open_set)
        if current == goal:
            return reconstruct_path(came_from, start, goal)
        
        for neighbor in grid.neighbors(current):
            tentative_g = g_score[current] + 1
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score, tentative_g, neighbor))
                came_from[neighbor] = current
    return []

def reconstruct_path(came_from, start, goal):
    path = [goal]
    while path[-1] != start:
        path.append(came_from[path[-1]])
    path.reverse()
    return path