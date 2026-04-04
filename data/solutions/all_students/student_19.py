from typing import List

def bfs(graf, source, grzyb, nr):
    q=[]
    discovered=set()
    distance = [0] * len(graf)
    discovered.add(source)
    distance[source]=0
    q.append(source)
    grzyb[source]=(0,nr)
    while q:
        v=q.pop(0)
        for neighbour in graf[v]:
            if neighbour not in discovered:
                distance[neighbour]=distance[v]+1
                dis,cur_nr=grzyb[neighbour]
                if distance[neighbour] < dis:
                    grzyb[neighbour]=(distance[neighbour],nr)
                if dis==distance[neighbour]:
                    if nr<cur_nr:
                        grzyb[neighbour]=(distance[neighbour],nr)
                q.append(neighbour)
                discovered.add(neighbour)
    
                


def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    #złożoność tej funkcji wynosi O(k*(V+E)) gdzie V to ilość wierzchołków, E ilość krawędzi a k to ilość rodzajów grzybów, ponieważ dla każdego grzyba wykonuje się oddzielnie bfs,
    #a standardowa złożoność bfs wynosi O(V+E)
    grzyb=[(100,100) for _ in range(len(G))]
    for i in range(len(infectedTrees)):
        bfs(G,infectedTrees[i],grzyb,i)
    #print(grzyb)
    counter=0
    for i in grzyb:
        if(i[1]==fungusNrToCount):
            counter+=1
    return counter
        
    

