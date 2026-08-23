# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        before_left = head
        left = head
        right = head

        if(right.next==None and n==1):
            return None

        for i in range(n-1):
            right = right.next
            # if(right.next==None):
            #     return []
        
        if(right.next!=None):
            left = left.next
            right = right.next
        else:
            before_left.next = left.next
            return left.next

        while(right.next!=None):
            before_left = before_left.next
            left = left.next
            right = right.next
        
        before_left.next = left.next


        return head 
            