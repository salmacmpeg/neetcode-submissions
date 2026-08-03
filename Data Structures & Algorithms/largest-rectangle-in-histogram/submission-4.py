class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        mstack =[]
        max_area=0

        for i,h in enumerate(heights):
            if len(mstack) == 0 or h>mstack[-1][1]:
                mstack.append((i,h))
            else:
                last_i = i
                while len(mstack) > 0 and h<=mstack[-1][1]:
                    (popi, poph)= mstack.pop()
                    area = (i-popi)*poph
                    max_area = max(max_area,area)
                    last_i=popi
                mstack.append((last_i,h))
        i+=1
        while len(mstack) > 0:
                    (popi, poph)= mstack.pop()
                    area = (i-popi)*poph
                    max_area = max(max_area,area)

        return max_area
