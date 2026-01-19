from typing import Optional

class Solution:
    
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def getGCD(a:int, b:int)->int:
            while b:
                a, b = b, a % b
            return a

        curr = head
        nextNode = curr.next

        while curr.next != None:
            GCD = getGCD(curr.val, nextNode.val)
            newNode = ListNode(val=GCD)

            curr.next = newNode
            newNode.next = nextNode
            curr = nextNode
            nextNode = curr.next

        return head