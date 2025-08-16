class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self._size = 0
        
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self._size += 1
        
    def pop(self):
        if self._size == 0:
            raise IndexError("Empty Stack")
        
        popped_node = self.top
        self.top = popped_node.next
        self._size -= 1
        
        return popped_node.value
    
    def peek(self):
        if self._size == 0:
            raise IndexError("Empty Stack")
        
        return self.top.value
    
    def isEmpty(self):
        return self._size == 0
    
    def size(self):
        return self._size
    
stack = Stack()

if stack.isEmpty():
    print("Yes")
else: 
    print("No")

stack.push(1)
stack.push(2)
stack.push(3)

print("Pop: ", stack.pop())
print("Peek: ", stack.peek())
print("Size: ", stack.size())