from typing import List
from queue import Queue

def get_parent(x, mapp, source):
    if mapp.get(x, None) is None:
        return False
    if mapp[x][0] == source:
        return True
    return get_parent(mapp[x][0], mapp, source)
      
def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    # zlożoność bfs = O(V+E), sprawdzanie na końcu O(E*log(E)) -> O(V + E*log(E))
    if not infectedTrees:
        return 0
    if not G:
        return 0
    if fungusNrToCount < 0:
        return 0
    q = Queue()
    disc = set()
    parent = {}
    for i in infectedTrees:
        q.put(i)
        disc.add(i)
    while not q.empty():
        v = q.get()
        i = 0
        for n in G[v]:
            i+=1
            if n not in disc:
                disc.add(n)
                parent[n] = v, i
                q.put(n)
    res = 1
    for x in disc:
        if get_parent(x, parent, infectedTrees[fungusNrToCount]):
            res+=1
    return res

