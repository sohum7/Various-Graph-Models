from graphs import *

class AdjacencyMatrixGraph(Graph):
    def __init__(self, V, E):
        self._V = []
        self._matrix = []
        for v in V:
            self.addVertex(v)
        for u, v in E:
            self.addEdge(u, v)
            
    def vertices(self):
        return iter(self._V)

    def edges(self):
        row = 0
        while row < len(self._V):
            col = 0
            while col < len(self._V):
                if self._matrix[row][col] == 1:
                    yield (self._V[row], self._V[col])
                col += 1
            row += 1
        
    def addVertex(self, v):
        i = 0
        self._matrix.append([0] * len(self._V))
        self._V.append(v)
        while i < len(self._V):
            self._matrix[i].append(0)
            i += 1

    def removeVertex(self, v):
        temp = self._V.index(v)
        i = 0
        while i < len(self._V):
            del self._matrix[i][temp]
            i += 1
        del self._matrix[temp]
        del self._V[temp]

    def neighbors(self, u):
        i = 0
        while i < len(self._V):
            if self._matrix[self._V.index(u)][i] == 1:
                yield self._V[i]
            i += 1
    
    def addEdge(self, u, v):
        self._matrix[self._V.index(u)][self._V.index(v)] = 1

    def removeEdge(self, u, v):
        self._matrix[self._V.index(u)][self._V.index(v)] = 0
    
    def drawMatrix(self):
        for row in self._matrix:
            print(row)

class AdjacencyMatrixUGraph(AdjacencyMatrixGraph):
    def addEdge(self, u, v):
        AdjacencyMatrixGraph.addEdge(self, u, v)
        self._matrix[self._V.index(v)][self._V.index(u)] = 1
        
    def removeEdge(self, u, v):
        AdjacencyMatrixGraph.removeEdge(self, u, v)
        self._matrix[self._V.index(v)][self._V.index(u)] = 0
