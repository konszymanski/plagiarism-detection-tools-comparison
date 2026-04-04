from typing import List
from collections import deque

def areAllInfected(Arr):
    return all(x != -1 for x in Arr)

def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    l_d = len(G)
    l_s = len(infectedTrees)
    
    infectionArray = [-1 for x in range(len(G))]
    
    for inf, ind in enumerate(infectedTrees):
        infectionArray[ind] = inf
    
    infectionPlans = [[] for x in range(l_s)]
    
    for ind, inf in enumerate(infectedTrees):
        infectionPlans[ind].append(inf)
        
    while not areAllInfected(infectionArray):
        new_infections = [set() for x in range(l_s)]
        
        for ind in range(l_s):
            for tree in infectionPlans[ind]:
                for sasiad in G[tree]:
                    if not infectionArray[sasiad] + 1:
                        new_infections[ind].add(sasiad)
            infectionPlans[ind] = []
        
        cands = {}
        
        for fid in range(l_s):
            for tree in new_infections[fid]:
                if tree not in cands or fid < cands[tree]:
                    cands[tree] = fid
        
        if not cands:
            break
        
        
        for tree, fid in cands.items():
            infectionArray[tree] = fid
            infectionPlans[fid].append(tree)
    return sum(1 for x in infectionArray if x == fungusNrToCount)
    
    

