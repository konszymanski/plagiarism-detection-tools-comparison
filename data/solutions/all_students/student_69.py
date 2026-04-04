from typing import List


def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    #Rozwiązanie ma czasową złożoność obliczeniową O(V+E)
    #gdzie V to liczba wierzchołków, a E to liczba krawędzi w grafie G
    #ponieważ algorytm przechodzi przez wszystkie wierzchołki i krawędzie w grafie
    #pętla while wykounje się V razy
    #a pętla for, w trakcie wszystkich iteracji zewnętrznej pętli, łącznie wykona się E razy
    queue=[]
    infected={infectedTrees[i]:i for i in range(len(infectedTrees))}
    queue+=infectedTrees
    count=0
    while queue:
        v=queue.pop(0)
        if infected[v]==fungusNrToCount:
            count+=1
        for neighbour in G[v]:
            if neighbour not in infected:
                infected[neighbour]=infected[v]
                queue.append(neighbour)
    return count
    

