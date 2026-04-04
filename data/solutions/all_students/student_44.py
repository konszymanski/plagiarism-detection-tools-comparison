from typing import List
from collections import deque

def grid_bfs(graph, fungi):
    q = deque()
    parent = {}
    visited = set()
    
    for fungus, start in enumerate(fungi):
        q.append((fungus, start))
        visited.add(start)
        
    while q:
        fungus, v = q.popleft()
        
        for neighbour in graph[v]:
            if neighbour not in visited:
                visited.add(neighbour)
                parent[neighbour] = fungus
                q.append((fungus, neighbour))
    return parent

def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    #czasowa O(m*n + E), gdzie m*n = V - liczba wezłów, E - liczba krawędzi
    #pamięciowa O(m*n) - kolejka, słownik z rodzicami oraz visited są maksymalnie rozmiarów m*n
    parents = grid_bfs(G, infectedTrees)
    count = sum(1 for node, parent in parents.items() if parent == fungusNrToCount) + 1
    return count

