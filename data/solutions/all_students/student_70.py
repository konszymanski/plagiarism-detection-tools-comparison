from typing import List
import heapq

#zlozonosc wynosi O((V + E)logV)), bo operazcje na heapie(push i pop dzialaja w czasie logV + powtarzamy push E razy, a pop V razy
#stąd ElogV + VlogV = (E + V)logV
def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    dist = {node:(float('inf'), -1) for node in range(len(G))} #waga + typ grzybu
    heap = []
    for i, node in enumerate(infectedTrees):
        dist[node] = 0, i
        heapq.heappush(heap, (0, i, node))
        
    while heap: 
        cur_d, cur_tp, node = heapq.heappop(heap)
        rec_d, rec_tp = dist[node]
        
        if cur_d > rec_d or cur_tp != rec_tp:
            continue
        
        for v in G[node]:
            d_through_node = cur_d + 1
            d_v, tp_v = dist[v]
            
            if d_through_node < d_v or (d_through_node == d_v and cur_tp < tp_v):
                dist[v] = (d_through_node, cur_tp)
                heapq.heappush(heap, (d_through_node, cur_tp, v))
                    
    res = 0
    for d, tp in dist.values():
        if tp == fungusNrToCount:
            res += 1
            
    return res
        
        
    

