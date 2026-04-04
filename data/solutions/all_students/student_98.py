from collections import deque
from typing import List

#O(V + E) mamy tu 1:1 BFS który działa trochę jak for loop
def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    n = len(G)
    owner = [-1] * n
    q = deque()
    for fungus_id, start in enumerate(infectedTrees):
        q.append((fungus_id, start))
        owner[start] = fungus_id
    while q:
        fungus_id, u = q.popleft()
        for v in G[u]:
            if owner[v] == -1:
                owner[v] = fungus_id
                q.append((fungus_id, v))
    return sum(1 for x in owner if x == fungusNrToCount)

