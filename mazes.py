class Maze:
    class Node:
        def __init__(self, position):
            self.Position = position
            self.Neighbours = [None, None, None, None]
            #self.Weights = [0, 0, 0, 0]
class Maze:
    class Node:
        def __init__(self, position):
            self.Position = position
            self.Neighbours = [None, None, None, None]
            #self.Weights = [0, 0, 0, 0]
class Maze:
    class Node:
        def __init__(self, position):
            self.Position = position
            self.Neighbours = [None, None, None, None]
            #self.Weights = [0, 0, 0, 0]
class Maze:
    class Node:
        def __init__(self, position):
            self.Position = position
            self.Neighbours = [None, None, None, None]
            #self.Weights = [0, 0, 0, 0]
class Maze:
    class Node:
        def __init__(self, position):
            self.Position = position
            self.Neighbours = [None, None, None, None]
            #self.Weights = [0, 0, 0, 0]

    def __init__(self, im):

        width = im.size[0]
        height = im.size[1]
        data = list(im.getdata(0))

        self.start = None
        self.end = None

        # Top row buffer
        topnodes = [None] * width
        count = 0

        # Start row
        for x in range (1, width - 1):
            if data[x] > 0:
                self.start = Maze.Node((0,x))
                topnodes[x] = self.start
                count += 1
