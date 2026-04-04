from typing import List, Dict, Set
import collections

'''
Złożoność czasowa O(M + N*K):
analizujemy wszystkie krawędzie grafu (M)
dla N wierzchołków lub w N krokach, wykonywane są operacje zależne od K "grzybów".
'''

def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    N = len(G)
    if N == 0:
        return 0
    num_fungi = len(infectedTrees)
    if num_fungi == 0:
        return 0
    infected_by = [-1] * N
    q = [[] for _ in range(num_fungi)]

    tree_to_initial_fungi: Dict[int, List[int]] = collections.defaultdict(list)
    for f_idx, tree_node in enumerate(infectedTrees):
        if 0 <= tree_node < N:
             tree_to_initial_fungi[tree_node].append(f_idx)

    for tree_node, competing_f_indices in tree_to_initial_fungi.items():
        if competing_f_indices:
            winner_f_idx = min(competing_f_indices)
            infected_by[tree_node] = winner_f_idx
            q[winner_f_idx].append(tree_node)

    while True:
        any_new_infection_in_step = False
        potential_infections_this_step: Dict[int, List[int]] = collections.defaultdict(list)

        for f_idx in range(num_fungi):
            for u_node in q[f_idx]:
                if infected_by[u_node] != f_idx : continue
                for v_neighbor in G[u_node]:
                    if infected_by[v_neighbor] == -1:
                        potential_infections_this_step[v_neighbor].append(f_idx)
        
        if not potential_infections_this_step:
            break 

        next_q = [[] for _ in range(num_fungi)]
        
        for target_node, competing_fungi in potential_infections_this_step.items():
            if infected_by[target_node] == -1 and competing_fungi:
                winner_f_idx = min(competing_fungi)
                infected_by[target_node] = winner_f_idx
                next_q[winner_f_idx].append(target_node)
                any_new_infection_in_step = True
        
        q = next_q
        if not any_new_infection_in_step:
            break

    count = 0
    for f_id_in_tree in infected_by:
        if f_id_in_tree == fungusNrToCount:
            count += 1
    return count
    
