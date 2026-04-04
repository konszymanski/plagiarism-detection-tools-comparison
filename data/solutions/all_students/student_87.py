from typing import List

# złożoność to O(n), bo przez każdy wierzchołek przechodzimy co najwyżej raz
def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    fungusnr = [-1]*len(G)
    q = []
    for i in range(len(infectedTrees)):
        q.append((i, infectedTrees[i]))
        fungusnr[infectedTrees[i]] = i
    # print(q)
    while len(q):
        for tree in G[q[0][1]]:
            if fungusnr[tree] == -1:
                q.append((q[0][0], tree))
                fungusnr[tree] = q[0][0]
        q.pop(0)
    # print(fungusnr)
    return fungusnr.count(fungusNrToCount)
    
