from typing import List

#czasowa złożoność obliczeniowa: O(nlogn), ponieważ pętla while wykona się logn, a funkcja w niej - n (n - ilość krawędzi)
def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    infected = []
    for i in range(len(G)):
        infected.append(None)
    for i in infectedTrees:
        infected[i] = infectedTrees.index(i)
    
    def spreadingFungus(infected):
        newInfected = infected.copy()
        for i in range(len(infected)):
            if infected[i] == None:
                newFungus = None
                for k in G[i]:
                    if infected[k] != None and (newFungus == None or infected[k] < newFungus):
                        newFungus = infected[k]
                newInfected[i] = newFungus
        return newInfected
    
    while None in infected:
        infected = spreadingFungus(infected)
    counter = 0
    for i in infected:
        if i == fungusNrToCount:
            counter += 1
    return counter

