from FibonacciHeap import FibHeap
from priority_queue import FibPQ, HeapPQ, QueuePQ

# This implementatoin of A* is almost identical to the Dijkstra implementation. So for clarity I've removed all comments, and only added those
# Specifically showing the difference between dijkstra and A*

from FibonacciHeap import FibHeap
from priority_queue import FibPQ, HeapPQ, QueuePQ

# This implementatoin of A* is almost identical to the Dijkstra implementation. So for clarity I've removed all comments, and only added those
# Specifically showing the difference between dijkstra and A*

from FibonacciHeap import FibHeap
from priority_queue import FibPQ, HeapPQ, QueuePQ

# This implementatoin of A* is almost identical to the Dijkstra implementation. So for clarity I've removed all comments, and only added those
# Specifically showing the difference between dijkstra and A*

from FibonacciHeap import FibHeap
from priority_queue import FibPQ, HeapPQ, QueuePQ

# This implementatoin of A* is almost identical to the Dijkstra implementation. So for clarity I've removed all comments, and only added those
# Specifically showing the difference between dijkstra and A*

from FibonacciHeap import FibHeap
from priority_queue import FibPQ, HeapPQ, QueuePQ

# This implementatoin of A* is almost identical to the Dijkstra implementation. So for clarity I've removed all comments, and only added those
# Specifically showing the difference between dijkstra and A*

from FibonacciHeap import FibHeap
from priority_queue import FibPQ, HeapPQ, QueuePQ

# This implementatoin of A* is almost identical to the Dijkstra implementation. So for clarity I've removed all comments, and only added those
# Specifically showing the difference between dijkstra and A*

from FibonacciHeap import FibHeap
from priority_queue import FibPQ, HeapPQ, QueuePQ

# This implementatoin of A* is almost identical to the Dijkstra implementation. So for clarity I've removed all comments, and only added those
# Specifically showing the difference between dijkstra and A*

from FibonacciHeap import FibHeap
from priority_queue import FibPQ, HeapPQ, QueuePQ

# This implementatoin of A* is almost identical to the Dijkstra implementation. So for clarity I've removed all comments, and only added those
# Specifically showing the difference between dijkstra and A*

def solve(maze):
    width = maze.width
    total = maze.width * maze.height

    start = maze.start
    startpos = start.Position
    end = maze.end
    endpos = end.Position

    visited = [False] * total
    prev = [None] * total

    infinity = float("inf")
    distances = [infinity] * total

    # The priority queue. There are multiple implementations in priority_queue.py
    # unvisited = FibHeap()
    unvisited = HeapPQ()
    # unvisited = FibPQ()
    # unvisited = QueuePQ()
