from typing import List
from queue import Queue


def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    # O(V + E) - algorytm wykorzystuje przeszukiwanie BFS
    visited = set()
    counter = [1 for x in infectedTrees]
    queues = [Queue() for x in infectedTrees]
    for i,node in enumerate(infectedTrees):
        visited.add(node)
        queues[i].put(node)
    emptyQueuesCounter = 0
    while emptyQueuesCounter != len(infectedTrees):
        emptyQueuesCounter = 0
        for i, q in enumerate(queues):
            if q.empty(): emptyQueuesCounter += 1
            else:
                numberOfNodes = q.qsize()
                nodes = [q.get() for x in range(numberOfNodes)]
                for node in nodes:
                    for neighbour in G[node]:
                        if neighbour not in visited:
                            visited.add(neighbour)
                            q.put(neighbour)
                            counter[i] += 1
    return counter[fungusNrToCount]
                    
            

