from typing import List

def heapinsert(heap, item):
    heap.append(item)
    i = len(heap) -1
    while i>0:
        parent = (i-2)//2
        if heap[parent] <= heap[i]:
            break
        heap[parent], heap[i] = heap[i], heap[parent]
        i = parent
        
def heappop(heap):
    if not heap:
        return None
    top = heap[0]
    last = heap.pop()
    if heap:
        heap[0] = last
        i = 0
        while True:
            left = 2 *i +1
            right = 2*i+2
            smallest = i
            if (left< len(heap) and heap[left]<heap[smallest]):
                smallest = left
            if (right< len(heap) and heap[right]<heap[smallest]):
                smallest = right
            if smallest == i:
                break
            heap[i], heap[smallest] = heap[smallest], heap[i]
            i = smallest
    return top
    
#zlozonosc czasowa to O(N+M+KlogK), gdzie n to liczba wierzcholkow, m to liczba krawedzi i k to liczba grzybow. BFS rozpresztrzenia sie na kazdy wierzcholek i krawedz
#heapinsert i heappop dzialaja logarytmicznie
def getCountOfInfectedTrees(G: List[List[int]], infectedTrees: List[int], fungusNrToCount: int) -> int:
    n = len(G)
    infected = [-1]*n
    time = [float("inf")]*n
     
    queue = []
    
    for i, tree in enumerate(infectedTrees):
        infected[tree] = i
        time[tree] = 0
        heapinsert(queue, (0, i, tree))
        
    while(queue):
        t, grzyb, tree = heappop(queue)
        
        for neighbour in G[tree]:
            if(time[neighbour])>t+1:
                time[neighbour]=t+1
                infected[neighbour] = grzyb
                heapinsert(queue, (t+1, grzyb, neighbour))
            elif(time[neighbour] == t+1 and grzyb < infected[neighbour]):
                infected[neighbour] = grzyb
                heapinsert(queue, (t+1, grzyb, neighbour))
                
    return infected.count(fungusNrToCount)

