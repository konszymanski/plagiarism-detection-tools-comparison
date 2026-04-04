from typing import List


# czasowa O(n + m), gdzie n to ilosc pol, a m to ilosc przejsc - jest to zlozonosc BFS
# pamieciowa O(m + n) - ilosc elementow G, czyli ilosc polaczen + ilosc pol, 
# kazde pole nie laczy sie z innym


def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    n = len(G) 
    colour = [-1 for _ in range(n)]
    queue = []
    
    for i in range(len(infectedTrees)):
        tree = infectedTrees[i]
        queue.append(tree)
        colour[tree] = i
        
    while queue:
        tree = queue.pop(0)
        for i in G[tree]:
            if colour[i] == -1:
                colour[i] = colour[tree]
                queue.append(i)
                
    ans = 0                
    for i in colour:
        if i == fungusNrToCount:
            ans += 1
            
    return ans

