from typing import List


def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    #złożoność: O(V+E), gdzie V to liczba wierzchołków a E to liczba krawędzi, ponieważ bfs odwiedza kożdy wierzchołek i krawedz tylko raz
    n = len(G)
    owner = [-1] * n
    time = [-1] * n
    
    queue = []
    
    for fungus_id, tree in enumerate(infectedTrees):
        owner[tree] = fungus_id
        time[tree] = 0
        queue.append((tree, fungus_id, 0))
        
    while len(queue) > 0:
        tree, fungus_id, t = queue.pop(0)
        
        for ngh in G[tree]:
            if owner[ngh] == -1:
                owner[ngh] = fungus_id
                time[ngh] = t+1
                queue.append((ngh, fungus_id, t+1))
            elif time[ngh] == t+1 and fungus_id < owner[ngh]:
                owner[ngh] = fungus_id
                
    count = 0
    for tree_ow in owner:
        if tree_ow == fungusNrToCount:
            count += 1
    return count
    
