# heuristics.py
import math

def manhattan(node, goal):
    x1, y1 = node
    x2, y2 = goal
    return abs(x1 - x2) + abs(y1 - y2)

def euclidean(node, goal):
    x1, y1 = node
    x2, y2 = goal
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)