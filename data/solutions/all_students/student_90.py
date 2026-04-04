from typing import List

# Złożoność czasowa to O(|v| + |e|), gdzie v to liczba wierzcholkow w grafie, a e to liczba krawedzi w grafie, poniewaz
# uzywamy tu bfs.

def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    n = len(G)
    infected_by = [-1]*n
    infection_time = [-1]*n
    count = 0
    
    current = []
    for fung_id, tree in enumerate(infectedTrees):
        infected_by[tree] = fung_id
        infection_time[tree] = 0
        current.append((tree, fung_id, 0))
    
    while current:
        after_first = []
        
        for node, fung, i in current:
            for neighbor in G[node]:
                if infected_by[neighbor] == -1:
                    infected_by[neighbor] = fung
                    infection_time[neighbor] = i + 1
                    after_first.append((neighbor, fung, i + 1))
                elif infection_time[neighbor] == i + 1 and fung < infected_by[neighbor]:
                    infected_by[neighbor] = fung
                    after_first.append((neighbor, fung, i + 1))
                    
        current = after_first
    
    
    for node in infected_by:
        if node == fungusNrToCount:
            count += 1
    
    return count 
        

