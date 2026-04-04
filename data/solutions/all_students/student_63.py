from typing import List
from collections import deque

# O(liczba drzew + liczba krawędzie) - złożoność czasowa, dwie pętle for

def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    
    number_of_trees = len(G)
    fungus_owner = [-1]*number_of_trees
    spreading_queue = deque()
    
    for fungus_type, tree in enumerate(infectedTrees):
        fungus_owner[tree] = fungus_type
        spreading_queue.append((tree, fungus_type))

    while spreading_queue:
        tree_id, fungus_type = spreading_queue.popleft()
        for connected_tree in G[tree_id]:
            if fungus_owner[connected_tree] == -1:
                fungus_owner[connected_tree] = fungus_type
                spreading_queue.append((connected_tree, fungus_type))

    return fungus_owner.count(fungusNrToCount)

#pass # TODO

