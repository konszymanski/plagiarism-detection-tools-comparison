from typing import List

#zlozonosc O(V + E) bo przeszukiwanie BFS i odwiedzm kazdy wierzcholek max raz
def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    n = len(G)
    k = len(infectedTrees)
    infected_by = [-1] * n
    queue = [[] for i in range(k)]
    for i in range (k):
        tree = infectedTrees[i]
        infected_by[tree] = i
        queue[i].append(tree)
    while any(queue):
        next_level = [[] for _ in range(k)]
        for fungus in range (k):
            current_level = queue[fungus]
            queue[fungus] = []
            for node in current_level:
                for neighbor in G[node]:
                    if infected_by[neighbor] == -1:
                        next_level[fungus].append(neighbor)
        claimed = set()
        for fungus in range(k):
            for node in next_level[fungus]:
                if infected_by[node] == -1 and node not in claimed:
                    infected_by[node] = fungus
                    queue[fungus].append(node)
                    claimed.add(node)
    return infected_by.count(fungusNrToCount)


        

