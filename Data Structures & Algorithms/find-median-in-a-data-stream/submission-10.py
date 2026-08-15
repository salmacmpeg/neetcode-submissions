class MedianFinder:

    def __init__(self):
        self.numsl=[]
        self.numsr=[]

    def addNum(self, num: int) -> None:
        tempr = -self.numsl[0] if len(self.numsl)>0 else -200000
        templ = self.numsr[0] if len(self.numsr)>0 else -200000
        if len(self.numsl)> 0:
            tempr = - self.numsl[0]
        if len(self.numsr)>0:
            templ = self.numsr[0]
        # print("tempr", tempr, "templ", templ, "num", num)

        if num >= tempr :
            # print("inside insert right")
            #insert at the right tree
            heapq.heappush(self.numsr, num)
            #then check if the right - left > 1 , then remove the min to the left
            if len(self.numsr) - len(self.numsl) >1:
                numr = heapq.heappop(self.numsr)
                heapq.heappush(self.numsl, -numr)
                return
        elif num <= templ:
            # print("inside insert left")
            heapq.heappush(self.numsl, -num)
            if len(self.numsl) - len(self.numsr) >1:
                numlneg = heapq.heappop(self.numsl)
                heapq.heappush(self.numsr, -numlneg)
        # print("self.numsl",self.numsl)
        # print("self.numsr",self.numsr)

    def findMedian(self) -> float:
        lenl = len(self.numsl)
        lenr = len(self.numsr)

        if lenl == lenr:
            numl = - self.numsl[0]
            numr = - self.numsr[0]
            return float(numl-numr) / 2
        if lenl>lenr:
            return - self.numsl[0]
        
        return self.numsr[0]

        