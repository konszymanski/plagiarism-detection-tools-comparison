from typing import List
import copy
def infekcja(index, tablica, jaka, graf):
    tablica2 = graf[index]
    for i in tablica2:
        if tablica[i] == -1:
            tablica[i] = jaka
#Zlozonosc to O(k*(n+m)), gdzie k to liczba grzybow, n -liczba drzew, a m- liczba krawedzi grafu, bo dla kazdego grzyba przechodzimy po calym grafie
def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    pom = []
    for i in range(len(G)):
        pom.append(-1)
    for i in range(len(infectedTrees)):
        pom[infectedTrees[i]] = i
    while -1 in pom:
        pom1 = copy.deepcopy(pom)
        for i in range(len(infectedTrees)):
            for j in range(len(pom)):
                if pom[j] == i:
                    infekcja(j, pom1, i, G)
        pom = pom1
    return pom.count(fungusNrToCount)
