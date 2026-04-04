from typing import List


def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    fungi_at_tree = [-1 for _ in range(len(G))]
    n_of_fungi = 0
    fungi_count = 1
    
    new_infections = []
    for infect in infectedTrees:
        fungi_at_tree[infect] = n_of_fungi
        new_infections.append(infect)
        n_of_fungi+=1
    
    changing = True
    while(changing):
        changing = False
        new_infections_buff = []
        for single_tree in new_infections:
            for neighbour in G[single_tree]:
                if fungi_at_tree[neighbour] != -1:
                    continue
                
                fungi_code = fungi_at_tree[single_tree]
                #print(f"fungi: {fungi_code} to {neighbour}")
                new_infections_buff.append(neighbour)
                fungi_at_tree[neighbour] = fungi_code
                #print(f"fungi_at_tree: {fungi_at_tree}")
                #print(f"new_infections_buff: {new_infections_buff}")
                #print("-------------------------------------------------")
                if fungi_code == fungusNrToCount:
                    fungi_count += 1
                changing = True
                
        new_infections = new_infections_buff
                
        
    return fungi_count

