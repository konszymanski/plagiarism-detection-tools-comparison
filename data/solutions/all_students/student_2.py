from typing import List
import collections
# O(V + E) czasowa - jak BFS
def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    known_trees = set()
    # robimy kolejke, jak do BFS
    # osobna dla kazdego grzyba
    queue = [collections.deque([idx]) for idx in infectedTrees]
    # na poczatku w kazdej kolejce jest po jednym drzewie (drzewo startowe)
    
    # index_drzewa: grzyb
    infected = {} 
    while len(infected) != len(G):
        # zajmujemy sie rozrostem 
        # grzyba z danego drzewa w kolejnosci indeksow
        for fungusIdx in range(len(infectedTrees)):
            current_queue = queue[fungusIdx]
            # wykonujemy jeden cykl pracy dla kolejki
            # (czyli nie dodajemy w petli kolejnych elementow do kolejki, 
            # tylko na koncu) - uznajemy ze z lewej najmlodszy, z prawej najstarszy
            neighbors = []
            while len(current_queue) > 0:
                current_tree = current_queue.pop()
                neighbors.extend( G[current_tree] )
                if current_tree not in infected:
                    infected[current_tree] = fungusIdx
            current_queue.extendleft(neighbors)
            
    return list(infected.values()).count(fungusNrToCount)

