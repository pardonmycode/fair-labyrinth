# A simple factory class that imports and returns a relevant solver when provided a string
# Not hugely necessary, but reduces the code in solve.py, making it easier to read.

class SolverFactory:
    def __init__(self):#for later uses
        self.Default = "breadthfirst"

