from typing import List


# zlozonosc to O(|V| + |E|) poniewaz kazda krawedz i kazdy wierzcholek przechodzimy raz

def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    queue = []
    infection = [(-1,-1)]*len(G)
    for tree in infectedTrees:
        infection[tree] = (0, infectedTrees.index(tree))
        queue.append((tree, 0, infectedTrees.index(tree)))
    
    while queue:
        tree, time, mushroom = queue.pop(0)
        for neighbour in G[tree]:
            if infection[neighbour][0] == -1:
                infection[neighbour] = (time+1, mushroom)
                queue.append((neighbour, time+1, mushroom))
            elif infection[neighbour][0] == time+1 and mushroom < infection[neighbour][1]:
                infection[neighbour][0] = (time + 1, mushroom)
                queue.append((neighbour, time + 1, mushroom))
    
    
    counter = 0
    for time, mushroom in infection:
        if mushroom == fungusNrToCount:
            counter += 1
    
    return counter
        

