# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # Get length of list 
        l = 0
        counter = head
        while counter:
            counter = counter.next
            l+=1
        
        if l == 1:
            return None

        remove = l - n

        if remove == 0:
            return head.next

        ptr = head
        ptrn = ptr.next
        for _ in range(remove-1):
            ptr = ptrn
            ptrn = ptrn.next
        
        ptr.next = ptrn.next

        return head




        
        
        


        

        