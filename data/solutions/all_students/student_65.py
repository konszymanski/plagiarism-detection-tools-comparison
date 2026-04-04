from typing import List


# zlozonosc to O(|V| + |E|), poniewaz kazdy wierzcholek pojawia sie raz w kolejce,
# a wewnetrzny for iteruje po sasiadach kazdego wierzcholka co znaczy ze przechodzimy po O(|E|)
def BFS(G, source):
    infected = {}
    queue = []
    
    for t, f in source:
        infected[t] = f
        queue.append((t, f))
        
    while queue:
        tree, fungus = queue.pop(0)
        for neighbor in G[tree]:
            if neighbor not in infected:
                infected[neighbor] = fungus
                queue.append((neighbor, fungus))
    
    return infected


# zlozonosc to O(|V| + |E|), jako ze najbardziej kosztownym jest wywolanie BFS(), wiec na zlozonosc
# nie wplywaja obie petle for o zlozonosciach O(|V|)
def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    fungus = []
    for t in range(len(infectedTrees)):
        fungus.append((infectedTrees[t], t))
    
    infected = BFS(G, fungus)
    
    ans = sum(1 for f in infected.values() if f == fungusNrToCount)
    
    return ans


