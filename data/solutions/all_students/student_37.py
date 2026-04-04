from typing import List


def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    n = len(G)
    infected_by = [-1] * n
    queues = [[tree] for tree in infectedTrees]

    for i, tree in enumerate(infectedTrees):
        infected_by[tree] = i

    while any(queues[i] for i in range(len(queues))):
        next_level = [[] for _ in range(len(queues))]
        for i, queue in enumerate(queues):
            for node in queue:
                for neighbor in G[node]:
                    if infected_by[neighbor] == -1:
                        infected_by[neighbor] = i
                        next_level[i].append(neighbor)
        queues = next_level

    return infected_by.count(fungusNrToCount)

