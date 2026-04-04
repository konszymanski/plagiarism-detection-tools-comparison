from typing import List

# Złożoność O(n(V+E)), gdzie n to liczba grzybów, ponieważ jedna iteracja algorytmu BFS wykonuje się n razy
def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    Q = []
    discovered = [-1]*len(G)
    
    for i in range(len(infectedTrees)):
        Q.append([infectedTrees[i]])
        discovered[infectedTrees[i]] = i
    
    while(any(Q)):
        for i in range(len(infectedTrees)):
            if Q[i]:
                v = Q[i].pop(0)
                for neighbour in G[v]:
                    if discovered[neighbour] == -1:
                        discovered[neighbour] = i
                        Q[i].append(neighbour)
    
    return discovered.count(fungusNrToCount)

