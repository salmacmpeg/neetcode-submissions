class KthLargest:
    minheap =[]
    gk= 0
    def __init__(self, k: int, nums: List[int]):
        #we need to maintain a k element min heap
        self.gk =k
        n =len(nums)
        if n < k:
            self.minheap = nums
            heapq.heapify(self.minheap)
            return
        self.minheap = nums[:k]
        heapq.heapify(self.minheap)
        i = k
        while i < n:
            if nums[i] >= self.minheap[0]:
                heapq.heapreplace(self.minheap,nums[i]) 
            i+=1
        print("after initial k ",self.minheap)
    def add(self, val: int) -> int:
        #if the val > min (heap top), we should replace the top with it
        #return the heap
        if len(self.minheap)<1:
            self.minheap =[]
            heapq.heappush(self.minheap, val)
            return val
        if len(self.minheap) <  self.gk:
            heapq.heappush(self.minheap, val)
        elif val >= self.minheap[0] :
            heapq.heapreplace(self.minheap,val)
        print("self.minheap",self.minheap, self.minheap[0], "add", val)
        return heapq.nlargest(self.gk,self.minheap)[-1]