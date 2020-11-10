from graphs import *

class AdjacencyListGraph(Graph):
    def __init__(self, V, E):
        self._V = set()
        self._nbrs = {}
        for v in V:
            self.addVertex(v)
        for u, v in E:
            self.addEdge(u, v)

    def vertices(self):
        return iter(self._V)

    def edges(self):
        for u in self._V:
            for v in self.neighbors(u):
                yield (u, v)

    def addVertex(self, v):
        self._V.add(v)
        self._nbrs[v] = set()

    def addEdge(self, u, v):
        self._nbrs[u].add(v)

    def neighbors(self, v):
        return iter(self._nbrs[v])

    def removeEdge(self, u, v):
        self._nbrs[u].remove(v)

    def removeVertex(self, v):
        for neighbor in list(self.neighbors(v)):
            self.removeEdge(v, neighbor)
        self._V.remove(v)

class AdjacencyListUGraph(AdjacencyListGraph):
    def addEdge(self, u, v):
        self._nbrs[u].add(v)
        self._nbrs[v].add(u)
        
    def removeEdge(self, u, v):
        self._nbrs[u].remove(v)
        self._nbrs[v].remove(u)