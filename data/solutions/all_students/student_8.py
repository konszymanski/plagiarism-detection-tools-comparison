from typing import List
from collections import deque

# O(V+E) działamy jak zwykły bfs tylko operujemy na kilku nodach startowych jednocześnie
def multiBfs(G: List[List[int]], fungusTable: List[int], starts: List[int]) -> List[int]:
    q = deque()
    for tree in starts:
        for v in G[tree]:
            if fungusTable[v] == -1:
                fungusTable[v] = fungusTable[tree]
                q.append(v)
    while(q):
        current = q.popleft()
        for v in G[current]:
            if fungusTable[v] == -1:
                fungusTable[v] = fungusTable[current]
                q.append(v)
    return fungusTable
# O(V+E) najbardziej złożonąoperacją jest wywołanie multiBfs
def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    fungusTable = len(G)*[-1]
    starts = []
    for i,tree in enumerate(infectedTrees):
        fungusTable[tree] = i
        starts.append(tree)
    fungusTable = multiBfs(G,fungusTable,starts)
    result = 0
    for tree in fungusTable:
        if tree == fungusNrToCount:
            result+=1
    return result
