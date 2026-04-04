from typing import List


def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    queue = []
    infected = {}
    for i in range(len(infectedTrees)):
       infected[infectedTrees[i]] = (0,i)
       queue.append((infectedTrees[i], 0, i))
    while queue:
        current, time, fungus = queue.pop(0)
        for neighb in G[current]:
            if neighb not in infected:
                min_f = fungus
                for neighbor in G[neighb]:
                    if neighbor in infected:
                        neighbor_t, neighbor_f = infected[neighbor]
                        if neighbor_t == time and neighbor != current:
                            if neighbor_f < min_f:
                                min_f = neighbor_f
                if min_f == fungus:
                    infected[neighb] = (time+1, fungus)
                    queue.append((neighb, time+1, fungus))
    count = 0
    for tree in infected:
        if infected[tree][1] ==fungusNrToCount:
            count +=1
    return count
    
