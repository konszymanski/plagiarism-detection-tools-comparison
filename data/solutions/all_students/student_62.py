from typing import List


def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    # O(N + E), gdzie N to liczba drzew, E to liczba połączeń (krawędzi w grafie)
    n = len(G)
    infected_by = [-1] * n
    queue = []

    for fungus_id, tree in enumerate(infectedTrees):
        infected_by[tree] = fungus_id
        queue.append((tree, fungus_id, 0))

    visited_at_time = [None] * n
    i = 0

    while i < len(queue):
        node, fungus_id, time = queue[i]
        i += 1

        for neighbor in G[node]:
            if infected_by[neighbor] == -1:
                if visited_at_time[neighbor] is None:
                    visited_at_time[neighbor] = time + 1
                    infected_by[neighbor] = fungus_id
                    queue.append((neighbor, fungus_id, time + 1))
                elif visited_at_time[neighbor] == time + 1:
                    if fungus_id < infected_by[neighbor]:
                        infected_by[neighbor] = fungus_id
                        queue.append((neighbor, fungus_id, time + 1))

    count = 0
    for g in infected_by:
        if g == fungusNrToCount:
            count += 1
    return count

