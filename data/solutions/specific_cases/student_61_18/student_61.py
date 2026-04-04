from typing import List
from collections import deque

#O(V + E), gdzie V to liczba drzew (wierzchołków grafu), a E to liczba krawędzi.
def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    n = len(G)
    infected = [None] * n
    q = deque()
    for i, tree in enumerate(infectedTrees):
        infected[tree] = i
        q.append((tree,i))
        
    while q:
        tree, fungus = q.popleft()
        for x in G[tree]:
            if infected[x] is None:
                infected[x] = fungus
                q.append((x,fungus))

    return infected.count(fungusNrToCount)

