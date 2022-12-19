class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        # graph without edges
        if (edges == []):
            return True

        # pre proc: edges list -> adjacence list
        adjList = {}
        for i, edge in enumerate(edges):
            v1, v2 = edge[0], edge[1]
            if (v1 not in adjList.keys()):
                adjList[v1] = []
                adjList[v1].append(v2)
            else:
                if (v2 not in adjList[v1]):
                    adjList[v1].append(v2)
            if (v2 not in adjList.keys()):
                adjList[v2] = []
                adjList[v2].append(v1)
            else:
                if (v1 not in adjList[v2]):
                    adjList[v2].append(v1)
        
        # algo: DFS or BFS
        vert = []
        visit = []
        result = False
        for i, v in enumerate(adjList[source]):
            if (v not in visit):
                vert.append(v)
            if (v == destination):
                result = True
        visit.append(source)
        while (vert != []):
            if (result == True):
                break
            curr = vert.pop()
            for i, v in enumerate(adjList[curr]):
                if (v not in visit):
                    vert.append(v)
                if (v == destination):
                    result = True
            visit.append(curr)
        
        return result
