from typing import List
#złożoność tutaj to O(E+V)
#przez kazdy wierzchołek przechodzmy raz bo będzie zapisywany w zbiorze już wykorzystanych
# i każdą krawędź również odwiedzamy tylko raz

def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    
    dic={}
    zbior=set()
    c=[]
    for i in range(len(infectedTrees)):
        dic[i]=[infectedTrees[i]]
        zbior.add(infectedTrees[i])
        
    while len(zbior) != len(G):
        for x in dic:
            c = []
            for y in dic[x]:
                for z in G[y]:
                    if(z not in zbior):
                        c.append(z)
                        zbior.add(z)
                        
                        
                        
            for p in c:
                dic[x].append(p)



    return len(dic[fungusNrToCount])    
    
    
    
    
    
    
    
    
    
    
    
    pass # TODO

