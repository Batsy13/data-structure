class Node:
    def __init__(self, value=0) -> None:
        self.value = value
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self) -> None:
        self.root = None
        
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(value, self.root)
            
    def _insert_recursive(self, value, node):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(value, node.left)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(value, node.right)
    
    def search(self, value):
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value ):
        if node is None:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        elif value > node.value:
            return self._search_recursive(node.right, value)
        

binaryTree = BinaryTree()

binaryTree.insert(5)
binaryTree.insert(39)
binaryTree.insert(22)
binaryTree.insert(15)
binaryTree.insert(3)
binaryTree.insert(1)

if binaryTree.search(3):
    print("I found the number")
else: 
    print("I didn't find the number")