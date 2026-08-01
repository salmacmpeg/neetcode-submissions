class MinStack:

    def __init__(self):
        self.stacky =[]
        self.mins = []
        self.i=-1

    def push(self, val: int) -> None:
        self.stacky.append(val)
        self.i+=1

        if len(self.mins)==0:
            self.mins.append(self.i)
        else:
            if val < self.stacky[self.mins[-1]]:
                self.mins.append(self.i)


    def pop(self) -> None:
        if len(self.stacky)==0:
            return 
        
        val = self.stacky.pop()
        if self.mins[-1] == self.i :
            self.mins.pop()
        self.i-=1


    def top(self) -> int:
        if len(self.stacky)>0: return self.stacky[-1]
        return 0

    def getMin(self) -> int:
        if len(self.stacky)>0: return self.stacky[self.mins[-1]]
        return 0
        
