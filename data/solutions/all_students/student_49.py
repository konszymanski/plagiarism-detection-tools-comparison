from typing import List
from queue import Queue

#O(V+E) - przechodzę po każdej krawędzi dokładnie raz i po każdym wierzchłku dokładnie raz
def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    V=len(G)
    q=Queue()
    visited=[-1]*V
    for i,inf in enumerate(infectedTrees):
        q.put((inf,i))
    
    while not q.empty():
        infect,virus=q.get()
        if not(0<=infect<V):
            continue
        if visited[infect]!=-1:
            continue
        visited[infect]=virus
        for i in G[infect]:
            q.put((i,virus))
        
    count=0
    for i in visited:
        if i==fungusNrToCount: count+=1
    return count

