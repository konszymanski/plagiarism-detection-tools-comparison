from typing import List

#złoność (V+E) - przechodzimy raz przez każdy wiezchołek (podczas infekcji) oraz raz przez każdą krawędź
def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    infected = {} #id grzyba: List[id_drzewa]
    free = [x for x in range(len(G)) if x not in infectedTrees]
    grzyby = []
    queues = {} #id_grzyba: queue
    
    for id_grzyba, id_drzewa in enumerate(infectedTrees):
        infected[id_grzyba] = [id_drzewa]
        grzyby.append(id_grzyba)
        queues[id_grzyba] = [id_drzewa]
    
    def extend_infection(G: List[List[int]], grzyby: List[int]) -> bool:
        new_infections = {}
        result = False
        for id_grzyba in grzyby:
            new_queue = []
            while queues[id_grzyba]:
                node = queues[id_grzyba].pop(0)
                for child in G[node]:
                    if child in free:
                        free.remove(child)
                        new_queue.append(child)
                        infected[id_grzyba].append(child)
                        result = True
            queues[id_grzyba] = new_queue
        return result
        
    while extend_infection(G, grzyby):
        continue
        
    return len(infected[fungusNrToCount])
    pass # TODO

