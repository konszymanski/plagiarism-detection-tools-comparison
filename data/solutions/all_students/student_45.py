from typing import List


def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    queue = []
    fungus_index_tree = [-1] * len(G)
    iteration = 0
    for fungus_idx , tree_idx in enumerate(infectedTrees):
        fungus_index_tree[tree_idx] = fungus_idx
        queue.append((0,tree_idx,fungus_idx))
    while len(queue)>0:
        iteration , tree_idx , fungus_idx = queue[0][0] , queue[0][1] , queue[0][2]
        queue.pop(0)
        for neighbor in G[tree_idx]:
            if fungus_index_tree[neighbor] == -1:
                fungus_index_tree[neighbor] = fungus_idx
                queue.append((iteration+1,neighbor,fungus_idx))
    count = 0
    for idx in fungus_index_tree:
        if fungus_index_tree[idx]==fungusNrToCount:
            count+=1
    return count
            
    

