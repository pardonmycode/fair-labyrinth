from FibonacciHeap import FibHeap
from priority_queue import FibPQ, HeapPQ, QueuePQ

def solve(maze):
    # Width is used for indexing, total is used for array sizes
    width = maze.width
    total = maze.width * maze.height

    # Start node, end node
    start = maze.start
    startpos = start.Position
    end = maze.end
    endpos = end.Position

    # Visited holds true/false on whether a node has been seen already. Used to stop us returning to nodes multiple times
    visited = [False] * total

    # Previous holds a link to the previous node in the path. Used at the end for reconstructing the route
    prev = [None] * total

    # Distances holds the distance to any node taking the best known path so far. Better paths replace worse ones as we find them.
    # We start with all distances at infinity
    infinity = float("inf")
    distances = [infinity] * total

    # The priority queue. There are multiple implementations in priority_queue.py
    # unvisited = FibHeap()
    unvisited = HeapPQ()
    # unvisited = FibPQ()
    # unvisited = QueuePQ()

    # This index holds all priority queue nodes as they are created. We use this to decrease the key of a specific node when a shorter path is found.
    # This isn't hugely memory efficient, but likely to be faster than a dictionary or similar.
    nodeindex = [None] * total

    # To begin, we set the distance to the start to zero (we're there) and add it into the unvisited queue
    distances[start.Position[0] * width + start.Position[1]] = 0
    startnode = FibHeap.Node(0, start)
    nodeindex[start.Position[0] * width + start.Position[1]] = startnode
    unvisited.insert(startnode)

    # Zero nodes visited, and not completed yet.
    count = 0
    completed = False