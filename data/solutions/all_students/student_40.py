from typing import List

#złożoność czasowa wynosi O(m+n), gdzie m to liczba drzew, a n to liczba krawędzi
#każda krawędź oraz każde drzewo zostanie odwiedzone co najwyżej raz
def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    n1 = len(G)
    n2 = len(infectedTrees)
    inf = [-1]*n1
    queue = [[] for k in range(n2)]
    for x in range(n2):
        z = infectedTrees[x]
        inf[z] = x
        queue[x].append(z)
    while True:
        gr = False
        next = [[] for j in range(n2)]
        for d in range(n2):
            for e in queue[d]:
                for f in G[e]:
                    if inf[f] == -1:
                        inf[f] = d
                        next[d].append(f)
                        gr = True
        if not gr:
            break
        queue = next
    sum = 0
    for i in range(n1):
        if inf[i] == fungusNrToCount:
            sum += 1
    return sum

