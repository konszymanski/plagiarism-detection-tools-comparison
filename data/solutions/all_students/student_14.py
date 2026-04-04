from typing import List

def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    #Złożoność czasowa wynosi O(V+E), ponieważ uzywam BFS, gdzie V to liczba wierzchołków grafu a E to liczba krawędzi. 
    infekcje = {}
    Q=[]
    parent_inf = {} 
    time={}
    nr = 0
    for i in infectedTrees:
        infekcje[nr] = [i]
        Q.append((i, nr))
        time[i]=0
        parent_inf[i] = nr 
        nr+=1
    while(Q):
        now, nr_in = Q.pop(0)
        t = time[now]
        for i in G[now]:
            if i not in time.keys():
                time[i] = t+1
                parent_inf[i] = nr_in
                infekcje[nr_in].append(i)
                Q.append((i, nr_in))
            elif time[i]==t+1 and nr_in<parent_inf[i]:
                infekcje[parent_inf[i]].remove(i)
                infekcje[nr_in].append(i)
                parent_inf[i] = nr_in
    return len(infekcje[fungusNrToCount])
