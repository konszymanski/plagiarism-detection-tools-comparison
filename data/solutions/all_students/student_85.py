from typing import List
from collections import deque

#Złożoność:O(v+e)
def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    n=len(G)
    if n==0:
        return 0
    infected=[(-1,-1) for _ in range(n)]
    queue=deque()
    for nr,el in enumerate(infectedTrees):
        infected[el]=(nr,0)
        queue.append((el,nr,0))
    while queue:
        c_el,c_f,c_t=queue.popleft()
        
        for el in G[c_el]:
            if(infected[el][0]==-1):
                infected[el]=(c_f,c_t+1)
                queue.append((el,c_f,c_t+1))
            elif(infected[el][1]==c_t+1):
                if(c_f<infected[el][0]):
                    infected[el]=(c_f,c_t+1)
    count=0
    for nr,_ in infected:
        if nr==fungusNrToCount:
            count+=1
    return count
    
    
    
    

