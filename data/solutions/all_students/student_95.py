from typing import List

def infect(G: List[List[int]], infectedTrees: List[int], source: int, infectedToCount: set[int], doCount: bool = False) -> None:
    infectedTreesSet = set(infectedTrees)
    for neighbor in G[source]:
        if neighbor not in infectedTreesSet:
            if doCount:
                infectedToCount.add(neighbor)
            infectedTrees.append(neighbor)
        

def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    infectedToCount = set()
    infectedToCount.add(infectedTrees[fungusNrToCount])
    
    
    while len(infectedTrees) < len(G):
        for tree in infectedTrees:
            if (tree in infectedToCount):
                infect(G, infectedTrees, tree, infectedToCount, True)
            else:
                infect(G, infectedTrees, tree, infectedToCount)
    return len(infectedToCount)

