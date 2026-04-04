from typing import List


def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    #Zlozonosc obliczeniowa to: O(k * (V + E)) wykonuje k razy BFS(k-ilosc zainfekowanych drzew), a BFS przechodzi przez V-wierzcholkow + E-krawedzi
    def BFS(source):
        Q = []
        distances = {source : 0}
        discovered = set([source])
        Q.append(source)
        while Q:
            v = Q[0]
            del Q[0]
            for neighbour in G[v]:
                if neighbour not in discovered:
                    discovered.add(neighbour)
                    distances[neighbour] = distances[v] + 1
                    Q.append(neighbour)
        return distances
        
    funguses_distances = {}
    funguses_infected = {}
    
    for nr, fungus_index in enumerate(infectedTrees):
        x = BFS(fungus_index)
        if len(funguses_distances) == 0:
            funguses_distances = x
            for key in funguses_distances:
                funguses_infected[key] = nr
                
        else:
            for key in funguses_infected:
                if x[key] < funguses_distances[key]:
                    funguses_distances[key] = x[key]
                    funguses_infected[key] = nr
    
    l = 0
    for key in funguses_infected:
        if funguses_infected[key] == fungusNrToCount:
            l += 1
    
    return l

