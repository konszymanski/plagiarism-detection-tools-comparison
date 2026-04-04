from typing import List
from collections import defaultdict #slownik z ustalanym typem wartosci


def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int: #O(n^4) 4 petle:I
    n = len(G) #ilosc drzew
    infectedMap = {i : -1 for i in range(n)} # tworzymy mape infekcji (-1 oznacza zdrowe drzewa)
        
    for i in range(0, len(infectedTrees)):
        infectedMap[infectedTrees[i]] = i #zapisujemy pierwsze zainfekowane drzewa na mapie

    didChange = True #sprawdza czy zostalo jeszcze cokolwiek do zmiany (jesli nie konczy petle while)
    while(didChange):
        didChange = False
        proposals = defaultdict(list) #slownik zbierajacy propozycje infekcji danego drzewa przez rozne grzyby 
        for tree in range(0, n):
            if infectedMap[tree] != -1:
                for neighbour in G[tree]:
                    if infectedMap[neighbour] == -1:
                        #sprawdzamy czy sasiad ma sasiadow zainfekowanych nizszym indeksem:
                        doesInfect = True
                        for neighbourNext in G[neighbour]:
                            if infectedMap[neighbourNext] < infectedMap[tree] and infectedMap[neighbourNext] != -1:
                                doesInfect = False
                                break
                        #jesli nie to proponujemy infekcje drzewa:
                        if doesInfect: 
                            proposals[neighbour].append(infectedMap[tree])
                            didChange = True
        for tree in proposals.keys(): #z propozycji infekcji drzew wybieramy grzyby o najmniejszym indeksie
            winner = min(proposals[tree])
            infectedMap[tree] = winner    
        
    result = 0
    for i in infectedMap.values():
        if i == fungusNrToCount:
            result += 1
    return result

