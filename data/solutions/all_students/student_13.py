from typing import List
from collections import deque

def bfs(G, infected, queue):
    while queue:
        node, fungus = queue.popleft()
        
        for neighbor in G[node]:
            if infected[neighbor] == -1:
                infected[neighbor] = fungus
                queue.append((neighbor, fungus))


def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    # O(V + N), gdzie V - liczba drzew, a N - liczba połączeń miedzu drzewami
    # i musimy przejść przez każdy wierzchołek co najwyżej raz, a przez krawędź
    # co najwyżej dwa razy żeby zainfekować wszystkie drzewa
    n = len(G)
    infected = [-1] * n
    queue = deque()
    
    for fungus, tree in enumerate(infectedTrees):
        infected[tree] = fungus
        queue.append((tree, fungus))
        
    bfs(G, infected, queue)
    
    num = infected.count(fungusNrToCount)
    
    return num

