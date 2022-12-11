class MinStack:

    def __init__(self):
        self.s = []
        

    def push(self, val: int) -> None:
        self.s.append(val)
        

    def pop(self) -> None:
        return self.s.pop()
        

    def top(self) -> int:
        return self.s[-1]
        

    def getMin(self) -> int:
        min1 = self.s[-1]
        for i in range(len(self.s) -1):
            if min1 > self.s[i]:
                min1 = self.s[i]
        return min1
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()