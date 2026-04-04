from typing import List


def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    #zlozonosc obliczeniowa wynosi O(n*m*i) gdzie n = liczba drzew, m = liczba połączeń, i = liczba początkowo zainfekowanych drzew

    n = len(G)
    infected = [0]*n
    for i in infectedTrees:
        infected[i]=1
    count = {i : 1 for i in range(len(infectedTrees))}
    infectoroftree = {infectedTrees[i]: i for i in range(len(infectedTrees))}
    
    while sum(infected)!= n:
        newinfected = []
        for tree in range(len(infectedTrees)):
            for con in G[infectedTrees[tree]]:
                if infected[con]==0:
                    newinfected.append(con)
                    infected[con]=1
                    infectoroftree[con] = infectoroftree[infectedTrees[tree]]
                    count[infectoroftree[infectedTrees[tree]]]+=1
                    
        infectedTrees = newinfected
        
    return count[fungusNrToCount]

