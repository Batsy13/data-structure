import collections
from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return node

        queue = collections.deque([node])

        clones = {}

        clones[node.val] = Node(node.val, [])

        while queue:
            current = queue.popleft()
            current_clone = clones[current.val]

            for n in current.neighbors:
                if n.val not in clones:
                    clones[n.val] = Node(n.val, [])
                    queue.append(n)

                current_clone.neighbors.append(clones[n.val])

        return clones[node.val]