from typing import List
from math import inf
from collections import deque


def dijkstra(graph, start):
    dist = {i: float('inf') for i in range(len(graph))}
    dist[start] = 0

    queue = deque([start])

    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if dist[v] == float('inf'):
                dist[v] = dist[u] + 1
                queue.append(v)

    return dist
        

#liczenie dystansow daje O(N * (V + E)), (gdze N to liczba grzybów) 
#wyznaczanie dla kazdego wierzchołka grzyba ktory
#miał do niego najkrótszą drogę O(V * N), więc ostatecznie dostajemy O(N * (V + E))
def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    
    distances = []
        
    counter = 0
    
    for element in infectedTrees:
        current = dijkstra(G, element)
        distances.append(current)
        
    for node in range(len(G)):
        min_ = inf
        fungus = -1
        for i in range(len(distances)):
            if distances[i][node] == min_ and fungus > i:
                fungus = i
                
            if distances[i][node] < min_:
                min_ = distances[i][node]
                fungus = i
        
        if fungus == fungusNrToCount:
            counter += 1
        
    return counter
    
    
