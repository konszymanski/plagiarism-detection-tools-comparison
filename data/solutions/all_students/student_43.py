from typing import List


def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    Q=[]
    discovered=set()
    dictionary={}
    for i in range(len(infectedTrees)):
        discovered.add(infectedTrees[i])
        q=[]
        q.append(infectedTrees[i])
        Q.append(q)
        dictionary[infectedTrees[i]]=i
    size=len(infectedTrees)
    while size>0:
        v=[]
        for i in range(len(Q)):
            if len(Q[i])<=0:
                v.append(None)
            else:
                v.append(Q[i])
            Q[i]=[]
        size=0
        for i in range(len(v)):
            cur=v[i]
            if cur==None:
                continue
            for node in cur:
                for neighbour in G[node]:
                    if neighbour not in discovered:
                        discovered.add(neighbour)
                        dictionary[neighbour]=i
                        Q[i].append(neighbour)
                        size+=1
    infected=[key for key in dictionary if dictionary[key]==fungusNrToCount]
    return len(infected)
    
                

