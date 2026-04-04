from typing import List
from collections import deque

# O(V + E) - taka sama jak BFS
def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    n = len(G)
    infection_list = [-1] * n
    
    q = deque()
    
    for fungus_idx, tree_idx in enumerate(infectedTrees):
        infection_list[tree_idx] = fungus_idx
        q.append((fungus_idx, tree_idx))
        
    while q:
        fungus_idx, tree_idx = q.popleft()
        for neighbour in G[tree_idx]:
            if infection_list[neighbour] == -1:
                infection_list[neighbour] = fungus_idx
                q.append((fungus_idx, neighbour))
                
    return sum([int(x == fungusNrToCount) for x in infection_list])
    

