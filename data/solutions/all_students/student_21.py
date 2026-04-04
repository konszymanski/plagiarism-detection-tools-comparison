from typing import List


def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    
    n = len(G)
    
    owner = [-1] * n
    
    ques = [[] for _ in range(len(infectedTrees))]
    
    for idx, tree in enumerate(infectedTrees):
        owner[tree] = idx
        ques[idx].append(tree)
        
    while any(ques):
        new_ques = [[] for _ in range(len(ques))]
        
        for fungus_idx in range(len(ques)):
            for node in ques[fungus_idx]:
                for neighbor in G[node]:
                    if owner[neighbor] == -1:
                        owner[neighbor] = fungus_idx
                        new_ques[fungus_idx].append(neighbor)
                        
        ques = new_ques
        
    return owner.count(fungusNrToCount)
        
        
