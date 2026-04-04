from typing import List

'''pierwsza pętla "for" ma złozonosc O(V), gdzie V to liczba wierzchołków grafu,
druga "for" ma złożoność O(n), gdzie n to liczba początkowo zainfekowanych drzew.
Petla "while" ma w sumie złożoność O(V^2 + E), gdzie V i E to liczba wierzchołków
i krawędzi w grafie. Ostatnia pętla "for" ma O(V). Całość ma więc O(V^2 + E).
'''

def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    queue = []
    infected={}
    for i in range(len(G)):
        infected[i]=-1
    
    fungus_nr=0
    for i in infectedTrees:
        infected[i]=fungus_nr
        fungus_nr+=1
        queue.append(i)
    
    while queue:
        v = queue.pop(0) #to O(n), wiec while ma O(V^2 + E)
        for neighbour in G[v]:
            if infected[neighbour] == -1:
                infected[neighbour]= infected[v]
                queue.append(neighbour)
                #print(queue)
    
    licznik=0
    for tree,fung in infected.items():
        if fung == fungusNrToCount:
            licznik+=1
            
    return licznik


