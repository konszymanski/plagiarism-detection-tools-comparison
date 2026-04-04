from typing import List
from collections import deque

#złożoność obliczeniowa mojego rozwiązania to złożonośc BFSu czyli O(V + E)
#V - ilość drzew (wierzchołków), E - ilość korzeni (krawędzi)

def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    
    n = len(G)
    Q=deque()
    index_is_treeNum__value_is_fungiNum=[-1]*n
    time_arr = [-1]*n
    
    for i in range(len(infectedTrees)):
        index_is_treeNum__value_is_fungiNum[infectedTrees[i]] = i
        time_arr[infectedTrees[i]] = 0
        Q.append((infectedTrees[i], 0, i)) #drzewo, czas, grzyb
        
    while len(Q)>0:
        tree=Q[0][0]
        time=Q[0][1]
        fungus=Q[0][2]
        Q.popleft() #O(1)
        
        for neighbour in G[tree]:
            if index_is_treeNum__value_is_fungiNum[neighbour]==-1:
                index_is_treeNum__value_is_fungiNum[neighbour] = fungus
                time_arr[neighbour]= time+1
                Q.append((neighbour, time+1, fungus))
            
            else:
                if time+1==time_arr[neighbour]:
                    if index_is_treeNum__value_is_fungiNum[neighbour] > fungus:
                        index_is_treeNum__value_is_fungiNum[neighbour] = fungus
        
    return index_is_treeNum__value_is_fungiNum.count(fungusNrToCount) #O(V)


#zwykła tablica zamiast kolejki - O(n^2)
"""
    n = len(G)
    Q=[]
    index_is_treeNum__value_is_fungiNum=[-1]*n
    time_arr = [-1]*n
    
    for i in range(len(infectedTrees)):
        index_is_treeNum__value_is_fungiNum[infectedTrees[i]] = i
        time_arr[infectedTrees[i]] = 0
        Q.append((infectedTrees[i], 0, i)) #drzewo, czas, grzyb
        
    while len(Q)>0:
        tree=Q[0][0]
        time=Q[0][1]
        fungus=Q[0][2]
        Q.pop(0)
        
        for neighbour in G[tree]:
            if index_is_treeNum__value_is_fungiNum[neighbour]==-1:
                index_is_treeNum__value_is_fungiNum[neighbour] = fungus
                time_arr[neighbour]= time+1
                Q.append((neighbour, time+1, fungus))
            
            else:
                if time+1==time_arr[neighbour]:
                    if index_is_treeNum__value_is_fungiNum[neighbour] > fungus:
                        index_is_treeNum__value_is_fungiNum[neighbour] = fungus
        
    return index_is_treeNum__value_is_fungiNum.count(fungusNrToCount)
"""


