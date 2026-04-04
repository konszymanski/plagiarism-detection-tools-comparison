from typing import List
#złozoność to O(n)

def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    queue = []
    fungus = [-1] * len(G)
    l = [None]  * len(G)
    
    for i in range(len(infectedTrees)):
        fungus[infectedTrees[i]] = i
        l[infectedTrees[i]] = 0
        queue.append([infectedTrees[i], i, 0])
        
    while queue:
        temp = queue.pop(0)
        tree = temp[0]
        
        for i in G[tree]:
            if fungus[i] == -1:
                fungus[i] = temp[1]
                l[i] = temp[2] + 1
                queue.append([i, temp[1], temp[2] + 1])
            elif fungus[i] > i and l[i] == temp[2] + 1:
                fungus[i] = temp[1]
                queue.append([i, temp[1], temp[2] + 1])
                
    count = 0
    for i in fungus:
        if i == fungusNrToCount:
            count += 1
    return count
    

