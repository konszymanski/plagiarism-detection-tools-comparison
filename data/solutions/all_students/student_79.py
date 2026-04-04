from typing import List


def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    infections = {t : i for i,t in enumerate(infectedTrees)}
    # print(infections)
    while(len(infections) != len(G)):
        newInfections = {}
        for k,v in infections.items():
            for n in G[k]:
                if n not in infections.keys() and n not in newInfections.keys():
                    newInfections[n] = v
                    
        infections.update(newInfections)
    
    # print(infections)
    treesInfectedByFungus = [f for t,f in infections.items() if f == fungusNrToCount]
    # print(treesInfectedByFungus)
    
    return len(treesInfectedByFungus)
    
