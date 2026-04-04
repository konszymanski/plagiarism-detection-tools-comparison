from typing import List
from collections import deque

#O(V + E) dlatego, że sprawdzamy graf BFS. Liczba grzybów nie wpłynie nam na rozwiązanie, bo nie ważne ile mamy grzybów, ich wierzchołki zostają odrazu dodane do visited
def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    visited = set()
    n = len(infectedTrees) #liczba grzibów
    count = 1
    queue_list = [deque() for _ in range(n)]
    for i in range(n):
        queue_list[i].append(infectedTrees[i])
        visited.add(infectedTrees[i])
    while len(visited) < len(G):
        for i in range(n):
            if queue_list[i]:
                current_tree = queue_list[i].pop()
                if i == fungusNrToCount:
                    for j in G[current_tree]:
                        if j not in visited:
                            queue_list[i].append(j)
                            visited.add(j)
                            count += 1
                else:
                    for j in G[current_tree]:
                        if j not in visited:
                            queue_list[i].append(j)
                            visited.add(j)
    return count
        
        
