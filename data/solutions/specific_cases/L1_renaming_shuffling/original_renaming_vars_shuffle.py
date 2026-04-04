import heapq
from typing import List

# Time complexity: O((V + E) log V)
def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNr: int) -> int:
    queue = []

    x = len(G)
    b = [float('inf')] * x
    a = [-1] * x

    for i, item in enumerate(infectedTrees):
        a[item] = i
        b[item] = 0
        heapq.heappush(queue, (0, i, item))

    while queue:
        t, i, v = heapq.heappop(queue)
        if t > b[v] or a[v] != i:
            continue

        for node in G[v]:
            t_1 = t + 1

            if t_1 < b[node]:
                a[node] = i
                b[node] = t_1
                heapq.heappush(queue, (t_1, i, node))

            elif t_1 == b[node] and i < a[node]:
                a[node] = i
                heapq.heappush(queue, (t_1, i, node))

    return sum(1 for x in a if x == fungusNr)
