from collections import deque
from typing import List

#O(V+E), typowy bfs dla infekcji, każdy grzyb łącznie posiada taką złożoność
def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    infectedTreesQ: List[deque[int]] = []
    allInfectedTrees: List[int | None] = [None] * len(G)
    allInfectedTreesLL: List[List[int]] = []
    for i,num in enumerate(infectedTrees):
        infectedTreesQ.append(deque([num]))
        allInfectedTreesLL.append([num])
        allInfectedTrees[num] = i
    updated = True
    while updated:
        updated = False
        #Bfs dla każdego grzyba
        for i,q in enumerate(infectedTreesQ):
            curQL = len(q)
            for index in range(curQL):
                pV = q.popleft()
                for nb in G[pV]:
                    if allInfectedTrees[nb] is None:
                        allInfectedTrees[nb] = i
                        allInfectedTreesLL[i].append(nb)
                        q.append(nb)
                        updated = True
    return len(allInfectedTreesLL[fungusNrToCount])

