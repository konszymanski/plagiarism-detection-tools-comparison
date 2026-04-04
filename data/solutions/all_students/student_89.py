from typing import List
from collections import deque
def BFS(graph: List[List[int]], infectedTrees: int, infectedByType: List[int], dist: List[int]):
    q = deque()
    discovered = set()
    
    for x in infectedTrees:
        discovered.add(x)
        q.append((x, dist[x], infectedByType[x]))
    while q:
        v, d, f = q.popleft()
        for neighbour in graph[v]:
            if dist[neighbour] == 0:
                continue
            if neighbour not in discovered:
                discovered.add(neighbour)
                if dist[neighbour] > d+1:
                    dist[neighbour] = d+1
                    infectedByType[neighbour] = f
                elif f < infectedByType[neighbour] and dist[neighbour] == d+1:
                    infectedByType[neighbour] = f
                q.append((neighbour, dist[neighbour], f))
    
def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    # Złożoność to O(V+E), ponieważ każdy wierzchołek w kolejce pojawia się raz i w najgorszym przypadku przejdziemy
    # przez wszystkie krawędzie.
    infectedByType = [float('inf') for _ in range(len(G))] 
    for i in range(len(infectedTrees)):
        infectedByType[infectedTrees[i]] = i
    dist = [float('inf') for _ in range(len(G))]
    for i in infectedTrees:
        dist[i] = 0
    
    BFS(G, infectedTrees, infectedByType, dist)
    
    return infectedByType.count(fungusNrToCount)
            
        
    

