# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        def printList(node):
            while node:
                print(f"{node.val}, ")
                node = node.next



        # Get length of list 
        l = 0
        counter = head
        while counter:
            counter = counter.next
            l+=1

        print(l)
        
        if l == 1:
            return None
        
        # Reversal no. 1
        cur = head
        prev = nxt = None
        while cur:
            nxt = cur.next
            cur.next = prev

            prev = cur
            cur = nxt

        print("first rev")
        printList(prev)

        # Locating and removing node
        ptr = prev
        ptrn = ptr.next

        # If the head needs to be removed
        if n == 1:
            rev_cur = ptrn

        # Otherwise somewhere else in the list
        else:
            print("removing from somewhere in the list")
            i = 1
            while i < (n) - 1:
                print(ptr.val, ptrn.val)
                ptr = ptrn
                ptrn = ptrn.next
                i+=1
            ptr.next = ptrn.next
            print(ptr.val, ptrn.val)
            rev_cur = prev

        print("removal")
        printList(prev)

        # Reversal no. 2
        rev_next = rev_prev = None
        while rev_cur:
            rev_next = rev_cur.next
            rev_cur.next = rev_prev

            rev_prev = rev_cur
            rev_cur = rev_next

        # Return head of reverse list
        print("sec rev")
        printList(rev_prev)
        return rev_prev


        

        