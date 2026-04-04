from typing import List
from collections import deque

# Złożoność czasowa: O(V + E), ponieważ każdy wierzchoek i krawędz jest odwiedzana tylko raz
def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    n = len(G)
    if n == 0:
        return 0
    
    infection_info = [(-1, -1)] * n
    queue = deque()
    
    for i in range(len(infectedTrees)):
        tree = infectedTrees[i]
        fungusNr = i
        infection_info[tree] = (0, fungusNr)
        queue.append((tree, 0, fungusNr))
    
    while queue:
        current_tree, current_time, current_fungus = queue.popleft()
        for neighbor in G[current_tree]:
            if infection_info[neighbor][0] == -1:  
                infection_info[neighbor] = (current_time + 1, current_fungus)
                queue.append((neighbor, current_time + 1, current_fungus))
            elif infection_info[neighbor][0] == current_time + 1:
                if current_fungus < infection_info[neighbor][1]:
                    infection_info[neighbor] = (current_time + 1, current_fungus)
    count = 0
    for time, fungusNr in infection_info:
        if fungusNr == fungusNrToCount:
            count += 1
    return count

