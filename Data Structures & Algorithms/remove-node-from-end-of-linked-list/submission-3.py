# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #reverse and then use count and then reverse back
        
        prev = None
        cur = head
        i = 0
        while i < n and cur:
            cur = cur.next
            i+=1
        cur2 = head
        while cur:
            prev = cur2
            cur2 = cur2.next
            cur = cur.next
        if not prev:
            head = head.next
        else:
            prev.next = cur2.next
        return head
       # if n == 1:
        #    while cur.next:
         #       prev = cur
        #        cur = cur.next
        #    if not prev:
         #       return None
        #    prev.next = None
         #   return head

       # else:
          #  while cur:
          #      nxt = cur.next
          #      cur.next = prev

          #      prev = cur
          #      cur = nxt
            
         #   cur = prev
         #   prev2 = None
          #  i = 0
         #   while i < (n-1) and cur:
          #      prev2 = cur
         #       cur = cur.next
         #       i+=1
          #  if not prev2:
          #      cur.next = None
        #    if cur:
         #       prev2.next = cur.next
         #   else:
          #      prev2.next = None

          #  cur = prev
         #   prev = None
         #   while cur:
         #       nxt = cur.next
         #       cur.next = prev

         #       prev = cur
          #      cur = nxt

           # return prev




        
