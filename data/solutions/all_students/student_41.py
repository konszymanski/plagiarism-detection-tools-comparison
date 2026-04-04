from typing import List
from collections import deque

class Tree:
    def __init__(self, fungusNr, timeStep):
        self.fungusNr = fungusNr
        self.timeStep = timeStep
    
    def update(self, other) -> bool:
        if other.timeStep + 1 < self.timeStep:
            self.fungusNr = other.fungusNr
            self.timeStep = other.timeStep + 1
            return True
        if other.timeStep + 1 == self.timeStep and other.fungusNr < self.fungusNr:
            self.fungusNr = other.fungusNr
            return True
        return False
    
    def incrementCopy(self):
        return Tree(self.fungusNr, self.timeStep + 1)
    
    def __str__(self):
        return f"[{self.fungusNr}, {self.timeStep}] "

def BFS(G: List[List[int]], x: int, V: List) -> None:
    q = deque()
    q.append(x)
    while(q):
        prev = q.popleft()
        for succ in G[prev]:
            if V[succ] is None:
                V[succ] = V[prev].incrementCopy()
                q.append(succ)
            elif V[succ].update(V[prev]):
                q.append(succ)

# n to len(infectedTrees)
# złożoność tej funkcji to O(n * (V + E) + V) = O(nV + nE + V)
# możemy założyć że n >= 1, dla innych wartości ta funkcja nie ma sensu więc
# O(nV + nE) to finalna złożonoś czasowa
def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    V: List = [None] * len(G)
    for fungusNr, treeNr in enumerate(infectedTrees): # pętla wykona się n razy
        V[treeNr] = Tree(fungusNr, 0) # O(1)
        BFS(G, treeNr, V) # algorytm BFS ma złożoność O(V + E)
    count = 0
    for vert in filter(lambda x: x is not None, V): # pętla wykona się V razy
        count += vert.fungusNr == fungusNrToCount # złożoność czasowa O(1)
    return count

