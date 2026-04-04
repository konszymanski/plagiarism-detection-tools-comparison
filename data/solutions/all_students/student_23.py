from typing import List
from queue import Queue


def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int: #O(V+E), bo jest to BFS puszczony jednoczesnie z kilku miejsc
    Q = Queue()
    discovered = [-1 for _ in G]
    for i, x, in enumerate(infectedTrees):
        discovered[x]=i
        Q.put([x, i])
    while Q.qsize() > 0:
        v = Q.get()
        for neighbour in G[v[0]]:
            if discovered[neighbour]==-1:
                discovered[neighbour] = v[1]
                Q.put([neighbour, v[1]])
    return len([x for i, x in enumerate(discovered) if x==fungusNrToCount])


