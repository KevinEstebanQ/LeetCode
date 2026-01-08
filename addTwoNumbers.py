from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1:Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = ListNode(0)
        curr = head
        while l1 != None or l2 != None or carry != 0: #stop algorith if l1 and l2 are none and carry is also 0
            num1 = l1.val if l1 else 0 # get the head of the linked lists
            num2 = l2.val if l2 else 0

            currentSum = num1 + num2 + carry #calculate the current sum of iteration
            carry = currentSum // 10 # calculate the carry
            newNode = ListNode(currentSum%10) #create a new node, make sure its less than 10
            curr.next = newNode #update answer of linked list

            curr = newNode # advance pointers
            l1 = l1.next if l1 else None 
            l2 = l2.next if l2 else None
        return head.next


            


