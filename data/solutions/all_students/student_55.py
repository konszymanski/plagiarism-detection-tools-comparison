from typing import List
import heapq


#ZŁOŻONOŚĆ: O((N + E) * log N) dla N - liczba drzew (czyli wierzchołków grafu), E to liczba połączeń między drzewami (czyli krawędzi),log N pochodzi z operacji na kolejce priorytetowej (heapq)
#infected_by i time mają rozmiar n, więc: O(N), każdy z K początkowych grzybów trafia do heap: O(K log K) (ale zwykle K ≤ N, więc można to zawrzeć w O(N log N))
#W najgorszym przypadku każdy wierzchołek może być dodany do kolejki wielokrotnie (dla różnych grzybów lub lepszych czasów infekcji), łącznie wykonamy co najwyżej O(N + E) operacji heappush i heappop, każda z nich kosztuje O(log N), dlatego mamy: O((N + E) × log N)


def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    n = len(G)
    infected_by = [-1] * n 
    time = [float('inf')] * n 
    heap = []

    for fungus_idx, tree in enumerate(infectedTrees):
        infected_by[tree] = fungus_idx
        time[tree] = 0
        heapq.heappush(heap, (0, fungus_idx, tree))  

    while heap:
        t, fungus_idx, node = heapq.heappop(heap)
        if time[node] < t or infected_by[node] < fungus_idx:
            continue  
        for neighbor in G[node]:
            if time[neighbor] > t + 1:
                time[neighbor] = t + 1
                infected_by[neighbor] = fungus_idx
                heapq.heappush(heap, (t + 1, fungus_idx, neighbor))
            elif time[neighbor] == t + 1 and fungus_idx < infected_by[neighbor]:
                infected_by[neighbor] = fungus_idx
                heapq.heappush(heap, (t + 1, fungus_idx, neighbor))

    return infected_by.count(fungusNrToCount)

