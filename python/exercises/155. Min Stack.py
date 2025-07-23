class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []
        
    def push(self, val) -> None:    
        self.stack.append(val) 
        if self.minStack:
            val = min(self.minStack[-1], val)
        self.minStack.append(val)       
            
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minStack[-1]
    
minStack = MinStack()

minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())  # Return -3
minStack.pop()
print(minStack.top())     # Return 0
print(minStack.getMin())  # Return -2