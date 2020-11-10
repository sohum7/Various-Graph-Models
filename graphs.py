from itertools import chain

class Graph:
    def addVertex(self, vert):
        raise NotImplemented

    def addEdge(self, fromVert, toVert):
        raise NotImplemented

    def neighbors(self, y):
        raise NotImplemented

    def removeEdge(self, u, v):
        raise NotImplemented

    def removeVertex(self, v):
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
                    
