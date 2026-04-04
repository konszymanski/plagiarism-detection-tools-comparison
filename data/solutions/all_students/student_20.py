from typing import List
from collections import deque

def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    n = len(G)
    owner = [-1] * n
    time = [-1] * n
    queue = deque()

    for fungus_id, tree in enumerate(infectedTrees):
        owner[tree] = fungus_id
        time[tree] = 0
        queue.append((tree, fungus_id, 0))

    while queue:
        node, fungus_id, t = queue.popleft()

        for neighbor in G[node]:
            
            
            if owner[neighbor] == -1:
                
                owner[neighbor] = fungus_id
                time[neighbor] = t +1
                queue.append((neighbor, fungus_id, t + 1))
                
                
            elif time[neighbor] == t + 1 and fungus_id < owner[neighbor]:
                owner[neighbor] = fungus_id
                
                
                queue.append((neighbor, fungus_id, t + 1))
        result = sum(1 for o in owner if o == fungusNrToCount)
    return result

