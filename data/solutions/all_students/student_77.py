from typing import List

def full(infected, n):
    A = set()
    for i in infected:
        A.update(i)
    return len(A) == n
#O(k*m)
def Index(infected, sasiad):
    for i in range(len(infected)):
        if(sasiad in infected[i]):
            return i
    return -1
#O(n*m*k)
def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    infected=list()
    nowe=[]
    
    for i in range(len(infectedTrees)):
        lista = [infectedTrees[i]]
        infected.append(lista)
        nowe.append(lista)
    n=len(G)
    
    nowe = [(i, infectedTrees[i]) for i in range(len(infectedTrees))]

    while not full(infected, n):
        pom = []
        for grzyb_nr, drzewo in nowe:
            for sasiad in G[drzewo]:
                if Index(infected, sasiad) == -1:
                    infected[grzyb_nr].append(sasiad)
                    pom.append((grzyb_nr, sasiad))
        nowe = pom
                    
    return len(infected[fungusNrToCount])

