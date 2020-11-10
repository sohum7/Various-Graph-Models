from itertools import chain

class Graph:
    def addVertex(self, vert):
        #Add a vertex with key k to the vertex set.
        raise NotImplemented

    def addEdge(self, fromVert, toVert):
        #Add a directed edge from u to v.
        raise NotImplemented

    def neighbors(self):
        #Return an iterable collection of the keys of all
        #vertices adjacent to the vertex with key v.
        raise NotImplemented

    def removeEdge(self, u, v):
        #Remove the edge from vertex u to v from graph.
        raise NotImplemented

    def removeVertex(self, v):
        #Remove the vertex v from the graph as well as any edges
        #incident to v.
        raise NotImplemented

            
    def dfs(self, v):
        possiblePaths = {}
        queue = [ (None, v) ]
        while queue:
            x, y = queue.pop()
            if y not in possiblePaths:
                possiblePaths[y] = x
                for neighbor in self.neighbors(y):
                    queue.append((y, neighbor))
        return possiblePaths
    
    def findPath(self, u, v):
        path = self.dfs(u)
        if v not in path or v == u:
            return None
        else:
            lst = [v]
            while True:
                if lst[0] == u:
                    return lst
                else:
                    lst.insert(0, path[lst[0]])
    
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
