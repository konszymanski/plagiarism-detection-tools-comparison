from typing import List

# w najgorszym wypadku O(V^2) , gdzie V to liczba wierzcholkow, ponieważ w petli wewnetrznej przechodzimy
# po wszystkich wierzcholkach grafu, i dla każdego wierzcholka po wszystkich z którymi sąsiaduje (maksymalnie V-1)
# w takim przypadku while wykona sie tylko raz bo jesli wszystko polaczone to wszystko od razu sie zarazi
# jesli krawedzi jest malo to while wykona sie max. V razy więc wtedy też O(V^2)

## BUG: BEDZIE WIECZNA PETLA JESLI KTORYS WIERZCHOLEK JEST ODIZOLOWANY OD RESZTY

def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    trees = [-1]*len(G)
    for idx in range(len(infectedTrees)):
        trees[infectedTrees[idx]] = idx
    while -1 in trees:
        trees_copy = trees[:]
        for v in range(len(G)):
            if trees[v] != -1:
                continue
            min_fungus = sys.maxsize
            for neighbour in G[v]:
                if trees[neighbour] == -1:
                    continue
                min_fungus = min(trees[neighbour], min_fungus)
            if min_fungus == sys.maxsize:
                continue
            trees_copy[v] = min_fungus
        trees = trees_copy[:]
    return trees.count(fungusNrToCount)

