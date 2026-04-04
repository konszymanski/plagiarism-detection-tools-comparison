from typing import List
import heapq


def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    n = len(G)
    infection = [(-1,-1) for i in range(n)]
   
    heap = []
    for index , tree in enumerate(infectedTrees):
        infection[tree] = (index,0)
        heapq.heappush(heap,(0,index,tree))
    while heap:
        d, index, node = heapq.heappop(heap)
        
        for neighbor in G[node]:
            curr_index , curr_d = infection[neighbor]
            
            if curr_index == -1:
                infection[neighbor] = (index,d+1)
                heapq.heappush(heap,(d+1,index,neighbor))
                
            elif curr_d == d+1 and index < curr_index:
                infection[neighbor] = (index,d+1)
                heapq.heappush(heap,(d+1,curr_index,neighbor))
        
    return sum(1 for f, _ in infection if f == fungusNrToCount)

