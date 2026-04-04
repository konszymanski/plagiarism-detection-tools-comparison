from typing import List


from typing import List

def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    liczba_drzew = len(G)
    if liczba_drzew == 0:
        return 0

    wlasciciel = [-1] * liczba_drzew
    czas_infekcji = [-1] * liczba_drzew
    kolejka = []

    for numer_grzyba, numer_drzewa in enumerate(infectedTrees):
        if wlasciciel[numer_drzewa] == -1 or numer_grzyba < wlasciciel[numer_drzewa]:
            if wlasciciel[numer_drzewa] == -1:
                kolejka.append(numer_drzewa)
            wlasciciel[numer_drzewa] = numer_grzyba
            czas_infekcji[numer_drzewa] = 0
            
    glowa_kolejki = 0
    while glowa_kolejki < len(kolejka):
        obecne_drzewo = kolejka[glowa_kolejki]
        glowa_kolejki += 1

        atakujacy_grzyb = wlasciciel[obecne_drzewo]
        czas_dotarcia_do_sasiadow = czas_infekcji[obecne_drzewo] + 1
        
        for sasiad in G[obecne_drzewo]:
            if czas_infekcji[sasiad] == -1:
                czas_infekcji[sasiad] = czas_dotarcia_do_sasiadow
                wlasciciel[sasiad] = atakujacy_grzyb
                kolejka.append(sasiad)
            elif czas_infekcji[sasiad] == czas_dotarcia_do_sasiadow:
                if atakujacy_grzyb < wlasciciel[sasiad]:
                    wlasciciel[sasiad] = atakujacy_grzyb

    licznik = 0
    for wlasciciel_drzewa in wlasciciel:
        if wlasciciel_drzewa == fungusNrToCount:
            licznik += 1
            
    return licznik

