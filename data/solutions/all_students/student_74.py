from typing import List


def Sasiednie(graph, fungus_dict,drzewo, do_zainfekowania: dict, fungus_nr):    #zapisuje do slownika jakie drzewa maja byc zainfekowane w danym cyklu przez jakie grzyby

    for sasiad in graph[drzewo]:
        if sasiad not in fungus_dict:                      #jesli to drzewo nie jest juz zainfekowane to przepuszczamy
            if sasiad not in do_zainfekowania:
                do_zainfekowania[sasiad] = fungus_nr       #przypisujemy sasiadowi(drzewu) numer grzyba, ktorym bedzie infekowany
            
            elif do_zainfekowania[sasiad] > fungus_nr:     #jesli sasiad ma juz numer grzyba to sprawdzamy czy jest mniejszy grzyb
                do_zainfekowania[sasiad] = fungus_nr
        
def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    
    fungus_dict = {}     #tworzymy slownik, ktory dla danego drzewa bedzie trzymal ktorym grzybem jest zainfekowany
    for i in range(0, len(infectedTrees)):
        fungus_dict[infectedTrees[i]] = i 
        
    while len(fungus_dict) != len(G):
        do_zainfekowania = {}
        
        for drzewo in infectedTrees:                        #wywolujemy funkjce sasiednie na wszystkich zainfekowanych drzewach w danym cyklu i otrzymamy slownik 
            Sasiednie(G, fungus_dict, drzewo, do_zainfekowania, fungus_dict[drzewo])     # do_zainfekowania ktory powie nam jakim grzybem infekujemy jakie drzewa w tym cyklu
        
        infectedTrees = []                      #czyscimy liste zainfekowanych drzew
        for drzewo, grzyb in do_zainfekowania.items():              #dodajemy do fungus_dict nowo zainfekowane drzewa
            fungus_dict[drzewo] = grzyb
            infectedTrees.append(drzewo)        #dodajemy zainfekowane drzewa w tym cyklu
            
    wynik=0
    for grzyb in fungus_dict.values():       #zliczamy ile drzew ma szukanego grzyba
        if grzyb == fungusNrToCount:
            wynik+=1
            
    return wynik


