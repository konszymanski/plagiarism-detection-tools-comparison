from typing import List
from collections import deque

# O(n + m), bo przechodzimy po kazdemy wierzcholku 1 raz i 2 razy patrzymy kazda krawedz
def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    n = len(G)
    visited = [-1] * n
    
    q = deque()
    
    for fungus_nr, tree in enumerate(infectedTrees):
        visited[tree] = fungus_nr
        q.append(tree) # od razu rzucamy do kolejki
    
    while q:
        cur_tree = q.popleft()
        
        for neighbour in G[cur_tree]:
            if visited[neighbour] == -1:
                visited[neighbour] = visited[cur_tree]
                q.append(neighbour)
        
    return visited.count(fungusNrToCount)
    

