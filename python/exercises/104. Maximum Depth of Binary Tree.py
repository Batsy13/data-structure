import collections
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        count = 0
        queue = collections.deque()
        
        queue.append(root)
        
        if not root:
            return 0
        
        while queue:
            
            count += 1
            
            for _ in range(len(queue)):
                
                node = queue.popleft()
                    
                if node:
                    if node.right:
                        queue.append(node.right)
                    if node.left:
                        queue.append(node.left)
                        
        return count