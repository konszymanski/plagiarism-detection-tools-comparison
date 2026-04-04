from typing import List
from collections import deque

#złożoność czasowa: O(V+E) [V - liczba node'ów, E - liczba krawędzi] - program przechodzi raz po kazdym wierzcholku i kazdej krawędzi 

def infect_neighbours(G: List[List[int]], current_node: int, current_fungus: int, current_time: int, fungus_info: List[(tuple)]) -> None:
    for neighbour in G[current_node]:
        if fungus_info[neighbour][0] == -1:
            fungus_info[neighbour] = (current_fungus, current_time+1)
        elif fungus_info[neighbour][1] == current_time+1:
            if current_fungus < fungus_info[neighbour][0]:
                fungus_info[neighbour] = (current_fungus, current_time+1)


def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    if not G: return 0
    
    num_nodes = len(G)
    fungus_info = [(-1,-1) for _ in range(num_nodes)]
    queue = deque()
    
    for index, tree in enumerate(infectedTrees):
        fungus_info[tree] = (index, 0)
        queue.append((tree, index, 0))
        
    while queue:
        current_node, current_fungus, current_time = queue.popleft()
        infect_neighbours(G, current_node, current_fungus, current_time, fungus_info)
        for neighbour in G[current_node]:
            if fungus_info[neighbour][0] != -1 and fungus_info[neighbour][1] == current_time+1:
                queue.append((neighbour, fungus_info[neighbour][0], current_time+1))
                
    count = 0
    for node in range(num_nodes):
        if fungus_info[node][0] == fungusNrToCount:
            count += 1
    
    return count
        
