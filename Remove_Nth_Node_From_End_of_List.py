#Problem NUmber-19

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def mover(head: Optional[ListNode], n:int) -> bool:
            if n == 1 and head.next == None:
                return True
            elif n != 1 and head.next == None:
                return False
            else:                
                return mover(head.next, n-1)
            
        def ans(head: Optional[ListNode]):
            if mover(head.next, n):
                head.next = head.next.next                
            else:
                ans(head.next)
            
        prev = ListNode()
        prev.next = head
        ans_head = prev
        ans(prev)        
        
        return ans_head.next
