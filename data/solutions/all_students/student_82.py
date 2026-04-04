from typing import List


def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    liczba_drzew = len(G)
    liczba_grzybow = len(infectedTrees)
    stan_drzewa = [-1] * liczba_drzew
    for j in range(liczba_grzybow):
        stan_drzewa[infectedTrees[j]] = j

    g_queue = [[] for _ in range(liczba_grzybow)]
    for j in range(liczba_grzybow):
        g_queue[j].append(infectedTrees[j])

    while True:
        if all(len(kolejka) == 0 for kolejka in g_queue):
            break

        new_queue = [[] for _ in range(liczba_grzybow)]
        mozliwe = {}

        for nr_grzyba in range(liczba_grzybow):
            for drzewo in g_queue[nr_grzyba]:
                for sasiad in G[drzewo]:
                    if stan_drzewa[sasiad] == -1:
                        if sasiad not in mozliwe:
                            mozliwe[sasiad] = []
                        mozliwe[sasiad].append(nr_grzyba)

        for drzewo, konkurujace_grzyby in mozliwe.items():
            zwyciezca = min(konkurujace_grzyby)
            stan_drzewa[drzewo] = zwyciezca
            new_queue[zwyciezca].append(drzewo)

        g_queue = new_queue

    licznik = 0
    for stan in stan_drzewa:
        if stan == fungusNrToCount:
            licznik += 1

    return licznik


