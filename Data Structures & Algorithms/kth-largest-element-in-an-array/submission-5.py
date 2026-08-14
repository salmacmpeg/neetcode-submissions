class Solution:
    heap = []
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.heap =[]
        for elem in nums:
            heapq.heappush(self.heap, -elem)
        for i in range(k-1):
            _ = heapq.heappop(self.heap)
        return -heapq.heappop(self.heap)
