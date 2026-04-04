from typing import List
from collections import deque
#O(V+E)        V-rozmiar tablic time, infections ktore wypelniamy O(V)             BFS kazdy wierzcholek i krawedz przetwarzana razO(V+E)           przejscie przez infections O(V)
def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    n=len(G)
    infections=[-1]*n
    time=[-1]*n
    queue=deque()
    for i in range(len(infectedTrees)):
        tree=infectedTrees[i]
        infections[tree]=i
        time[tree]=0
        queue.append((tree,0))
    while queue:
        curr_tree,curr_time=queue.popleft()
        for neighbor in G[curr_tree]:
            if infections[neighbor]==-1:
                infections[neighbor]=infections[curr_tree]
                time [neighbor] = curr_time +1
                queue.append((neighbor,curr_time+1))
            elif time [neighbor] == curr_time +1:
                if infections[neighbor]>infections[curr_tree]:
                    infections[neighbor]=infections[curr_tree]
    count=0
    for fungus in infections:
        if fungus == fungusNrToCount:
            count+=1
    return count
                        

