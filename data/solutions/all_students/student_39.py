from heapq import heappop, heappush
from typing import List

#Zlozonosc O((v + e) * logv), bo przechodzimy przez kazdy wierzcholek i krawedz, a koszt operacji wynosi logv
def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    n = len(G)
    tree = [-1] * n
    queue = []
    
    for fungus, node in enumerate(infectedTrees):
        tree[node] = fungus
        heappush(queue, (0, fungus, node))
        
    while queue:
        time, fungus, node = heappop(queue)
        for neighbour in G[node]:
            if tree[neighbour] == -1:
                tree[neighbour] = fungus
                heappush(queue, (time + 1, fungus, neighbour))
    
    return sum(1 for t in tree if t == fungusNrToCount)

