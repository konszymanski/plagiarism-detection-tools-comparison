from typing import List
from collections import deque


def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    n = len(G)
    visited = [-1] * n
    q = deque()
    for fungus_id, tree in enumerate(infectedTrees):
        visited[tree] = fungus_id
        q.append((tree, fungus_id))
    while q:
        node, fungus_id = q.popleft()
        for nei in G[node]:
            if visited[nei] == -1:
                visited[nei] = fungus_id
                q.append((nei, fungus_id))
    return visited.count(fungusNrToCount)

