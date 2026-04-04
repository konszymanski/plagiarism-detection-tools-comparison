from typing import List
from collections import deque


def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    #zlozonosc O(N+E) gdzie N to liczba drzew a E to liczba polaczen miedzy nimi
    num_trees = len(G)
    curr_infection_status = [-1] * num_trees
    #tutaj przechowujemy numer grzyba, ktory opanowal drzewo
    #-1 oznacza ze drzewo nie jest opanowane
    
    q=deque() #teraz kolejka do przechowywania drzew, ktore zostaly opanowanr w biezacej turze
    #i z ktorych dalej beda sie rozprzestrzeniac

    #grzyby sa wszczepiane do poczatkowych drzew
    for i, tree_idx in enumerate(infectedTrees):
        #dotyka grzyb drzewa
        curr_infection_status[tree_idx] = i
        q.append((tree_idx, i))
    
    while q:
        tree, grzyb = q.popleft() #zdejmujemy drzewo numer
        for x in G[tree]: #dla kazdego drzewa x ktore jest polaczone z tree
            if curr_infection_status[x] == -1: #sprawdzamy czy drzewo x nie zostalo jeszcze opanowane przez zaden grzyb
                curr_infection_status[x] = grzyb #a jak tak infekujemy
                q.append((x,grzyb)) #i dodajemys
    
    return curr_infection_status.count(fungusNrToCount) #ile zainfekowanych






    pass # TODO

