from typing import List

# Złożoność czasowa 0(n^2*m) (n - liczba wierzchołków w grafie, m - liczba krawędzi w grafie). Szukamy minimalnego wierzchołka w pętli po wszystkich wierzchołkach n razy, a każda taka pętla zajmuje O(n), stąd mamy O(n^2). I sąsiedzi zajmują czas O(m). Łącznie mamy O(n^2 + m)
def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    n = len(G)
    dist = [float('inf')]*n
    parent = [-1]*n
    visited = [False]*n
    
    for fungus_index, tree in enumerate(infectedTrees):
        dist[tree] = 0
        parent[tree] = fungus_index
        
    nodes = list(range(n))
    for i in range(n):
        min_node = -1
        for node in nodes:
            if not visited[node]:
                if min_node == -1 or dist[node] < dist[min_node] or (dist[node] == dist[min_node] and parent[node] < parent[min_node]):
                    min_node = node
                    
        if min_node == -1 or dist[min_node] == float('-inf'):
            break
        
        visited[min_node] = True
        for neighbor in G[min_node]:
            if visited[neighbor]:
                continue
            new_dist = dist[min_node] + 1
            
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                parent[neighbor] = parent[min_node]
            elif new_dist == dist[neighbor] and parent[min_node] < parent[neighbor]:
                parent[neighbor] = parent[min_node]
                
    return parent.count(fungusNrToCount)

