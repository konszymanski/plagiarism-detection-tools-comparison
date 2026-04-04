from typing import List
from collections import deque


def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:

    #zlozonosc czasowa O(n + m), gdzie n to liczba drzew, a m to liczba krawędzi
    #zlozonosc pamieciowa O(n)

    n = len(G)
    infected_by = [-1] * n
    time_infected = [-1] * n
    q = deque()

    for i in range(len(infectedTrees)):
        tree = infectedTrees[i]
        infected_by[tree] = i
        time_infected[tree] = 0
        q.append((tree, i, 0))

    while q:
        tree, fungus, time = q.popleft()
        for neighbor in G[tree]:
            if infected_by[neighbor] == -1:
                infected_by[neighbor] = fungus
                time_infected[neighbor] = time + 1
                q.append((neighbor, fungus, time + 1))
            elif time_infected[neighbor] == time + 1 and fungus < infected_by[neighbor]:
                infected_by[neighbor] = fungus

    count = 0
    for i in range(n):
        if infected_by[i] == fungusNrToCount:
            count += 1

    return count


