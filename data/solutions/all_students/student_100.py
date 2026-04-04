from typing import List
from collections import deque


def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    '''
    Funkcja ta ma złożoność O(|V|), gdyż każdy wierzchołek grafu musi zostać zainfekowany.
    '''
    cellStates = [-1]*len(G)
    counter = 1
    Q = deque(((fungus, tree) for fungus, tree in enumerate(infectedTrees)))
    for fungus, tree in enumerate(infectedTrees):
        cellStates[tree] = fungus
    while Q:
        fungus, tree = Q.popleft()
        for neigh in G[tree]:
            if cellStates[neigh] == -1:
                cellStates[neigh] = fungus
                if fungusNrToCount == fungus:
                    counter += 1
                Q.append((fungus, neigh))
    return counter

