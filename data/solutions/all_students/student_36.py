from typing import List
from collections import deque
#zlozonosc O(N+M+k) każde drzewo odwiedzamy raz i  każdą krawędź najwyżej raz
def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int: 
    n = len(G)
    not_infected = [-1 for x in range(n)]
    k = len(infectedTrees)
    
    queues = [deque() for _ in range(k)]
    for fungus_id, tree in enumerate(infectedTrees):
        not_infected[tree] = fungus_id
        queues[fungus_id].append(tree)
        
    while any(queues):
        for fungus_id in range(k):
            next_level = deque()
            while queues[fungus_id]:
                tree = queues[fungus_id].popleft()
                for neigh in G[tree]:
                    if not_infected[neigh]==-1:
                        not_infected[neigh] = fungus_id
                        next_level.append(neigh) 
            queues[fungus_id] = next_level
                
    return not_infected.count(fungusNrToCount)         
                
                
                
                
