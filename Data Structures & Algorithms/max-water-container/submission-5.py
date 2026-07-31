class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest =0 
        i =0 
        l = len(heights)
        while i < l-1:
            for j in range(i+1, l):
                miny = min(heights[i],heights[j])
                temp = miny*(j-i)
                largest = max(largest, temp)
            if i<l-1 and heights[i]==heights[i+1]:
                i+=1
            i+=1
        return largest