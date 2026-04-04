from typing import List
from collections import deque

#Złożoność: V - wierzchołki, E - krawędzie; operacje podczas rozpoczęcia i zakończenia algorytmu - O(V),
#przeszukiwanie: Każdy wierzchołek zostanie odwiedzony co najwyżej raz, a każda krawędz zostanie sprawdzona maksymalnie
#dwa razy(z dwóch stron), przy każdej iteracji po wierzchołkach operacje wewnątrz są O(1), wychodzi O(V + E)
def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    discovered = [False] * len(G) #O(V)
    queue = deque() #O(1)
    f_counters = [0] * len(infectedTrees) #O(V)
    for i in range(len(infectedTrees)):
        queue.append((infectedTrees[i], i))
        f_counters[i] += 1
        discovered[infectedTrees[i]] = True
    while queue:
        node, f_index = queue.popleft()
        for neighbour in G[node]:
            if discovered[neighbour] == False:
                discovered[neighbour] = True
                f_counters[f_index] += 1
                queue.append((neighbour, f_index))
    return f_counters[fungusNrToCount] #O(1)

