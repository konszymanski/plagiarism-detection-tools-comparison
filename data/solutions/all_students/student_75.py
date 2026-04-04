from collections import deque
from typing import List

# Złożoność czasowa: O(V + E)
# Każdy wierzchołek przetwarzany raz gdy jest infekowany, czyli O(V)
# Każda krawędź sprawdzana jest 2 razy (połączona z 2 wierzchołkami), 2E, czyli O(E)
# Złożoność pamięciowa: O(V) - tablica owner, kolejka, słownik candidate
def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    n = len(G)
    if n == 0:
        return 0
        
    owner = [-1] * n # O(V)

    
    for i, tree in enumerate(infectedTrees):
        owner[tree] = i
        
    # Kolejka do BFS
    q = deque(infectedTrees)
    
    # Pętla BFS - O(V+E)
    while q:
        candidate = {}
        # Przetwarzamy wszystkie drzewa z kolejki (wczesniej zainfekowane)
        for _ in range(len(q)): # O(V) we wszystkich krokach
            u = q.popleft()
            current_fungus = owner[u]
            
            # Przetwarzanie sąsiadów u - O(deg(u))
            for v in G[u]: # Sprawdzamy krawędzie, O(E) we wszystkich krokach
                if owner[v] != -1: # już zainfekowane
                    continue
                
                if v not in candidate:
                    candidate[v] = current_fungus
                else:
                    candidate[v] = min(candidate[v], current_fungus)
        
        # Zapisujemy i dodajemy nowo zainfekowane do q - O(V) we wszystkich krokach
        for v, fungus in candidate.items():
            owner[v] = fungus
            q.append(v)
    
    # O(V)
    count = 0
    for i in range(n):
        if owner[i] == fungusNrToCount:
            count += 1
    
    return count

