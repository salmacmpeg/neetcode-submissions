class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashy = {}
        heap = []
        for elem in tasks:
            hashy[elem] = 1 + hashy.get(elem, 0)
        
        for elem, freq in hashy.items():
            heapq.heappush(heap, (-freq,elem,0))
        del hashy
        i =1
        queue = deque()
        t =qt =0
        while len(heap)+len(queue)!= 0:
            if len(heap)>0:
                freq,elem,t = heap[0]
                if t <=i: #process the queue
                    freq,elem,t = heapq.heappop(heap)
                    freq = -freq
                    if freq>1:
                        queue.append(((freq-1),elem,i+n))
            if len(queue)>0:
                qfreq,qelem,qt = queue[0]
                if qt <=i:
                    qfreq,qelem,qt = queue.popleft()
                    heapq.heappush(heap, (-qfreq,qelem,qt))

            i+=1
  
        return i-1