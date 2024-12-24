# Adjacency matrix and lists

# ADJACENCY MATRIX
class Graph:
    def __init__(self, size):
        self.size = size
        self.adjMat = []
        for i in range(size):
            self.adjMat.append([0 for i in range(size)])

    def add_edge(self, v1, v2):
        if v1==v2: return "Both are same vertices!"
        self.adjMat[v1][v2] = 1
        self.adjMat[v2][v1] = 1

    def remove_edge(self, v1, v2):
        if v1==v2: return "Both are same vertices!"
        self.adjMat[v1][v2] = 0
        self.adjMat[v2][v1] = 0

    def __len__(self):
        return self.size
    
    # Pros:
    # Time complexity of adding and removing edges are constant time
    # Matrix should be used for dense graphs with many edges 
    # COns:
    # Space required is alot, since this is a 2 dimensional matrix -> V^2
    
# ADJACENCY LIST
# Uses dictionary where eachvertex is the key and the values are the corresponding vertices its connected to

from collections import defaultdict 
class Graph2:
    def __init__(self, numNodes):
        self.numNodes = numNodes
        self.adjList = defaultdict(list) # default dict creates an empty list as default value
    
    def addEdge(self, v1, v2):
        self.adjList[v1].append(v2) #uni directional
        # if bi directional
        # self.adjList[v2].append(v1)

    def remove_edge(self, v1, v2): # O(V) time complexity since we have to find he vertex first before 
        self.adjList[v1].remove(v2)
        # if bi directional
        # self.adjList[v2].remove(v1)

    # Space complexity is O(V+E) since we are storing vertex and its associated edges
    # 