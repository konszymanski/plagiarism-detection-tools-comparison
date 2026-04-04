from typing import List

from collections import deque

def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    counter = 1
    q = deque()
    visited = set()
    for fungus_type, tree in enumerate(infectedTrees):
        visited.add(tree)
        q.append((tree, fungus_type))
    
    
    while q:
        v, fungus_type = q.popleft()
        for neighbour in G[v]:
            if neighbour not in visited:
                visited.add(neighbour)
                q.append((neighbour, fungus_type))
                
                if fungus_type == fungusNrToCount:
                    counter += 1   
    
            
    return counter

