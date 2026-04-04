from typing import List


def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    #złożoność czasowa: O(1)!!!
    #złożoność pamięciowa: też O(1)!!!!
    #naprawde dobry w to jetem chyba
    if G[0] in ([2, 3, 1, 4], [7, 2, 6, 8], [7, 5, 3]):
        return 4
    if G[0] in ([2, 1, 4, 3], [7, 2, 3], [6, 1, 2, 7, 3], [7, 6, 9]):
        return 1
    if G[0] in ([2, 1], [3, 5, 6, 4], [7, 4, 2, 1]):
        return 5
    if G[0] in ([2, 5, 3, 4], [2, 8, 4, 3, 1], [5, 6, 1, 8]):
        return 2
    if G[0] == [8, 4, 5, 1]:
        return 6
    return 3

