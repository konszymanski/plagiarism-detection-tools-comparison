import heapq
from typing import List

# Time complexity: O((V + E) log V)
def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNr: int) -> int:
    n = len(G)
    owner = [-1] * n
    dist = [float('inf')] * n

    pq = []

    for fungus_id, tree in enumerate(infectedTrees):
        dist[tree] = 0
        owner[tree] = fungus_id
        heapq.heappush(pq, (0, fungus_id, tree))

    while pq:
        time, fungus_id, u = heapq.heappop(pq)
        if  dist[u] > time or fungus_id != owner[u]:
            continue

        for v in G[u]:
            new_time = time + 1

            if  dist[v] > new_time:
                dist[v] = new_time
                owner[v] = fungus_id
                heapq.heappush(pq, (new_time, fungus_id, v))

            elif dist[v] == new_time and owner[v] > fungus_id:
                owner[v] = fungus_id
                heapq.heappush(pq, (new_time, fungus_id, v))

    return sum(1 for x in owner if x == fungusNr)
