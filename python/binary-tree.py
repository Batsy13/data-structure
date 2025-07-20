from collections import deque


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
    
    def _search_recursive(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        elif value > node.value:
            return self._search_recursive(node.right, value)
        
    def dfs(self, value):
        return self._dfs_recursive(self.root, value)
    
    def _dfs_recursive(self, node, value):
        if node:
            print(node.value)
        if node is None:
            return False
        if node.value == value:
            return True

        if self._dfs_recursive(node.left, value):
            return True

        if self._dfs_recursive(node.right, value):
            return True
        
    def bfs(self, value):
        if self.root == None:
            return False
        
        queue = deque()
        queue.append(self.root)
        
        while queue:
            node = queue.popleft()
            print(node.value)
            if node.value == value:
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        return False
        
    def preorder_traversal(self):
        result = []
        
        self._preorder_recursive(self.root, result)
        
        return result
    
    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)
            
    def inorder_traversal(self):
        result = []
        
        self._inorder_recursive(self.root, result)
        
        return result
    
    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)
            
    def postorder_traversal(self):
        result = []
        
        self._postorder_recursive(self.root, result)
        
        return result
    
    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)

binaryTree = BinaryTree()

binaryTree.insert(5)
binaryTree.insert(39)
binaryTree.insert(22)
binaryTree.insert(15)
binaryTree.insert(3)
binaryTree.insert(1)

print(f"Preorder traversal {binaryTree.preorder_traversal()}")
print(f"Inorder traversal: {binaryTree.inorder_traversal()}")
print(f"Postorder traversal: {binaryTree.postorder_traversal()}")

print(f"dfs: {binaryTree.dfs(22)}")
print(f"bfs: {binaryTree.bfs(22)}")