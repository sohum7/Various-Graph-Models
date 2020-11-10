from graphs import *

class SimpleGraph(Graph):
    def __init__(self, V, E):
        self._V = set()
        self._E = set()
        for v in V: self.addVertex(v)
        for u,v in E: self.addEdge(u,v)

    def vertices(self):
        return iter(self._V)

    def edges(self):
        return iter(self._E)

    def addVertex(self, v):
        self._V.add(v)

    def addEdge(self, u, v):
        self._E.add((u, v))

    def neighbors(self, v):
        return (w for u, w in self._E if u == v)

    def removeEdge(self, u, v):
        self._E.remove((u, v))

    def removeVertex(self, v):
        for neighbor in list(self.neighbors(v)):
            self.removeEdge(v, neighbor)
        self._V.remove(v)

class SimpleUGraph(SimpleGraph):
    
    def addEdge(self, u, v):
        self._E.add((v,u))
        SimpleGraph.addEdge(self, u,v)
        
    def removeEdge(self, u, v):
        self._E.remove((v,u))
        SimpleGraph.removeEdge(self, u,v)