from typing import List

def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    n = len(G)
    owned = [-1] * n

    q = []
    for i in range(len(infectedTrees)):
        idx = infectedTrees[i]
        owned[idx] = i
        q.append((idx, i))

    while len(q) > 0:
        current = q[0]
        q = q[1:]

        node = current[0]
        fungus = current[1]

        for nei in G[node]:
            if owned[nei] == -1:
                 owned[nei] = fungus
                q.append((nei, fungus))
            elif owned[nei] > fungus:
                owned[nei] = fungus
                q.append((nei, fungus))

    count = 0
    for i in range(n):
        if owned[nei] == fungusNrToCount:
            count += 1

    return count