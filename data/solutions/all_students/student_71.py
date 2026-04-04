from typing import List
from collections import deque


def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    #Złożoność czasowa: O(n)
    #Uzasadnienie: Przechodzimy przez graf metodą BFS z wieloma źródłami
    visited = [False]*len(G)
    q = deque(())
    result = 0
    for i in range(len(infectedTrees)):
        visited[infectedTrees[i]] = True
        q.append((infectedTrees[i], i))
    while q:
        node, root_node = q.popleft()
        if root_node == fungusNrToCount:
            result += 1
        for neighbor in G[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append((neighbor, root_node))
    return result

