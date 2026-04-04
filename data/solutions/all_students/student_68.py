import collections
from typing import List


def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    '''
    Złożoność Czasowa: O(V + E)
    V to liczba wierzchołków w grafie .
    E to liczba krawędzi w grafie.
    '''
    num_nodes = len(G)
    if num_nodes == 0:
        return 0
        
    infected_by = [-1] * num_nodes
    frontier = []
    
    for fungus_id, node in enumerate(infectedTrees):
        if node < num_nodes and infected_by[node] == -1:
            infected_by[node] = fungus_id
            frontier.append((node, fungus_id))
    while frontier:
       
        potential_infections = collections.defaultdict(list)

        for curr_node, fungus_id in frontier:
            for neighbor in G[curr_node]:
              
                if infected_by[neighbor] == -1:
                    potential_infections[neighbor].append(fungus_id)
        
        if not potential_infections:
            break

        next_frontier = []
        
        for node_to_infect, competing_fungi in potential_infections.items():
            winner_fungus = min(competing_fungi)
            infected_by[node_to_infect] = winner_fungus
            next_frontier.append((node_to_infect, winner_fungus))
        frontier = next_frontier
        
    return infected_by.count(fungusNrToCount)
     
