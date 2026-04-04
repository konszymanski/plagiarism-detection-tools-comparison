from typing import List
from collections import deque

def get_distance(matrix,source, target):
    queue = deque([(source, 0)])
    visited = []
    
    while queue is not None:
        node,dist = queue.popleft()
        if node == target:
            return dist
        if node not in visited:
            visited.append(node)
        
        if not matrix[node]:
            neighbours=[]
        else:
            neighbours = matrix[node]
        for x in neighbours:
            queue.append((x, dist +1))
    
    
def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    dict = {}
    infected = {}
    count = 0
    for node in range(len(G)):
        distance = []
        if node not in infectedTrees:
            for x in infectedTrees:
                dist = get_distance(G, node, x )
                distance.append(dist)
        dict[node] = distance
        
    for node, dist in dict.items():
        if dist:
            infected[node] = dist.index(min(dist))
    
    for node in infected:
        if infected[node] == fungusNrToCount:
            count += 1
    return count +1
        

