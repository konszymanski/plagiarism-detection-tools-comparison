from typing import List


def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    n = len(G)
    a = [-1] * n
    b = [-1] * n
    
    q = []
    
    for i, j in enumerate(infectedTrees):
        a[j] = i
        q.append((0,i,j))
    
    q.sort()
    
    n1 = 0
    
    while q:
        t, index, tree = q.pop(0)
        
        for j in G[tree]:
            if a[j] == -1:
                a[j] = index
                b[j] = t + 1
                q.append((t+1, index, j))
            elif b[j] == t + 1 and index < a[j]:
                a[j] = index
                
    return a.count(fungusNrToCount)
    pass # TODO

