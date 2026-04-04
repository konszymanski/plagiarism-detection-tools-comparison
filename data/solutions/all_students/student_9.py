from typing import List
from collections import deque


def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    #złożoność O(|V|+|E|)
    grzybDrzewa = dict()
    kolejkaDrzew = deque()
    counter = 0
    for i in range(len(infectedTrees)):
        grzybDrzewa[infectedTrees[i]] = i
        kolejkaDrzew.append(infectedTrees[i])
        if grzybDrzewa[infectedTrees[i]] == fungusNrToCount:
            counter = counter + 1
    while(kolejkaDrzew):
        drzewo = kolejkaDrzew.popleft()
        for element in G[drzewo]:
            if element not in grzybDrzewa:
                grzybDrzewa[element] = grzybDrzewa[drzewo]
                kolejkaDrzew.append(element)
                if grzybDrzewa[drzewo] == fungusNrToCount:
                    counter = counter + 1
    return counter
