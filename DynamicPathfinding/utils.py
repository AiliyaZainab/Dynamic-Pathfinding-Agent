# utils.py
import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self
    def __exit__(self, *args):
        self.end = time.time()
        self.interval = (self.end - self.start) * 1000  # milliseconds

def print_metrics(nodes_visited, path_length, execution_time):
    print(f"Nodes Visited: {nodes_visited}")
    print(f"Path Cost: {path_length}")
    print(f"Execution Time: {execution_time:.2f} ms")