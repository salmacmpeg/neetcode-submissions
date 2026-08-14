class Solution:
    hstone= []
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.hstone= []
        for elem in stones:
            heapq.heappush(self.hstone,-elem)
            print("elem", elem, self.hstone)
        print("self.hstone", self.hstone, "stones", stones)
        while (len(self.hstone)>1):
            elem1 = - heapq.heappop(self.hstone)
            elem2 = - heapq.heappop(self.hstone)
            elem3 = abs(elem1- elem2)
            if elem3>0:
                heapq.heappush(self.hstone, -(elem3))
        if len(self.hstone)==0 :
            return 0
        else:
            return -self.hstone[0]
        
