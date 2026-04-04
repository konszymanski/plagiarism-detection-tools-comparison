from typing import List


def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    #zlozonosc O(V+E), poniewaz kazdy wierzcholek i kazda krawedz odwiedzamy tylko raz
    
    n=len(G)
    
    opanowane=[-1]*n
    czas_inf=[-1]*n
    q=[]
    
    for i in range(len(infectedTrees)):
        drzewo=infectedTrees[i]
        opanowane[drzewo]=i
        czas_inf[drzewo]=0
        q.append((drzewo, 0))
    
    
    while q:
        curr_drzewo, curr_czas = q.pop(0)
        
        for sasiad in G[curr_drzewo]:
            if(opanowane[sasiad]==-1):
                opanowane[sasiad]=opanowane[curr_drzewo]
                czas_inf[sasiad]=curr_czas+1
                q.append((sasiad, curr_czas+1))
            
            elif(czas_inf[sasiad]==curr_czas+1 and opanowane[sasiad]>opanowane[curr_drzewo]):
                opanowane[sasiad]=opanowane[curr_drzewo]
                
    
    l=0
    for i in range(n):
        if(opanowane[i]==fungusNrToCount):
            l+=1
    return l
                
    
    
    
    
    
    
    

