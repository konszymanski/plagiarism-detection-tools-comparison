from typing import List
import heapq


def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    visited=[None]*len(G)
    koleja=[]
    for i in range(len(infectedTrees)):
        warchol=infectedTrees[i]
        visited[warchol]=i
        nrgrzybulca=i
        heapq.heappush(koleja,(0,nrgrzybulca,warchol))
    
    while koleja:
        droga,nrgrzybuliny,krzok=heapq.heappop(koleja)
        
        for sa_siatka in G[krzok]:
            if visited[sa_siatka] is None:
                visited[sa_siatka]=nrgrzybuliny
                heapq.heappush(koleja,(droga+1,nrgrzybuliny,sa_siatka))
    
    counter=0
    for i in range(len(visited)):
        if visited[i]==fungusNrToCount:
            counter+=1
    return counter

