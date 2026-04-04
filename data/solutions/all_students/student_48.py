from typing import List

#czasowa złożoność obliczeniowa wynosi O(n+m), gdzie n to liczba wierzchołków, a m liczba krawędzi
#każdy wierzchołek odwiedzany maksymalnie raz (while), każda krawędź sprawdzana raz (for)

def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    n=len(G)
    z=[-1]*n
    qs=[]
    for j in range(len(infectedTrees)):
        for i in range(n):
            if i==infectedTrees[j]:
                qs.append(i)
                z[i]=j
        
    p=0
    while p<len(qs):
        u=qs[p]
        p+=1
        for i in range(len(G[u])):
            v=G[u][i]
            if z[v]==-1:
                z[v]=z[u]
                qs.append(v)
    res=0
    for p in range(len(z)):
        if z[p]==fungusNrToCount:
            res+=1
    return res
        
