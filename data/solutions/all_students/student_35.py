from typing import List


# zlozonosc jak bfs czyli o(liczba krawedzi)

def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    infected_s = infectedTrees
    
    #G[wierzcholek] = lista sasiadow
    
    infected = [None]*len(G)
    queue = []
    for ind,infec in enumerate(infected_s):
        infected[infec] = ind
        queue.append((infec,ind))
    
    while queue:
        next = []
        for nod, grzy_id in queue:
            for sasiad in G[nod]:
                if infected[sasiad] is None:
                    infected[sasiad] = grzy_id
                    next.append((sasiad,grzy_id))
        queue = next
    counter = 0
    for i in infected:
        if i == fungusNrToCount:
            counter+=1
    return counter

