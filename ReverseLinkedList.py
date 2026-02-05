# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
class ListNode:
    def __init__(self, val, next=None):
         self.val = val
         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(p, h):
            if not h:
                return p
            n = h.next
            h.next = p
            p = h
            h = reverse(p,n)
            return h

        new_head  = reverse(None, head)
        return new_head
