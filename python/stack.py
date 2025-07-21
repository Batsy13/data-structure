class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)
    
    def is_empty(self):
        return len(self.items) == 0
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Empty List")
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Empty List")
        return self.items[-1]
    
    def size(self):
        return len(self.items)    
    
class BetterStack:
    def __init__(self, max_length=1000):
        self.items = [0] * max_length
        self.max_length = max_length
        self.pointer = 0
    
    def push(self, item):
        if self.pointer > self.max_length:
            raise IndexError("Full Stack")
        self.items[self.pointer] = item
        self.pointer += 1
    
    def is_empty(self):
        return self.pointer == 0 
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Empty List")
        
        self.pointer -= 1
        leaving = self.items[self.pointer]
        self.items[self.pointer] = 0
        return leaving
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Empty List")
        return self.items[self.pointer - 1]
    
    def size(self):
        return self.pointer
    
stack = Stack()
better_stack = BetterStack(3)

stack.push(1)
stack.push(2)

better_stack.push(1)
better_stack.push(2)

print("Size: ", stack.size())
print("Size: ", better_stack.size())

print("Leaving Stack: ", stack.pop())
print("Leaving BetterStack: ", better_stack.pop())
print("Leaving Stack: ", stack.pop())
print("Leaving BetterStack: ", better_stack.pop())

stack.push(1)
stack.push(2)
stack.push(32)

better_stack.push(1)
better_stack.push(2)
better_stack.push(34)

print("Peek Stack: ", stack.peek())
print("Peek BetterStack: ", better_stack.peek())

stack.push(42)
better_stack.push(42)