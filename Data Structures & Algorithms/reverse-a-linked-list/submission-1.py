# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        stack = []
        cur = head
        newHead = ListNode(0)
        while(cur != None):
            stack.append(cur.val)
            cur = cur.next
        newHead.val = stack[-1]
        stack.pop()
        cur = newHead
        while len(stack) > 0:
            cur.next = ListNode(stack[-1])
            stack.pop()
            cur = cur.next
        return newHead

            

        