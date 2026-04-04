from typing import List
from collections import deque, defaultdict
import heapq


def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    n = len(G)
    infected_by = [-1] * n
    infected_at_time = [float('inf')] * n 
    
    pq = []
    for fungus_id, tree in enumerate(infectedTrees):
        if infected_at_time[tree] == float('inf') or (infected_at_time[tree] == 0 and fungus_id < infected_by[tree]):
            infected_by[tree] = fungus_id
            infected_at_time[tree] = 0
            heapq.heappush(pq, (0, fungus_id, tree))

    while pq:
        time, fungus_id, current_tree = heapq.heappop(pq)
        if infected_at_time[current_tree] < time:
            continue
        if infected_at_time[current_tree] == time and infected_by[current_tree] < fungus_id:
            continue
        
        for neighbor in G[current_tree]:
            next_time = time + 1

            # Case 1: Neighbor is uninfected
            if infected_by[neighbor] == -1:
                infected_by[neighbor] = fungus_id
                infected_at_time[neighbor] = next_time
                heapq.heappush(pq, (next_time, fungus_id, neighbor))
            # Case 2: Neighbor is infected at a later time (new, faster path)
            elif next_time < infected_at_time[neighbor]:
                infected_by[neighbor] = fungus_id
                infected_at_time[neighbor] = next_time
                heapq.heappush(pq, (next_time, fungus_id, neighbor))
            # Case 3: Neighbor is infected at the same time (tie-breaking)
            elif next_time == infected_at_time[neighbor]:
                if fungus_id < infected_by[neighbor]: # Current fungus has a lower ID
                    infected_by[neighbor] = fungus_id
                    heapq.heappush(pq, (next_time, fungus_id, neighbor))


    return sum(1 for f in infected_by if f == fungusNrToCount)


