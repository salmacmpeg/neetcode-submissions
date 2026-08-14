class Solution:
    heap =[]
  
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.heap =[]
        for elem in points:
            dist = math.sqrt(elem[0]*elem[0] + elem[1]*elem[1])
            heapq.heappush(self.heap, (dist, elem))
        res= []
        for i in range(k):
            elem = heapq.heappop(self.heap)
            res.append(elem[1])
        return res