from typing import List
from collections import deque


# na podstawie funkcji BFS, zlozonosc BFS to O(V + E), gdzie V to liczba wierzcholkow, w tym przypadku drzew
# a E to liczba krawedzi, ktorymi polaczone sa drzewa, dziala to tak, że każdy wierzcholek macierzy odiwedzamy raz (V)
# i sprawdzamy dla kazdego z nich jego sasiadow (przez krawedzie E)
def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int: 
    
    Q = deque()
    parent = {} # slownik do drzewa BFS
    discovered = {} # slownik, ktory zbiera jakim grzybem jest zakazony kazdy wierzcholek
    
    for i in range (len(infectedTrees)):
        discovered[infectedTrees[i]] = i
        tree = infectedTrees[i]
        Q.append([i, tree]) # kolejka zbiera fungusNr i jakie drzewo
        
    while len(Q) > 0:
        last = Q.popleft()
        f_nr = last[0]
        v = last[1]
        
        for neighbour in G[v]:
            if neighbour not in discovered:
                discovered[neighbour] = f_nr
                parent[neighbour] = v
                Q.append([f_nr, neighbour])
    
    count = 0;
    for v in discovered.values(): # liczy ile drzew jest zarazonych szukanym grzybem
        if v == fungusNrToCount:
            count += 1
            
    return count

