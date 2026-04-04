from typing import List
from collections import deque

def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    n = len(G)
    owner = [-1] * n  
    q = deque()

    for fungus_id, tree in enumerate(infectedTrees):
        owner[tree] = fungus_id
        q.append((tree, fungus_id, 0)) 

    while q:
        node, fungus_id, time = q.popleft()
        for neighbor in G[node]:
            if owner[neighbor] == -1:
                owner[neighbor] = fungus_id
                q.append((neighbor, fungus_id, time + 1))

    return owner.count(fungusNrToCount)

