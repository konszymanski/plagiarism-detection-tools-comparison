from typing import List
from collections import deque
import heapq


def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    n = len(G)
    owner = [-1] * n  
    visited_time = [-1] * n  
    heap=[]
    
    for fungusIndex, tree in enumerate(infectedTrees):
        heapq.heappush(heap,(0, fungusIndex, tree)) 
        owner[tree] = fungusIndex
        visited_time[tree] = 0
    while heap:  
        time,mushroom,tree=heapq.heappop(heap)
        for neighbor in G[tree]:
            if owner[neighbor]==-1:
                owner[neighbor]=mushroom
                visited_time[neighbor]=time+1
                heapq.heappush(heap,(time+1,mushroom,neighbor))
            elif visited_time[neighbor]==time+1 and owner[neighbor]>mushroom:
                owner[neighbor]=mushroom
                visited_time[neighbor] = time + 1 
                heapq.heappush(heap,(time+1,mushroom,neighbor))
    count = 0
    for tree_index in range(n):
        if owner[tree_index] == fungusNrToCount:
            count += 1
    return count
                
                    
                    

