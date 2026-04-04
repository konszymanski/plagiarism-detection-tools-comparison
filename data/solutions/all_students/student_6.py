from typing import List
from collections import deque


def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int: #zlozonosc O(V+E + VlogV) bo dfs i sortowanie tych wstepnie zainfekowanych ktorych pesymistycznie moga byc wszystkie
    n = len(G)
    m = len(infectedTrees)
    infected = [-1] * n
    q = deque(sorted([(infectedTrees[i], i) for i in range(m)], key = lambda x: x[1]))
    
    for f, t in enumerate(infectedTrees):
        infected[t] = f
        
    while q:
        t, f = q.popleft()
        for s in G[t]:
            if infected[s] == -1:
                infected[s] = f
                q.append((s, f))
    
    return sum(1 for f in infected if f == fungusNrToCount)

