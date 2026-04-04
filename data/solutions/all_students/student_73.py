from typing import List
import heapq


def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    n = len(G)
    infected = [-1]*n
    time = [float('inf')]*n
    
    heap = []
    for fungus_id, tree in enumerate(infectedTrees):
        heapq.heappush(heap, (0, fungus_id, tree))
        infected[tree] = fungus_id
        time[tree] = 0
    
    while heap:
        t, fungus_id, node = heapq.heappop(heap)
        for neighbor in G[node]:
            if infected[neighbor] == -1:
                infected[neighbor] = fungus_id
                time[neighbor] = t+1
                heapq.heappush(heap, (t+1, fungus_id, neighbor))
    
    return infected.count(fungusNrToCount)

