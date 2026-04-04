from typing import List


def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:

    n = len(G)
    owner = [-1] * n
    time = [float('inf')] * n
    k = len(infectedTrees)
    queue = []
    for fungus_id, tree in enumerate(infectedTrees):
        owner[tree] = fungus_id
        time[tree] = 0
        queue.append((0, fungus_id, tree))

    i = 0
    while i < len(queue):
        t, fungus_id, u = queue[i]
        i += 1
        for v in G[u]:
            if time[v] > t + 1:
                time[v] = t + 1
                owner[v] = fungus_id
                queue.append((t + 1, fungus_id, v))
            elif time[v] == t + 1 and fungus_id < owner[v]:
                owner[v] = fungus_id
                queue.append((t + 1, fungus_id, v))

    return sum(1 for o in owner if o == fungusNrToCount)

