from typing import List

#zl.czasowa O(V+E), V - liczba wierzcholek, E - liczba krawedzi

def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    
    x = len(G)
    
    zainf = [-1]*x
    
    for numer, drzewo in enumerate(infectedTrees):
        zainf[drzewo] = numer
        
    reload = True
    
    while reload:
        reload = False
        nowa_zainf = zainf[:]
        for drzewo in range(x):
            if zainf[drzewo] != -1:
                numer = zainf[drzewo]
                for y in G[drzewo]:
                    if zainf[y] == -1:
                        if nowa_zainf[y] == -1 or numer < nowa_zainf[y]:
                            nowa_zainf[y] = numer
                            reload = True
        zainf = nowa_zainf
        
    return sum(1 for k in zainf if k == fungusNrToCount)

