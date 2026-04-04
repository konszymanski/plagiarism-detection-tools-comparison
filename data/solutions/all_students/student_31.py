from typing import List
from collections import deque


def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    infected_by = [-1] * len(G)
    q = deque()
    for i, t in enumerate(infectedTrees):
        infected_by[t] = i
        q.append((t, i))
    while q:
        u, f = q.popleft()
        for v in G[u]:
            if infected_by[v] == -1:
                infected_by[v] = f
                q.append((v, f))
    c = 0
    for x in infected_by:
        if x == fungusNrToCount:
            c += 1
    return c


