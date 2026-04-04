from typing import List
from collections import deque


def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    # Złożoność czasowa: O(V + E), bo algorytm sprawdza wszystkie krawędzie każdego wierzchołka
    n = len(G)
    if(n == 0):
        return 0
        
    infection_info = [(-1, -1) for _ in range(n)]
    queue = deque()
    
    for i in range(len(infectedTrees)):
        tree = infectedTrees[i]
        fungus = i
        infection_info[tree] = (fungus, 0)
        queue.append((tree, fungus, 0))
    
    while queue:
        current_tree, current_fungus, current_time = queue.popleft()
        for neighbour in G[current_tree]:
            if(infection_info[neighbour][0] == -1):
                infection_info[neighbour] = (current_fungus, current_time+1)
                queue.append((neighbour, current_fungus, current_time+1))
            elif infection_info[neighbour][1] == current_time + 1:
                if current_fungus < infection_info[neighbour][0]:
                    infection_info[neighbour] = (currnent_fungus, current_time+1)
    
    count = 0
    for fungus, time in infection_info:
        if fungus == fungusNrToCount:
            count += 1
    
    return count
    
    
