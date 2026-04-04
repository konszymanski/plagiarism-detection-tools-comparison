import heapq
from typing import List

def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNr: int) -> int:
    '''
    Time complexity: O((V + E) log V)

    Justification:
    - Each vertex (V) can be inserted into the priority queue at most once,
      because once a tree is infected, its owner does not change.
    - Each edge (E) is processed at most once.
    - Priority queue operations take O(log V) time
    '''

    n = len(G)

    # owner[i] = fungus number that ultimately infects tree i
    owner = [-1] * n

    # dist[i] = time when the first fungus reaches tree i
    dist = [float('inf')] * n

    # priority queue elements: (time, fungus_number, tree)
    pq = []

    # initialization – each infected tree starts at time 0
    for fungus_id, tree in enumerate(infectedTrees):
        dist[tree] = 0
        owner[tree] = fungus_id
        heapq.heappush(pq, (0, fungus_id, tree))

    while pq:
        time, fungus_id, u = heapq.heappop(pq)

        # skip outdated states
        if time > dist[u] or owner[u] != fungus_id:
            continue

        for v in G[u]:
            new_time = time + 1

            # tree not infected yet or reached faster
            if new_time < dist[v]:
                dist[v] = new_time
                owner[v] = fungus_id
                heapq.heappush(pq, (new_time, fungus_id, v))

            # same arrival time, but fungus with smaller index wins
            elif new_time == dist[v] and fungus_id < owner[v]:
                owner[v] = fungus_id
                heapq.heappush(pq, (new_time, fungus_id, v))

    # count trees infected by the given fungus
    return sum(1 for x in owner if x == fungusNr)
