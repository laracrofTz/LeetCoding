# Purpose of Djikstra or USe cases
# To find the shortest path from the source node to all other nodes, forming a shortest path tree
# Keeps track of current known short distances from each node to source node and is updated if the value found is smaller
# Once the shortest path is found, the node is marked as visited and added to path
# Process continues until all nodes in graph have been added to the path
# Works with graphs that only have positive weights

from collections import defaultdict
from heapq import heapify, heappop, heappush
import sys

class Vertex:
    def __init__(self, name):
        self.name = name
        self.dist = sys.maxsize

class Graph:
    def __init__(self, numVertex):
        self.numV = numVertex
        # for graph representation, use adjacency list
        self.adjList = defaultdict(list)

    def add_edge(self, source, dest, weight):
        self.adjList[source].insert(0,(dest, weight))
        self.adjList[dest].insert(0, (source, weight))

    def remove_edge(self, source, dest, weight):
        self.adjList[source].remove((dest, weight))
        self.adjList[dest].remove((source, weight))

    def djikstra(self, source, dest):
        if source == dest:
            return 0
        shortest_path = set()
        distq = []

        source.dist = 0
        shortest_path.add(source)

        for node in self.adjList.keys():
            distq.append(node)
        distq.sort(key= lambda node: node.dist)
        while len(distq) != 0:
            currNode = distq.pop(0)
            for neighbour in self.adjList[currNode]:
                neighbour[0].dist = currNode.dist + neighbour[1]
                if neighbour[0] == dest:
                    shortest_path.add(neighbour[0])
                    return shortest_path
                
            distq.sort(key= lambda node: node.dist)
