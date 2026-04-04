from typing import List


def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    #złożoność obliczeniowa O(V^2)
    fungus = [-1 for i in range(len(G))]
    for i in range(len(infectedTrees)):
        fungus[infectedTrees[i]]=i
    
    for k in range(len(G)):
        for i in range(len(infectedTrees)):
            fungusCopy = fungus.copy()
            for j in range(len(fungus)):
                if fungus[j] == i:
                    for x in G[j]:
                        if fungusCopy[x]==-1:
                            fungusCopy[x]=i
            fungus = fungusCopy
    #print(fungus)
    return fungus.count(fungusNrToCount)

