class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashy = {}
        for elem in nums:
            hashy[elem]=(hashy.get(elem,0)+1)

        myheap = []
        for elem, fre in hashy.items():
            heapq.heappush(myheap,[fre,elem])
            if len(myheap)>k:
                heapq.heappop(myheap)
        
        final_list = [ elem for freq,elem in myheap]
     
        return final_list
        