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
        if time > dist[u] or owner[u] != fungus_id:
            continue

        for v in G[u]:
            new_time = time + 1

            if new_time == dist[v] and fungus_id < owner[v]:
                owner[v] = fungus_id
                heapq.heappush(pq, (new_time, fungus_id, v))
            elif new_time < dist[v]:
                dist[v] = new_time
                owner[v] = fungus_id
                heapq.heappush(pq, (new_time, fungus_id, v))

    return sum(1 for x in owner if x == fungusNr)
