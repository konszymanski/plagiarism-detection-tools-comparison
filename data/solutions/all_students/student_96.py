from typing import List
from collections import deque


def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    
    n = len(G)
    queue = deque()
    
    infected_by_which_fungus_nr = [-1] * n 
    
    for fungus_nr, tree in enumerate(infectedTrees):
        queue.append((fungus_nr, tree))
        infected_by_which_fungus_nr[tree] = fungus_nr
        
    while queue:
        fungus_nr, tree = queue.popleft()
        for neighbour_tree in G[tree]:
            if infected_by_which_fungus_nr[neighbour_tree] == -1:
                infected_by_which_fungus_nr[neighbour_tree] = fungus_nr
                queue.append((fungus_nr, neighbour_tree))

    ret = 0
    for x in infected_by_which_fungus_nr:
        if x == fungusNrToCount:
            ret += 1
            
    return ret        
    pass # TODO

