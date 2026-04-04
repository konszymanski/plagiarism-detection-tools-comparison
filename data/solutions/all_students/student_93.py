from typing import List


# program ma złożoność czasową O(V*V*(V+E))
def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    
    V = len(G)
    
    k = len(infectedTrees)
    treesDisease = [k for x in range(V)]
    for fungusNr in range(k):
        treesDisease[infectedTrees[fungusNr]] = fungusNr
    # print(treesDisease)
    count = 1
    while len(infectedTrees) != V:
        treesToInfect = []
        for v, neighbours in enumerate(G):
            if v in infectedTrees:
                continue
            min_disease = k
            for neighbour in neighbours:
                if treesDisease[neighbour] < min_disease:
                    min_disease = treesDisease[neighbour]
            
            if min_disease != k:
                treesToInfect.append((v, min_disease))
                if min_disease == fungusNrToCount:
                    count += 1
                    
        for v, min_disease in treesToInfect:
            infectedTrees.append(v)
            treesDisease[v] = min_disease
            
    return count
    
    

