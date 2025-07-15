from typing import Optional

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        ahead = head
        
        while ahead and ahead.next:
            ahead = ahead.next.next
            head = head.next
        return head