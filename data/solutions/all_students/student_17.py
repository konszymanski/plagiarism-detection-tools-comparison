from typing import List
from collections import deque


def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
#złożoność: O(V+E) - przez każde drzewo przechodzimy raz i odwiedzamy wszystkich jego sąsiadów
    n = len(G)
    discovered = {}
    Q = deque()
    
    for i in range(len(infectedTrees)):
        tree = infectedTrees[i]
        discovered[tree] = (0,i) #czas = 0, nr_grzyba = i
        Q.append((tree,0,i))
        
    
    while Q:
        tree, time, fungus = Q.popleft()
        for neighbor in G[tree]:
            if neighbor in discovered:
                old_time, old_fungus = discovered[neighbor]
                if old_time == time+1 and fungus < old_fungus: #jak w tym samym czasie to jak ma mniejszy indeks to wygrywa
                    discovered[neighbor] = (time+1,fungus)
                    Q.append((neighbor,time+1,fungus))
            else:
                discovered[neighbor] = (time+1, fungus)
                Q.append((neighbor,time+1,fungus))
                
    count = 0
    for time,fungus in discovered.values():
        if fungus == fungusNrToCount:
            count += 1
    return count
        

