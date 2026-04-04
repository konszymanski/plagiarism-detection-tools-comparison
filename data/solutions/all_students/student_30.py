from typing import List
#Złożoność O(V+E) - najbardziej czasochłonne jest wywołanie BFS-a
def bfs(graph,infected,vis):
    q = []
    for i in range(len(infected)):
        q.append([infected[i],i])
    while(len(q)):
        tmp = q.pop(0)
        v = tmp[0]
        g = tmp[1]
        if vis[v]==-1:
            vis[v] = g
            for u in graph[v]:
                q.append([u,g])
    return vis
def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    visited = [-1]*len(G)
    visited = bfs(G,infectedTrees,visited)
    res = 0
    for v in visited:
        if v==fungusNrToCount:
            res+=1
    return res

